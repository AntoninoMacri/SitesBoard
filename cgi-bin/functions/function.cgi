#!/usr/bin/perl
use CGI;
use CGI::Session;
use XML::XPath;

use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use File::Basename;

use CGI::Carp qw(fatalsToBrowser);

my $file = '../data/progetto.xml';  
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