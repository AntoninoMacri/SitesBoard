#!/usr/bin/perl

require "functions/session_function.cgi";

use CGI;
use CGI::Session;
use XML::XPath;

use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use File::Basename;

use CGI::Carp qw(fatalsToBrowser);

$page = new CGI;
$username = $page->param('login_user');
$password = $page->param('login_password');


my $file = '../data/progetto.xml';  
my $parser = XML::LibXML->new();
my $doc= $parser->parse_file($file);

my $nome=$doc->findnodes('/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]/nome');
my $cognome=$doc->findnodes('/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]/cognome');
my $username=$doc->findnodes('/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]/user');
my $email=$doc->findnodes('/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]/mail');
my $password=$doc->findnodes('/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]/password');


my $xp = XML::XPath->new(filename => '../data/progetto.xml');
$xpath_exp='/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]';

my $nodeset = $xp->find($xpath_exp);

if ($nodeset->size eq 1) {
	$session = new CGI::Session();
	#$session->expire('20m');
	#$session->param('username', $username);	
	#$session->param('email',$email);
	#$session->param('password', $password);
	
	createSession($nome,$cognome,$username, $email, $password);

	#print "Content-type: text/html\n\n";
	#print $session->param('username');
	#print "<br />";
	#print $session->param('password');
	#print "<br />";
	#print $session->param('email');

	print $session->header(-location=>"profile.cgi");
}
else {
	print $page->header(-location=>"login.cgi");
}
