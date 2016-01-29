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
$userInsertion = $cgi->param('idInsertion');


#controllo se si è loggati
if(defined($session) &&  defined($userInsertion))
{

	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser
	my $doc = $parser->parse_file($file) || die("File non trovato");
	my $userNode = $doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]/listaAnnunci/annuncio[@id="'.$userInsertion.'"]')->get_node(1);

	if(!defined($userNode))
	{
		print $cgi->redirect( 'showInsertions.cgi?msgError=Inserzione non trovata.' );
	}
	else
	{
		my $bacheca = $userNode->parentNode;

		#elimino il figlio
		$bacheca->removeChild($userNode);

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


