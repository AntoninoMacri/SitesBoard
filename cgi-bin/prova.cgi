#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI;

require 'functions/session_function.cgi';


my $s = getSession();

if(! defined $s)
{
        my $p = createSession('Davide','R','Ered','emailll','Pass');
        my $id = $p->id;
        my $name = getSessionName($p);

		print "Content-type: text/html\n\n";
        print "Prova sessione creata -> <br/> Nome: $name <br/> ID: $id ";

}
else
{
        my $name = getSessionName($s); 
        my $id = $s->id;
		destroySession($s);
		print "Content-type: text/html\n\n";
        print "Prova sessione trovata: <br/> Nome: $name <br/> ID: $id <br/>";
        
}






