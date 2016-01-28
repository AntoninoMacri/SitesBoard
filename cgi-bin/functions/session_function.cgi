#!/usr/bin/perl -w
use CGI;
use CGI::Session;
use XML::XPath;

use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use File::Basename;
use CGI qw(:standard Vars);
use warnings;


#funzioni per le sessioni
sub createSession(){
	my $username=$_[0];
	my $password=$_[1];

	my $session = new CGI::Session();
	$session->expire('20m');
	$session->param('username',$username);
	$session->param('password',$password);

	return $session;
}

sub getSession() {
        $sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
        if ($sessione->is_expired || $sessione->is_empty) { # Se manca la sessione torno in home
                #print redirect(-url=>'login.cgi');
                return undef;
        } else {
                # print $sessione->param('username');
                return $sessione;
        }
}

sub getSessionUsername(){
	my $session = $_[0];
	return $session->param('username');
}

sub getSessionPassword(){
	my $session = $_[0];
	return $session->param('password');
}

sub destroySession(){
	my $session=getSession();
	if(defined($session))
	{
		$session->close();
		$session->delete();
		$session->flush();
	}
}
#necessario per far tornare true... altrimenti perl da errore
1;

