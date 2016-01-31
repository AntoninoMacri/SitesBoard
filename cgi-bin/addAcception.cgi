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
my $idUserInsertion = $cgi->param('idUserInsertion');

#controllo se si è loggati
if(defined($session) && defined($idInsertion) && defined($idUserInsertion))
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
	my $nodoInsertion=$doc->findnodes('/bacheca/persona[@id="'.$idUserInsertion.'"]/listaAnnunci/annuncio[@id="'.$idInsertion.'"]/listaDisponibili')->get_node(0); 

	if(defined($nodoInsertion))
	{
		my $insertion='<idProgrammatore>'.$idUser.'</idProgrammatore>';
		#verifico sia bilanciata
		my $frammento = $parser->parse_balanced_chunk($insertion);

		#inserisco un nuovo figlio
		$nodoInsertion->appendChild($frammento);

		#serializzazione
		open(OUT, ">../data/database.xml");
		print OUT $doc->toString;
		close(OUT);
		

		print $cgi->redirect( 'showAcceptions.cgi' );
	}
	else
	{
		print $cgi->redirect( 'showAcceptions.cgi?msgError=Errore nella rimozione dell\'accetazione.' );
	}
}
else
{
	print $cgi->redirect( 'login.cgi' );
}


