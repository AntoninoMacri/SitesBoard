#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use XML::XPath;
use POSIX qw(strftime);


require 'functions/session_function.cgi';

#ottengo la sessione
my $session = getSession();
my $cgi = CGI->new();

#my $titleInsertion = $cgi->param('titolo');
#my $objectInsertion = $cgi->param('oggetto');
#my $descriptionInsertion = $cgi->param('descrizione');

my $titleInsertion = "prova";
my $objectInsertion = "prova";
my $descriptionInsertion = "prova";


#controllo se si è loggati
if(defined($session) &&  defined($titleInsertion)&&  defined($objectInsertion)&&  defined($descriptionInsertion))
{
	my $userUsername = $session->param('username');
	my $userPassword = $session->param('password');
	#creazione oggetto e dichiarazione variabili
	my $file = '../data/database.xml';  
	my $parser = XML::LibXML->new();
	
	#parser
	my $doc = $parser->parse_file($file) || die("File non trovato");

	#ottengo tutti gli id di tutti gli annunci
	my $id_annuncio=$doc->findnodes('/bacheca/persona[user/text()="'.$userUsername.'" and password/text()="'.$userPassword.'"]/listaAnnunci/annuncio/@id'); 
	#scorro la lista per ottenere l'id più grande
	my $highest;
	for (my $x=1; $x <= $id_annuncio->size; $x++) {
		if($id_annuncio > $highest)
		{
			$highest = $id_annuncio->to_literal;
		}
	}

	print "Content-type: text/html\n\n";
	print $id_annuncio;

	my $userNode = $doc->findnodes('/bacheca/persona[user/text()="'.$userUsername.'" and password/text()="'.$userPassword.'"]/listaAnnunci')->get_node(1);

	if(!defined($userNode))
	{
		print $cgi->redirect( 'addInsertions.cgi?msgError=Errore nell\'inserimento dell\'inserzione.' );
	}
	else
	{
		my $data = strftime "%F", gmtime;

		my $insertion='<annuncio id="'.$highest.'">
							<titolo>'.$titleInsertion.'</titolo>
							<oggetto>'.$objectInsertion.'</oggetto>
							<descrizione>'.$descriptionInsertion.'</descrizione>
							<tipologia>Social</tipologia>
							<data>'.$data.'</data>
							<listaDisponibili>
								<idProgrammatore>1</idProgrammatore>
							</listaDisponibili>
						</annuncio>';



		#verifico sia bilanciata
		my $frammento = $parser->parse_balanced_chunk($insertion);

		#inserisco un nuovo figlio
		$userNode->appendChild($frammento);

		#serializzazione
		open(OUT, ">../data/database.xml");
		print OUT $doc->toString;
		close(OUT);

		print $cgi->redirect( 'showInsertion.cgi' );
	}
}
else
{
	print $cgi->redirect( 'login.cgi' );
}


