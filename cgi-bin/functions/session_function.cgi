#!/usr/bin/perl

use CGI;
use CGI::Session;

#funzioni per le sessioni
sub createSession(){
	my $session = new CGI::Session();
	$session->expire('20m');
	
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
}

sub getSession(){
	my $session = CGI::Session->load() or die $!;
	if($session->is_expired || $session->is_empty){
		return undef;
	}
	else{
		#print "entrato nell' if";
		#my $name = $session->param('name');
		#print "<br />";
		#print $name;
		return $session;
	}
}

#sub getSessionName(){
#	my $session = $_[0];	
#	return $session->param('name');
#}
#
#sub getSessionSurname(){
#	my $session = $_[0];
#	return $session->param('surname');
#}
#
#sub getSessionUsername(){
#	my $session = $_[0];
#	return $session->param('username');
#}
#
#sub getSessionEmail(){
#	my $session = $_[0];
#	return $session->param('email');
#}

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

