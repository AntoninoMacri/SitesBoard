#!/usr/bin/perl -w

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use XML::LibXML;
use warnings;

use XML::XPath;
use File::Basename;


require 'functions/function.cgi';
require 'functions/session_function.cgi';

$username = "";	# Per il messaggio con user vuoto
$password = "";	# Per il messaggio con password vuota


my $s = getSession();

$page = new CGI;

if(! defined $s)
{
	my $username = $page->param('login_user');
	my $password = $page->param('login_password');


	#pulizia e correzione input
	$username = inputControl($username);
	$password = inputControl($password);

	my $xp = XML::XPath->new(filename => '../data/database.xml');
	my $xpath_exp='/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]';

	my $nodeset = $xp->find($xpath_exp);
	my $boolPassLenght=length $password>7;
	if($nodeset->size ne 1){
		my $url="login.cgi?msgError=*Username e Password errati";
		if(!$boolPassLenght){ $url = "login.cgi?msgError=*Il campo Password deve contenere almeno 8 caratteri"; }
		if($password eq "") { $url = "login.cgi?msgError=*Campo Password vuoto"; }
		if($username eq "") { $url = "login.cgi?msgError=*Campo Username vuoto"; }
	print "Location: $url\n\n";
	}
	my $sessione = createSession($username,$password);
	print $sessione->header(-location=>"profile.cgi");
}
else
{
	$url = "home.cgi";
	print "Location: $url\n\n";
}