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

sub getBio(){
	my $session = $_[0];
	return $doc->findnodes('/bacheca/persona[user/text()="'.$session->param('username').'" and password/text()="'.$session->param('password').'"]/biografia')->to_literal;
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
			my $id_annuncio=$annuncio->findnodes('@id')->to_literal;
			my $titolo=$annuncio->findnodes('titolo/text()');
			my $oggetto=$annuncio->findnodes('oggetto/text()');
			my $descrizione=$annuncio->findnodes('descrizione/text()');
			my $tipologia=$annuncio->findnodes('tipologia/text()')->to_literal;
			my $data=$annuncio->findnodes('data/text()');
			my @var = ($username,$titolo,$oggetto,$descrizione,$tipologia,$data,$id_annuncio,$id_persona->to_literal); #array contenente un annuncio
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

	my $query=$doc->findnodes('/bacheca/persona[user/text()="'.$sessionUsername.'"]/listaAnnunci/annuncio[@id="'.$id_annuncio.'"]/listaDisponibili/idProgrammatore');

	for (my $x=1; $x <= $query->size; $x++) {
		my $id=$query->get_node($x)->to_literal;
		my $user=$doc->findnodes('/bacheca/persona[@id="'.$id.'"]/user')->to_literal;
		push @board, $user;
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
	my $sessionUsername = $_[0];
	my $idUtente=$doc->findnodes('/bacheca/persona[user/text()="'.$sessionUsername.'"]/@id')->to_literal;

	my @insertions;
	
	my $query=$doc->findnodes('/bacheca/persona[listaAnnunci/annuncio/listaDisponibili/idProgrammatore/text()="'.$idUtente.'"]');

	for(my $z=1; $z <= $query->size; $z++){
		#per ogni persona mi prendo id e user
		my $nodePers=$query->get_node($z);
		my $autore=$nodePers->findnodes('user/text()')->to_literal;
		my $id_autore=$nodePers->findnodes('@id')->to_literal;

		#mi prendo gli annunci
		my $nodeAnnunci=$nodePers->findnodes('listaAnnunci/annuncio[listaDisponibili/idProgrammatore/text()="'.$idUtente.'"]');

		for(my $s=1; $s <= $nodeAnnunci->size; $s++){
			#per ogni annuncio mi prendo i dati
			my $nodeAnn=$nodeAnnunci->get_node($s);
			my $titolo=$nodeAnn->findnodes('titolo/text()')->to_literal;
			my $oggetto=$nodeAnn->findnodes('oggetto/text()')->to_literal;
			my $tipologia=$nodeAnn->findnodes('tipologia/text()')->to_literal;
			my $data=$nodeAnn->findnodes('data/text()')->to_literal;
			my $id_ann=$nodeAnn->findnodes('@id')->to_literal;

			my @var = ($titolo,$oggetto,$tipologia,$data,$autore,$id_ann,$id_autore); #array contenente un annuncio
			push @insertions, \@var;
		}
	}
	return @insertions;
}

sub isAccepted{
	my $user_Username = $_[0];
	my $id_autore = $_[1];
	my $id_annuncio = $_[2];

	my $idUtente=$doc->findnodes('/bacheca/persona[user/text()="'.$user_Username.'"]/@id')->get_node(1)->to_literal;

	my $query=$doc->findnodes('/bacheca/persona[@id="'.$id_autore.'"]/listaAnnunci/annuncio[@id="'.$id_annuncio.'"]/listaDisponibili/idProgrammatore[text()="'.$idUtente.'"]/text()');
	if(defined($query) && $query->size > 0)
	{
		return "true";
	}
	return "false";
}




sub getMyBoard()
{
	my $user_Username = $_[0];
	print "<br />username: ";
	print $user_Username;
	print "<br />";

	my $idUtente=$doc->findnodes('/bacheca/persona[user/text()="'.$user_Username.'"]/@id')->get_node(1) or die "utente non trovato"; #ottengo l'id dell'utente loggato

	my @board;

	my $persona=$doc->findnodes('/bacheca/persona/@id'); #ottengo tutti gli id di tutte le persone
	for (my $y=1; $y <= $persona->size; $y++) {
    	my $id_persona=$persona->get_node($y); #ottengo il nodo di una sola persona


		my $query=$doc->findnodes('/bacheca/persona[@id!="'.$idUtente->to_literal.'" and @id="'.$id_persona->to_literal.'"]/listaAnnunci/annuncio');


		my $username=$doc->findnodes('/bacheca/persona[@id="'.$id_persona->to_literal.'"]/user/text()');
		
		for(my $x=1; $x <= $query->size; $x++){
			my $annuncio=$query->get_node($x);
			my $ann_presente=$annuncio->findnodes('listaDisponibili/idProgrammatore[text()="'.$idUtente->to_literal.'"]');
			if($ann_presente->size==0)
				{
					my $annuncio=$query->get_node($x);
					my $id_annuncio=$annuncio->findnodes('@id')->to_literal;
					my $titolo=$annuncio->findnodes('titolo/text()');
					my $oggetto=$annuncio->findnodes('oggetto/text()');
					my $descrizione=$annuncio->findnodes('descrizione/text()');
					my $tipologia=$annuncio->findnodes('tipologia/text()')->to_literal;
					my $data=$annuncio->findnodes('data/text()');
					my @var = ($username,$titolo,$oggetto,$descrizione,$tipologia,$data,$id_annuncio,$id_persona->to_literal); #array contenente un annuncio
					push @board, \@var;
				}
		}
	}
    #return InsertionSort(\@board);
	return @board;
}


#
#Funzioni di richiamo delle funzioni di controllo dell'input
sub profileChangeControl(){
	my $url="profileChange.cgi?";
	my $ris=checkName($_[0]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkSurname($_[1]);
	if($ris ne 1){ return $url.$ris; }
	my $ris=checkData($_[2],$_[3],$_[4]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkEmail($_[5]);
	if($ris ne 1){ return $url.$ris; }
	return 1;
}

sub addInsertionControl(){
	my $url="addInsertion.cgi?";
	my $ris=checkTitolo($_[0]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkOggetto($_[1]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkDescrizione($_[2]);
	if($ris ne 1){ return $url.$ris; }
	return 1;	
}

sub registrationControl(){
	my $url="registration.cgi?";
	my $ris=checkName($_[0]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkSurname($_[1]);
	if($ris ne 1){ return $url.$ris; }
	my $ris=checkData($_[2],$_[3],$_[4]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkUser($_[5]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkEmail($_[6]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkPassword($_[7]);		
	if($ris ne 1){ return $url.$ris; }
	$ris=checkConfirmPassword($_[7],$_[8]);
	if($ris ne 1){ return $url.$ris; }
	return 1;	
}



sub recoveryControl(){
	my $url="pass_recovery.cgi?";
	my $ris=checkName($_[0]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkSurname($_[1]);
	if($ris ne 1){ return $url.$ris; }
	my $ris=checkData($_[2],$_[3],$_[4]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkUser($_[5]);
	if($ris ne 1){ return $url.$ris; }
	my $ris=checkUser($_[6]);
	if($ris ne 1){ return $url.$ris; }
	$ris=checkPassword($_[7]);		
	if($ris ne 1){ return $url.$ris; }
	$ris=checkConfirmPassword($_[7],$_[8]);
	if($ris ne 1){ return $url.$ris; }
	return 1;	
}




#Funzioni di controllo della validità dell'input
sub checkDescrizione()
{
	my $par = $_[0];
	my $url="msgError=*Campo Descrizione vuoto";
	
	if(!defined($par) || $par eq ""){
		return $url;
	}
	return 1;
}


sub checkOggetto()
{
	my $par = $_[0];
	my $url="msgError=*Campo oggetto vuoto";
	
	if(!defined($par) || $par eq ""){
		return $url;
	}
	return 1;
}


sub checkTitolo()
{
	my $par = $_[0];
	my $url="msgError=*Campo Titolo vuoto";
	
	if(!defined($par) || $par eq ""){
		return $url;
	}
	return 1;
}

sub checkSurname()
{
	my $par = $_[0];
	my $url="msgError=*Campo Cognome vuoto";
	
	if(!defined($par) || $par eq ""){
		return $url;
	}
	return 1;
}


sub checkName()
{
	my $par = $_[0];
	my $url="msgError=*Campo Nome vuoto";
	
	if(!defined($par) || $par eq ""){
		return $url;
	}
	return 1;
}


sub checkPassword()
{
	my $par = $_[0];
	my $url="msgError=*Campo password vuoto";
	
	if(!defined($par) || $par eq ""){
		return $url;
	}

	my $boolPassLenght=length $password<7;
	$url = "Il campo Password deve contenere almeno 8 caratteri"; 
	if(!$boolPassLenght){ 
		return $url;
	}
	return 1;
}


sub checkConfirmPassword()
{
	my $par = $_[0];
	my $conferma=$_[1];
	my $url="msgError=*Campo ripeti password vuoto";
	
	if(!defined($conferma) || $conferma eq ""){
		return $url;
	}

	my $boolPassLenght=length $password<7;
	$url = "Il campo ripeti la Password deve contenere almeno 8 caratteri"; 
	if(!$boolPassLenght){ 
		return $url;
	}

	$url = "campo Ripeti la Password deve coincidere con il campo Password"; 
	if($par ne $conferma){
		return $url;
	}
	return 1;
}

sub checkUser()
{
	my $par = $_[0];
	my $url="msgError=*Campo Username vuoto";
	
	if(!defined($par) || $par eq ""){
		return $url;
	}
	return 1;
}


sub checkEmail()
{
	my $par = $_[0];
	#chomp($par);
	my $url="msgError=*Campo Email vuoto";
	if(!defined($par) || $par eq ""){
		return $url;
	}

	$url="msgError=*Email non valida";
	if($par=~ m/^([\w\-\+\.]+)@([\w\-\+\.]+)\.([\w\-\+\.]+)$/i ){
		return 1;
	}
	return $url;
}

sub checkData(){

	my $year = $_[0];
	my $month = $_[1];
	my $day = $_[2];

	my $url="msgError=*Campo Anno vuoto";
	if(!defined($year) || $year eq ""){
		return $url;
	}
    
    $url="msgError=*Il campo Anno deve contenere 4 cifre";
    if(!($year=~ m/^[0-9]{4}$/)){
        return $url;
    }

    $url="msgError=*L'anno di nascita deve essere successivo al 1900";
    if($year<1900){
        return $url;
    }

    my $bisestile=0;
    if($year%4==0){
        $bisestile=1;
    }

	$url="msgError=*msgError=*Campo Mese di Nascita vuoto";
	if(!defined($month) || $month eq ""){
		return $url;
	}

	$url="msgError=*msgError=*Il campo Mese deve contenere 1 o 2 cifre";
    if(!($month=~ m/^[0-9]{1,2}$/)){
        return $url;
    }

    $url="msgError=*Il campo Mese deve contenere un valore da 1 a 12";
    if($month>12 || $month<1){
        return $url;
    }

    $url="msgError=*Campo Giorno di Nascita vuoto";
	if(!defined($day) || $day eq ""){
		return $url;
	}

	$url="msgError=*Il campo Giorno deve contenere 1 o 2 cifre";
    if(!($day=~ m/^[0-9]{1,2}$/)){
        return $url;
    }
    
    $url="msgError=*Il campo Giorno deve contenere un valore da 1 a 31";
    if($day>31 || $day<1){
        return $url;
    }

    if($day>28 && $month==2){
        if($day==29)
        {
            if($bisestile==0)
                { 
                	$url="msgError=*Anno NON bisestile. Febbraio ha al massimo 28 giorni";
                    return $url;
                }
        }
        else
        { 
        	$url="msgError=*Febbraio ha al massimo 29 giorni";
            return $url;
		}
    }
    if($day==31 && ($month==11 || $month==4 || $month==6 || $month==9)){
    	$url="msgError=*30 giorni al massimo";
        return $url;
    }
    return 1;
}


#controllo che un input sia accettabile all'interno del database [NON contiene <,>,&]
#in caso siano presenti questi simboli allora ritorno una stringa che che li sostituisce con &amp; &gt; &lt;
sub inputControl(){ 
	my $par  = $_[0];

	my $amp="\&";
	my $amp_r="\&amp\;";
	$par =~ s/$amp/$amp_r/g;

	my $lt="\<";
	my $lt_r="\&lt\;";
	$par =~ s/$lt/$lt_r/g;


	my $gt="\>";
	my $gt_r="\&gt\;";
	$par =~ s/$gt/$gt_r/g;

	return $par;
}

sub extractType(){ #presa una variabile in input la ritorna senza carattere " ad inizio e fine stringa
	$par=$_[0];
	$par=substr $par,1,length $par; 
	$par=substr $par,0,-1; 

	return $par;
}