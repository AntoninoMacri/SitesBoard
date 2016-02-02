#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use XML::XPath;
use POSIX qw(strftime);


require 'functions/session_function.cgi';

#ottengo la sessione
my $cgi = CGI->new();

my $newUserName = $cgi->param('reg_name');
my $newUserSurname = $cgi->param('reg_surname');
my $newUserYear = $cgi->param('reg_year');
my $newUserMonth = $cgi->param('reg_month');
my $newUserDay = $cgi->param('reg_day');
my $newUserUsername = $cgi->param('reg_username');
my $newUserEmail = $cgi->param('reg_email');
my $newUserPassword = $cgi->param('reg_pass');



#controllo se ci sono tutti i dati
if(defined($newUserName)&&  
	defined($newUserSurname)&&  defined($newUserYear)&&  
	defined($newUserMonth)&&  defined($newUserDay)&& 
	defined($newUserUsername)&&  defined($newUserEmail)&& defined($newUserPassword))
{

	if(length $newUserMonth== 1){ $newUserMonth='0'.$newUserMonth; }
	if(length $newUserDay== 1){ $newUserDay='0'.$newUserDay; }

	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser
	my $doc = $parser->parse_file($file) || die("File non trovato");

	#Ottengo tutti gli id e gli user con i stessi dati del nuovo utente
	# se ritorna qualcosa allora significa che segnalo all'utente che i campi username ed email sono già presenti nel DB
	my @check_result=$doc->findnodes('/bacheca/persona[user/text()="'.$newUserUsername.'"]'); 
	if(@check_result == 0)
	{
		#username non presente dunque controllo l'email
		my @check_result2 =$doc->findnodes('/bacheca/persona[mail/text()="'.$newUserEmail.'"]'); 
		if(@check_result2  != 0)
		{
			#email già in uso
			print $cgi->redirect( 'registration.cgi?msgError=Email già presente nel sistema' );
		}
		#altrimenti continua
	}
	else{
		#username già in uso
		print $cgi->redirect( 'registration.cgi?msgError=Username già presente nel sistema');
	}

	#ottengo tutti gli id di tutti gli utenti
	my @id_result=$doc->findnodes('/bacheca/persona/@id'); 
	#scorro la lista per ottenere l'id più grande
	my $highest;
	for (@id_result) {
		if($_->nodeValue > $highest)
		{
			$highest = $_->nodeValue;
		}
	}
	$highest = $highest +1; 
	
	#inserisco l'utente nel db
	my $insertion='<persona id="'.$highest.'">
					<nome>'.$newUserName.'</nome>
					<cognome>'.$newUserSurname.'</cognome>
					<dataNascita>'.$newUserYear.'-'.$newUserMonth.'-'.$newUserDay.'</dataNascita>
					<user>'.$newUserUsername.'</user>
					<password>'.$newUserPassword.'</password>
					<mail>'.$newUserEmail.'</mail>
					<biografia></biografia>
					<listaAnnunci>
					</listaAnnunci>
					</persona>';

	#verifico sia bilanciata
	my $frammento = $parser->parse_balanced_chunk($insertion);

	#ottengo il nodo padre di persona
	my $bacheca=$doc->findnodes('/bacheca')->get_node(1); 

	#inserisco un nuovo figlio
	$bacheca->appendChild($frammento);

	#serializzazione
	open(OUT, ">../data/database.xml");
	print OUT $doc->toString;
	close(OUT);

	#creazione sessione
	my $sessione = createSession($newUserUsername,$newUserPassword);
	print $sessione->header(-location=>"profile.cgi");


	print $cgi->redirect( 'profile.cgi' );
}
else
{
	print $cgi->redirect( 'login.cgi' );
}


