#!/usr/bin/perl -w

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use XML::LibXML;
use warnings;

require 'functions/session_function.cgi';


my $s = getSession();

if(! defined $s)
{
	print "Content-type: text/html\n\n";
        print "Prova sessione vuota";
}
else
{
        #my $username = getSessionName($s); 
        #my $id = $s->id;
        #my $name= getName($s);
		#destroySession($s);
	    print "Content-type: text/html\n\n";
        print $s->param('username');
       #print "Prova sessione trovata <br/> Username: $username <br/> ID: $id <br/>";
#        print "Prova sessione trovata <br/> Username: $username <br/> ID: $id <br/><br/>Ottenuto da Function<br/> Nome: $name <br/>";
}
