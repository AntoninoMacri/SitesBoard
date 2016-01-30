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

my $recover_name= $cgi->param('recover_name');
my $recover_surname = $cgi->param('recover_surname');
my $recover_year = $cgi->param('recover_year');
my $recover_month = $cgi->param('recover_month');
my $recover_day = $cgi->param('recover_day');
my $recover_username = $cgi->param('recover_username');
my $recover_email = $cgi->param('recover_email');
my $recover_pass = $cgi->param('recover_pass');



#controllo se ci sono tutti i dati
if(defined($recover_name) &&  defined($recover_surname)&&  defined($recover_year)&&  defined($recover_month)
	&&  defined($recover_day)&&  defined($recover_username)&&  defined($recover_email)&&  defined($recover_pass))
{
	#creazione data di nascita
	my $dataNascita = $recover_year."-".$recover_month."-".$recover_day;
	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser
	my $doc = $parser->parse_file($file) || die("File non trovato");

	#cerco l'utente nel database
	my @check_result=$doc->findnodes('/bacheca/persona
		[nome/text()="'.$recover_name.'" and cognome/text()="'.$recover_surname.'" and dataNascita/text()="'.$dataNascita.'" and
			user/text()="'.$recover_username.'" and mail/text()="'.$recover_email.'"]'); 
	
	#se esiste cambio la password
	if(!(@check_result == 0))
	{  	

		my $nodeResult=$doc->findnodes('/bacheca/persona[user/text()="'.$recover_username.'"]/password/text()')->get_node(1); 
		$nodeResult->setData($recover_pass);

		#serializzazione
		open(OUT, ">../data/database.xml");
		print OUT $doc->toString;
		close(OUT);

		print $cgi->redirect( 'login.cgi' );
	}
	else{
		#utente non presente nel db
		print $cgi->redirect( 'login.cgi' );
	}
}
else
{
	#redirect
	print $cgi->redirect( 'home.cgi' );
}


