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

#controllo se si è loggati
if(defined($session))
{

	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser
	my $doc = $parser->parse_file($file) || die("File non trovato");
	my $userNode = $doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]')->get_node(1);
	if(!defined($userNode))
	{
		print $cgi->redirect( 'profile.cgi?msgError=Errore cancellazione del profilo.' );
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
		

		print $cgi->redirect( 'logout.cgi' );
	}
}
else
{
	print $cgi->redirect( 'login.cgi' );
}


