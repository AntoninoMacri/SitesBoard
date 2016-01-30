#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use XML::XPath;

require 'functions/session_function.cgi';

#ottengo la sessione
my $session = getSession();
my $cgi = CGI->new();

#parametri
my $newUserName = $cgi->param('name');
my $newUserSurname = $cgi->param('surname');
my $newUserAge = $cgi->param('age');
my $newUserUsername = $cgi->param('username');
my $newUserEmail = $cgi->param('email');

#controllo se si è loggati
if(defined($session) && defined($newUserName) && defined($newUserSurname) && defined($newUserAge) && defined($newUserUsername) && defined($newUserEmail))
{
	my $userUsername = $session->param('username');
	my $userPassword = $session->param('password');
	
	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser per ottenere l'id utente loggato
	my $doc = $parser->parse_file($file) || die("File non trovato");
	my $idUser=$doc->findnodes('/bacheca/persona[user/text()="'.$userUsername.'" and password/text()="'.$userPassword.'"]/@id')->get_node(1);
	#nodo non trovato
	if(!defined($idUser))
	{
		print $cgi->redirect( 'profileChange.cgi?msgError=Errore modifica del profilo.' );
	}

	#trovo i nodi che si devono cambiare
	my $nodeChangeName=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/nome/text()')->get_node(1);
	my $nodeChangeSurname=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/cognome/text()')->get_node(1);
	my $nodeChangeAge=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/dataNascita/text()')->get_node(1);
	my $nodeChangeUsername=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/user/text()')->get_node(1);
	my $nodeChangeEmail=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/mail/text()')->get_node(1);


	if(defined($nodeChangeName) && defined($nodeChangeSurname)&& defined($nodeChangeAge)&& defined($nodeChangeUsername) &&defined($nodeChangeEmail))
	{

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
				print $cgi->redirect( 'proffileChange.cgi?msgError=Email già presente nel sistema' );
			}
			#altrimenti continua
		}
		else{
			#username già in uso
			print $cgi->redirect( 'proffileChange.cgi?msgError=Username già presente nel sistema');
		}

		#modifica i campi
		$nodeChangeName->setData($newUserName); 
		$nodeChangeSurname->setData($newUserSurname); 
		$nodeChangeAge->setData($newUserAge); 
		$nodeChangeUsername->setData($newUserUsername); 
		$nodeChangeEmail->setData($newUserEmail); 

		#serializzazione
		open(OUT, ">../data/database.xml");
		print OUT $doc->toString;
		close(OUT);
	}
	else
	{
		print $cgi->redirect( 'profileChange.cgi?msgError=Errore modifica del profilo.' );
	}
}
else
{
	print $cgi->redirect( 'login.cgi' );
}


