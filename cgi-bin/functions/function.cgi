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
	
	my $username=$doc->findnodes('/bacheca/persona[@id="'.$id_persona.'"]/user');
	my $query=$doc->findnodes('/bacheca/persona[@id="'.$id_persona.'"]/listaAnnunci/annuncio[@id="'.$ad.'"]')->get_node(1) or die "Annuncio non trovato";
	my $titolo=$query->findnodes('titolo/text()');
	my $oggetto=$query->findnodes('oggetto/text()');
	my $descrizione=$query->findnodes('descrizione/text()')->to_literal;
	my $tipologia=$query->findnodes('tipologia/text()');
	my $data=$query->findnodes('data/text()');

	my @var = ($username,$titolo,$oggetto,$descrizione,$tipologia,$data);
	return @var;
}

sub getBoard(){
	my @board;

	my $persona=$doc->findnodes('/bacheca/persona/@id'); #ottengo tutti gli id di tutte le persone
	for (my $y=1; $y <= $persona->size; $y++) {
    	my $id_persona=$persona->get_node($y); #ottengo il nodo di una sola persona

		my $id_annuncio=$doc->findnodes('/bacheca/persona[@id="'.$id_persona->to_literal.'"]/listaAnnunci/annuncio/@id'); #ottengo tutti gli id di tutti gli annunci
		my $query=$doc->findnodes('/bacheca/persona[@id="'.$id_persona->to_literal.'"]/listaAnnunci/annuncio');
		
		my $username=$doc->findnodes('/bacheca/persona[@id="'.$id_persona->to_literal.'"]/user/text()');
		
		for (my $x=1; $x <= $id_annuncio->size; $x++) {
			my $annuncio=$query->get_node($x);
			my $titolo=$annuncio->findnodes('titolo/text()');
			my $oggetto=$annuncio->findnodes('oggetto/text()');
			my $descrizione=$annuncio->findnodes('descrizione/text()');
			my $tipologia=$annuncio->findnodes('tipologia/text()')->to_literal;
			my $data=$annuncio->findnodes('data/text()');
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
		if($type ne $tipo){ splice (@board, $i, 1); $i--;} 
	}
	return @board;
}


sub isMin()
{
	my $data1= $_[0];
	my $data2= $_[1];

	my $true='1';
	my $false='0';

	my $anno1=substr($data1, 0, 4);
	my $anno2=substr($data2, 0, 4);
	if($anno1<$anno2){return $true;}
	if($anno1>$anno2){return $false;}
	
	my $mese1=substr($data1, 5, 2);
	my $mese2=substr($data2, 5, 2);
	if($mese1<$mese2){return $true;}
	if($mese1>$mese2){return $false;}


	my $giorno1=substr($data1, 8, 2);
	my $giorno2=substr($data2, 8, 2);
	if($giorno1<$giorno2){return $true;}
	if($giorno1>$giorno2){return $false;}
	
	if($giorno1==$giorno2){return $false;}
}


sub getPersonalAd()
{
	my $sessionUsername = $_[0];

	my @board;

	my $query=$doc->findnodes('/bacheca/persona[user/text()="'.$sessionUsername.'"]/listaAnnunci/annuncio');
	for (my $x=1; $x <= $query->size; $x++) {
		my $annuncio=$query->get_node($x);
		my $titolo=$annuncio->findnodes('titolo/text()')->to_literal;
		my $oggetto=$annuncio->findnodes('oggetto/text()')->to_literal;
		my $tipologia=$annuncio->findnodes('tipologia/text()')->to_literal;
		my $data=$annuncio->findnodes('data/text()')->to_literal;
		my $idPersona=$doc->findnodes('/bacheca/persona[user/text()="'.$sessionUsername.'"]/@id')->to_literal;
		my $idAnnuncio=$annuncio->findnodes('@id')->to_literal;
		my @var = ($sessionUsername,$titolo,$oggetto,$tipologia,$data,$idPersona,$idAnnuncio); #array contenente un annuncio
		push @board, \@var;
	}
	return @board;
}


sub getDisponibili()

{
	my $sessionUsername = $_[0];
	my $id_annuncio=$_[1];

	my @board;

	my $query=$doc->findnodes('/bacheca/persona[user/text()="'.$sessionUsername.'"]/listaAnnunci/annuncio[@id="'.$id_annuncio.'"]/listaDisponibili')->get_node(1) or die "listaAnnunci non trovata";
	my $idp=$query->findnodes('idProgrammatore');

	for (my $x=1; $x <= $idp->size; $x++) {
		my $id=$idp->get_node($x)->to_literal;

		my $nome=$doc->findnodes('/bacheca/persona[@id="'.$id.'"]/nome')->to_literal;
		my $cognome=$doc->findnodes('/bacheca/persona[@id="'.$id.'"]/cognome')->to_literal;
		my $user=$doc->findnodes('/bacheca/persona[@id="'.$id.'"]/user')->to_literal;
		my @var = ($user,$id,$nome,$cognome); #array contenente un programmatore con i dati personali
		push @board, \@var;
	}
	return @board;
}

sub getUtente{
	my $username = $_[0];

	my @utente;

	my $query=$doc->findnodes('/bacheca/persona[user/text()="'.$username.'"]')->get_node(1) or die "Utente non trovato";
	
	my $nome=$query->findnodes('nome')->to_literal;
	my $cognome=$query->findnodes('cognome')->to_literal;
	my $dataNascita=$query->findnodes('dataNascita')->to_literal;
	my $email=$query->findnodes('mail')->to_literal;
	my $biografia=$query->findnodes('biografia')->to_literal;

	push @utente, $nome;
	push @utente, $cognome;
	push @utente, $dataNascita;
	push @utente, $email;
	push @utente, $biografia;


	return @utente;
}

sub getAcceptedAd(){
	my $sessionUsername = $_[0];# dallo username di una persona bisogna risalire al suo id

	my $query=$doc->findnodes('/bacheca/persona[user/text()="'.$sessionUsername.'"]/@id');

	# bisogna interrogare ogni annuncio nel database e vedere se in listaDisponibili compare
	# l'id trovato sopra

	# da qui bisogna prendere quell'annuncio e metterlo in un array come in getPersonalAdd,
	# solo che sono annunci di un altro utente
}












