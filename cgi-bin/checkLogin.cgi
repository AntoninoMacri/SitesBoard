#!/usr/bin/perl -w

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use XML::LibXML;
use warnings;
require 'functions/session_function.cgi';

$username = "";	# Per il messaggio con user vuoto
$password = "";	# Per il messaggio con password vuota


my $s = getSession();

$page = new CGI;


if(! defined $s)
{
	$username = $page->param('login_user');
	$password = $page->param('login_password');
	if($username!="" || $password!=""){
		my $sessione = createSession($username,$password);
		print $sessione->header(-location=>"profile.cgi");
	}
	$url = "login.cgi";
	print "Location: $url\n\n";
}
else
{
	$url = "login.cgi";
	my $id = $s->id;
	print "Content-type: text/html\n\n";
	print $id;
	#print "Location: $url\n\n";
}