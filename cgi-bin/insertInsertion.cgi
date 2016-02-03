#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use XML::XPath;
use POSIX qw(strftime);

require 'functions/function.cgi';
require 'functions/session_function.cgi';

#ottengo la sessione
my $session = getSession();
my $cgi = CGI->new();

my $titleInsertion = $cgi->param('addTitolo');
my $objectInsertion = $cgi->param('addOggetto');
my $descriptionInsertion = $cgi->param('addDescrizione');
my $TipoInsertion = $cgi->param('addTipologia');

#pulizia e correzione input
$TipoInsertion = extractType($TipoInsertion); #tolgo le virgolette inserite dalla select
$titleInsertion = inputControl($titleInsertion);
$objectInsertion = inputControl($objectInsertion);
$descriptionInsertion = inputControl($descriptionInsertion);
$TipoInsertion = inputControl($TipoInsertion);

my $url=addInsertionControl($titleInsertion,$objectInsertion, $descriptionInsertion);

#controllo se si è loggati
if(defined($session))
{
	if($url eq 1 && defined($TipoInsertion))
		{
		my $userUsername = $session->param('username');
		my $userPassword = $session->param('password');
		#creazione oggetto e dichiarazione variabili
		my $file = '../data/database.xml';  
		my $parser = XML::LibXML->new();
		
		#parser
		my $doc = $parser->parse_file($file) || die("File non trovato");

		#ottengo tutti gli id di tutti gli annunci
		my @id_annuncio=$doc->findnodes('/bacheca/persona[user/text()="'.$userUsername.'" and password/text()="'.$userPassword.'"]/listaAnnunci/annuncio/@id'); 
		#scorro la lista per ottenere l'id più grande
		my $highest;

		for (@id_annuncio) {
			if($_->nodeValue > $highest)
			{
				$highest = $_->nodeValue;
			}
		}

		$highest = $highest + 1;
		

		my $userNode = $doc->findnodes('/bacheca/persona[user/text()="'.$userUsername.'" and password/text()="'.$userPassword.'"]/listaAnnunci')->get_node(1);

		#controlla se la ricerca è andata a buon fine
		if(defined($userNode))
		{
			my $data = strftime "%F", gmtime;

			my $insertion='<annuncio id="'.$highest.'">
								<titolo>'.$titleInsertion.'</titolo>
								<oggetto>'.$objectInsertion.'</oggetto>
								<descrizione>'.$descriptionInsertion.'</descrizione>
								<tipologia>"'.$TipoInsertion.'"</tipologia>
								<data>'.$data.'</data>
								<listaDisponibili>
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

			print $cgi->redirect( 'showInsertions.cgi' );

		}
		else
		{
			print $cgi->redirect( 'addInsertions.cgi?msgError=Errore nell\'inserimento dell\'inserzione.' );
		}
	}
	else
	{
		print $cgi->redirect($url);
	}
}
else
{
	print $cgi->redirect( 'login.cgi' );
}
