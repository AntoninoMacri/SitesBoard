#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use XML::XPath;
use Net::SMTP;

require 'functions/function.cgi';
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
my $recover_ConfirmPassword=$cgi->param('recover_re_pass');

my $url=recoveryControl($recover_name,$recover_surname,$recover_year,$recover_month,$recover_day, $recover_username ,$recover_email,$recover_pass,$recover_ConfirmPassword);

#controllo se ci sono tutti i dati
if($url eq 1)
{
	
	if(length $recover_month== 1){ $recover_month='0'.$recover_month; }
	if(length $recover_day== 1){ $recover_day='0'.$recover_day; }

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
	print $cgi->redirect($url);
}


