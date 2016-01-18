#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI;

require 'functions/session_function.cgi';

print "Content-type: text/html\n\n";

my $s = getSession();


if($s == undef)
{
        createSession('Davide','R','Ered','emailll','Pass');
        print "Sessione creata";
}
else
{
		print getSessionName($s);
        print "sessione trovata";
}


