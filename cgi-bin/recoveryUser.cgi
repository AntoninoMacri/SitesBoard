#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use XML::XPath;
use Net::SMTP;


require 'functions/session_function.cgi';

#ottengo la sessione
my $cgi = CGI->new();

#my $recover_name= $cgi->param('recover_name');
#my $recover_surname = $cgi->param('recover_surname');
#my $recover_email = $cgi->param('recover_email');
my $recover_name= "Antonino";
my $recover_surname = "Macrì";
my $recover_email = "davider1994\@gmail.com";


#controllo se ci sono tutti i dati
if(defined($recover_name)&&  defined($recover_surname)&&  defined($recover_email))
{

	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser
	my $doc = $parser->parse_file($file) || die("File non trovato");


	#cerco l'utente nel database
	my @check_result=$doc->findnodes('/bacheca/persona[nome/text()="'.$recover_name.'" and cognome/text()="'.$recover_surname.'" and mail/text()="'.$recover_email.'"]'); 
	print "Content-type: text/html\n\n";
	#se esiste gli invio una mail
	if(!(@check_result == 0))
	{  	
		#genero password a random
		my $newUserPassword = "Password a caso";

		#prendo il nodo password
		my $userPassword = $doc->findnodes('/bacheca/persona[nome/text()="'.$recover_name.'" and cognome/text()="'.$recover_surname.'" and mail/text()="'.$recover_email.'"]/password/text()')->get_node(1); 
		
		#cambio password
		$userPassword->setData($newUserPassword);
        
		#invio l'email all'utente contenete la nuova password
		my $userUsername = $doc->findnodes('/bacheca/persona[nome/text()="'.$recover_name.'" and cognome/text()="'.$recover_surname.'" and mail/text()="'.$recover_email.'"]/user/text()')->get_node(1); 
		my $mailFrom = "recovery_password@sitesboard.com";
		my $mailTo = $recover_email;
		my $mailObject = "Riprestino Password";
		my $mailTesto = "E' stata effettuata la procedura di cambio password a SitesBoard.\n
						I nuovi dati di accesso sono:
						Username: ".$userUsername."\n
						Password: ".$newUserPassword."\n
						\n
						Cordiali saluti da SitesBoard.";

		my $smtp = Net::SMTP->new($mailObject,
			Hello => $mailObject,
			Timeout => 30,
			Debug => 1);
		$smtp->mail($mailFrom);
		$smtp->to($mailTo);
		$smtp->data();
		$smtp->datasend($mailTesto);
		$smtp->dataend();
		$smtp->quit;

		#serializzazione
		open(OUT, ">../data/database.xml");
		print OUT $doc->toString;
		close(OUT);

		print $cgi->redirect( 'login.cgi' );
	}
	else{
		#utente non presente nel db
		print $cgi->redirect( 'home.cgi' );
	}
}
else
{
	print $cgi->redirect( 'home.cgi' );
}


