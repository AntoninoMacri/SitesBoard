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
if(defined($session) && define($newUserName) && define($newUserSurname) && define($newUserAge) && define($newUserUsername) && define($newUserEmail))
{
	my $userUsername = $session->param('username');
	my $userPassword = $session->param('password');
	
	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser per ottenere l'id utente loggato
	my $doc = $parser->parse_file($file) || die("File non trovato");
	my $idUser=$doc->findnodes('/bacheca/persona[user/text()="'.$userUsername.'" and password/text()="'.$userPassword.'"]/@id'); 

	#trovo i nodi che si devono cambiare
	my $nodeChangeName=$doc->findnodes('/bacheca/persona[@id="'.$idUser.'"]/name');
	my $nodeChangeSurname=$doc->findnodes('/bacheca/persona[@id="'.$idUser.'"]/surname');
	my $nodeChangeAge=$doc->findnodes('/bacheca/persona[@id="'.$idUser.'"]/age');
	my $nodeChangeUsername=$doc->findnodes('/bacheca/persona[@id="'.$idUser.'"]/user');
	my $nodeChangeEmail=$doc->findnodes('/bacheca/persona[@id="'.$idUser.'"]/email');


	if(!defined($nodeChangeName) || !defined($nodeChangeSurname)|| !defined($nodeChangeAge)|| !defined($nodeChangeUsername) || !defined($nodeChangeEmail))
	{
		print $cgi->redirect( 'profileChange.cgi?msgError=Errore modifica del profilo.' );
	}
	else
	{
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
		

		print $cgi->redirect( 'logout.cgi' );
	}
}
else
{
	print $cgi->redirect( 'login.cgi' );
}


