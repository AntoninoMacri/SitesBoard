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
	$username = $page->param('login_user');
	$password = $page->param('login_password');
	$temp=checkLog($username,$password);
	my $xp = XML::XPath->new(filename => '../data/database.xml');
	$xpath_exp='/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]';

	my $nodeset = $xp->find($xpath_exp);

	$boolPassLenght=length $password>1;
	if ($nodeset->size eq 1){
		if(($username!="" || $password!="" )&& $boolPassLenght){
			my $sessione = createSession($username,$password);
			print $sessione->header(-location=>"profile.cgi");
		}
	}
	$url = "login.cgi?msgError=*Username e Password errati";
	print "Location: $url\n\n";
}
else
{
	$url = "home.cgi";
	print "Location: $url\n\n";
}