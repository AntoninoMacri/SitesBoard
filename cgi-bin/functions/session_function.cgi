#!/usr/bin/perl

use CGI::Session;

#funzioni per le sessioni
sub createSession(){
	my $session = new CGI::Session();
	my ($name,$surname,$year,$month,$day,$username,$email,$password) = split(@_);

	$session->param('name',$name);
	$session->param('surname',$surname);
	$session->param('year',$year);
	$session->param('month',$month);
	$session->param('day',$day);
	$session->param('username',$username);
	$session->param('email',$email);
	$session->param('password',$password);
}

sub getSession(){
	my $session = CGI::Session->load() or die $!;
	if($session->is_expired || $session->is_empty){
		return undef;
	}
	else{
		return $session;
	}
}

sub getSessionName(){
	my ($session) = shift(@_);	
	return $session->param('name');
}

sub getSessionSurname(){
	my ($session) = shift(@_);
	return $session->param('surname');
}

sub getSessionYear(){
	my ($session) = shift(@_);
	return $session->param('year');
}

sub getSessionMonth(){
	my ($session) = shift(@_);
	return $session->param('month');
}

sub getSessionDay(){
	my ($session) = shift(@_);
	return $session->param('day');
}

sub getSessionUsername(){
	my ($session) = shift(@_);
	return $session->param('username');
}

sub getSessionEmail(){
	my ($session) = shift(@_);
	return $session->param('email');
}

sub getSessionPassword(){
	my ($session) = shift(@_);
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

