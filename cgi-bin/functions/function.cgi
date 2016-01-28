#!/usr/bin/perl
use CGI;
use CGI::Session;
use XML::XPath;

use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use File::Basename;


my $file = '../data/database.xml';  
my $parser = XML::LibXML->new();
my $doc= $parser->parse_file($file);


sub getName(){
	my $session = $_[0];
	return $doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]/nome')->to_literal;
}

sub getSurname(){
	my $session = $_[0];
	return my $cognome=$doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]/cognome')->to_literal;
}

sub getUsername(){
	my $session = $_[0];
	return my $username=$doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]/user')->to_literal;
}

sub getEmail(){
	my $session = $_[0];
	return my $email=$doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]/mail')->to_literal;

}

sub getDate(){
	my $session = $_[0];
	return $doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]/dataNascita')->to_literal;
}

sub checkLog(){ #controlla se l utente esiste nel database 
	my $username= $_[0];
	my $password= $_[1];
	return $doc->findnodes('/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]/user')->to_literal;
}

#parametro1 in ingresso prendo l'id di una persona da cui trovrerò il relativo annuncio
#parametro2 in ingresso prendo l'id di un annuncio, e restituisce il nodo dell'annuncio 
sub getAd(){  #ritorna un array{username,titolo,oggetto,descrizione,tipologia,data}
	my $id_persona= $_[0];
	my $ad= $_[1]; 
	
	$username=$doc->findnodes('/bacheca/persona[@id="'.$id_persona.'"]/user');
	$query=$doc->findnodes('/bacheca/persona[@id="'.$id_persona.'"]/listaAnnunci/annuncio[@id="'.$ad.'"]')->get_node(1) or die "Annuncio non trovato";
	$titolo=$query->findnodes('titolo/text()');
	$oggetto=$query->findnodes('oggetto/text()');
	$descrizione=$query->findnodes('descrizione/text()')->to_literal;
	$tipologia=$query->findnodes('tipologia/text()');
	$data=$query->findnodes('data/text()');

	@var = ($username,$titolo,$oggetto,$descrizione,$tipologia,$data);
	return @var;
}

sub getBoard(){
	my @board;

	$persona=$doc->findnodes('/bacheca/persona/@id'); #ottengo tutti gli id di tutte le persone
	for (my $y=1; $y <= $persona->size; $y++) {
    	$id_persona=$persona->get_node($y); #ottengo il nodo di una sola persona

		$id_annuncio=$doc->findnodes('/bacheca/persona[@id="'.$id_persona->to_literal.'"]/listaAnnunci/annuncio/@id'); #ottengo tutti gli id di tutti gli annunci
		$query=$doc->findnodes('/bacheca/persona[@id="'.$id_persona->to_literal.'"]/listaAnnunci/annuncio');
		
		$username=$doc->findnodes('/bacheca/persona[@id="'.$id_persona->to_literal.'"]/user/text()');
		
		for (my $x=1; $x <= $id_annuncio->size; $x++) {
			$annuncio=$query->get_node($x);
			$titolo=$annuncio->findnodes('titolo/text()');
			$oggetto=$annuncio->findnodes('oggetto/text()');
			$descrizione=$annuncio->findnodes('descrizione/text()');
			$tipologia=$annuncio->findnodes('tipologia/text()')->to_literal;
			$data=$annuncio->findnodes('data/text()');
			my @var = ($username,$titolo,$oggetto,$descrizione,$tipologia,$data); #array contenente un annuncio
			push @board, \@var;
		}
    }
    return InsertionSort(\@board);
}


sub InsertionSort() #passo un riferimento alla matrice
{
	my @board=@{$_[0]}; #deferenzio il riferimento alla matrice
	my $i;
	my $j;
	my @temp;
	for (my $i=1; $i <scalar(@board); $i++) {
		$j=$i;
		while ($j>0 && isMin($board[$j-1][5],$board[$j][5])){
			@temp=\@{@board[$j]};
			@board[$j]=\@{ @board[$j-1] };
			@board[$j-1]=@temp;
			$j--;
		}
	}
	return @board;
}

sub getBoardTipologia()
{
	my $tipo= $_[0];

	my @board=getBoard();
	for (my $i=0; $i <scalar(@board); $i++) {
		my $type=$board[$i][4];
		if($type ne $tipo){ splice (@board, $i, 1); } 
	}
	return @board;
}


sub isMin()
{
	my $data1= $_[0];
	my $data2= $_[1];

	$true='1';
	$false='0';

	$anno1=substr($data1, 0, 4);
	$anno2=substr($data2, 0, 4);
	if($anno1<$anno2){return $true;}
	if($anno1>$anno2){return $false;}
	
	$mese1=substr($data1, 5, 2);
	$mese2=substr($data2, 5, 2);
	if($mese1<$mese2){return $true;}
	if($mese1>$mese2){return $false;}


	$giorno1=substr($data1, 8, 2);
	$giorno2=substr($data2, 8, 2);
	if($giorno1<$giorno2){return $true;}
	if($giorno1>$giorno2){return $false;}
	
	if($giorno1==$giorno2){return $false;}
}