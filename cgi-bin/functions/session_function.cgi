#!/usr/bin/perl -w

use CGI;
use CGI::Session;


#funzioni per le sessioni
sub createSession(){
    
	my $cgi = new CGI;
    my $dir = '../data/tmpSession';

    #Se non esiste la cartella per mantenere le sessioni quest'ultima viene creata
    if ( !( -d $dir ) ) {
		mkdir $dir;
    }

    my $session = new CGI::Session( 'driver:File', undef, { Directory => $dir } ); #Crea la sessione
    my $cookie = $cgi->cookie( 'CGISESSID' => $session->id );


	my $name=$_[0];
	my $surname=$_[1];
	my $username=$_[2];
	my $email=$_[3];
	my $password=$_[4];
	

	$session->param('name',$name);
	$session->param('surname',$surname);
	$session->param('username',$username);
	$session->param('email',$email);
	$session->param('password',$password);


	#print "Content-type: text/html\n\n";
	#print $session->param('username');
	#print getSessionName($session);

	#print "Content-type: text/html\n\n";	
	#print $session->param('name');
	#print "<br />";
	#print $session->param('surname');
	#print "<br />";
	#print $session->param('username');
	#print "<br />";
	#print $session->param('password');
	#print "<br />";
	#print $session->param('email');
	
	#return $session;

	$cookie = $cgi->cookie(CGISESSID => $session->id);
	$cgi->header( -cookie=>$cookie );

	return $session;
}

sub getSession(){

        my $cgi = new CGI;
        my $sid = $cgi->cookie( 'CGISESSID' ) || undef;
        if($sid == undef){
                return undef;
        }
        else{
                my $session =  new CGI::Session(undef, $sid, { Directory => '../data/tmpSession' } ); #Crea la sessione
                return $session;
        }


}

sub getSessionName(){
	my $session = $_[0];	
	return $session->param('name');
}

sub getSessionSurname(){
	my $session = $_[0];
	return $session->param('surname');
}

sub getSessionYear(){
	my $session = $_[0];
	return $session->param('year');
}

sub getSessionMonth(){
	my $session = $_[0];
	return $session->param('month');
}

sub getSessionDay(){
	my $session = $_[0];
	return $session->param('day');
}

sub getSessionUsername(){
	my $session = $_[0];
	return $session->param('username');
}

sub getSessionEmail(){
	my $session = $_[0];
	return $session->param('email');
}

sub getSessionPassword(){
	my $session = $_[0];
	return $session->param('password');
}

sub destroySession(){
	$session=CGI::Session->load() or die $!;
	$SID = $session->id;
	$session->close();
	$session->delete();
	$session->flush();
}
#necessario per far tornare true... altrimenti perl da errore
1;

