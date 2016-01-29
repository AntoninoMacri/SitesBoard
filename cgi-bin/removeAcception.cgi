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

my $idInsertion = $cgi->param('idInsertion');
my $usernameUserInsertion = $cgi->param('idUsername');

#controllo se si è loggati
if(defined($session))
{

	my $userUsername = $session->param('username');
	my $userPassword = $session->param('password');

	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser per ottenere l'id utente loggato
	my $doc = $parser->parse_file($file) || die("File non trovato");
	my $idUser=$doc->findnodes('/bacheca/persona[user/text()="'.$userUsername.'" and password/text()="'.$userPassword.'"]/@id'); 

	#trovo l'annuncio
	my $nodoInsertion=$doc->findnodes('/bacheca/persona[user/text()="'.$usernameUserInsertion.'"]/listaAnnunci/annuncio[@id="'.$idInsertion.'"]/listaDisponibili/idProgrammatore[text()="'.$idUser.'"]'); 

	if(!defined($nodoInsertion))
	{
		print $cgi->redirect( 'profile.cgi?msgError=Errore nella rimozione dell\'accetazione.' );
	}
	else
	{
		my $bacheca = $nodoInsertion->parentNode;

		#elimino il figlio
		$bacheca->removeChild($nodoInsertion);

		#serializzazione
		open(OUT, ">../data/database.xml");
		print OUT $doc->toString;
		close(OUT);
		

		print $cgi->redirect( 'showInsertions.cgi' );
	}
}
else
{
	print $cgi->redirect( 'login.cgi' );
}


