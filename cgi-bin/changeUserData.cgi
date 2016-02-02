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
my $newUserYear= $cgi->param('year');
my $newUserMonth = $cgi->param('month');
my $newUserDay = $cgi->param('day');
my $newUserPass = $cgi->param('password');
my $newUserEmail = $cgi->param('email');
my $newUserBio = $cgi->param('bio');
#creo la data nel formato giusto
my $newUserDate = $newUserYear."-".$newUserMonth."-".$newUserDay;

#controllo se si è loggati
if(defined($session) && defined($newUserName) && defined($newUserSurname) && defined($newUserYear) && defined($newUserMonth)
	&& defined($newUserDay)&& defined($newUserPass)&& defined($newUserEmail)&& defined($newUserBio))
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
	my $nodeChangeDate=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/dataNascita/text()')->get_node(1);
	my $nodeChangeEmail=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/mail/text()')->get_node(1);
	my $nodeChangePassword=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/password/text()')->get_node(1);
	my $nodeChangeBiografia=$doc->findnodes('/bacheca/persona[@id="'.$idUser->nodeValue.'"]/biografia/text()')->get_node(1);


	if(defined($nodeChangeName) && defined($nodeChangeSurname)&& defined($nodeChangeDate) &&defined($nodeChangeEmail)
		&&defined($nodeChangePassword)&&defined($nodeChangeBiografia))
	{

		#Ottengo tutti gli id e gli user con i stessi dati del nuovo utente

		#controllo l'email se è gia presente
		my @check_result2 =$doc->findnodes('/bacheca/persona[mail/text()="'.$newUserEmail.'"]'); 
		if(@check_result2  != 0)
		{
			#email già in uso
			print $cgi->redirect( 'proffileChange.cgi?msgError=Email già presente nel sistema' );
		}
		#altrimenti continua

		#modifica i campi
		$nodeChangeName->setData($newUserName); 
		$nodeChangeSurname->setData($newUserSurname); 
		$nodeChangeDate->setData($newUserDay); 
		$nodeChangeEmail->setData($newUserEmail); 
		$nodeChangePassword->setData($newUserPass); 
		$nodeChangeBiografia->setData($newUserBio); 

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


