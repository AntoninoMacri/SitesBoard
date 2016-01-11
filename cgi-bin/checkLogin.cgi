#!/usr/bin/perl

use CGI;
use CGI::Session;
use XML::XPath;

use CGI::Carp qw(fatalsToBrowser);

$page = new CGI;
$username = $page->param('login_user');
$password = $page->param('login_password');

my $xp = XML::XPath->new(filename => '../data/progetto.xml');
$xpath_exp='/bacheca/persona[user/text()="'.$username.'" and password/text()="'.$password.'"]';

my $nodeset = $xp->find($xpath_exp);

if ($nodeset->size eq 1) {
	$session = new CGI::Session();
	$session->expire('20m');
	$session->param('username', $username);
	print $session->header(-location=>"profile.cgi");
}
else {
	print $page->header(-location=>"login.cgi");
}
