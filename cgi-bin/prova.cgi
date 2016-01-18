#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI;

require 'functions/session_function.cgi';

print "Content-type: text/html\n\n";

my $s = getSession();

if($s == undef)
{
        my $p = createSession('Davide','R','Ered','emailll','Pass');
        my $id = $p->id;
        my $name = getSessionName($p);
        print "Prova sessione creata -> <br/> Nome: $name <br/> ID: $id ";

}
else
{
        my $name = getSessionName($s); 
        my $id = $s->id;
        print "Prova sessione trovata: <br/> Nome: $name <br/> ID: $id <br/>";
        destroySession($s);
}






