#!/usr/bin/perl -w


require 'functions/function.cgi';
require 'functions/session_function.cgi';

#my $sessione = createSession('Torroncino93','12345678');

my $session=getSession();

my $id_persona=1;
my $ad=1;


my $username= 'Torroncino93';
my $password= '12345678';

print "Content-type: text/html\n\n";
print getName($sessione);
print "<br />";
print getSurname($sessione);
print "<br />";
print getEmail($sessione);
print "<br />";
print getDate($sessione);
print "<br/><br/>";

print getAd($id_persona,$ad);
@var=getAd($id_persona,$ad);
print "<br/><br/><br/>";
print $var[0];

print "<br/>checkLog(): ";	
print checkLog($username,$password);

print "<br/>".length $var[0];
$t=length $var[0]>7;
print "<br/>".$t;

#my $s = getSession();
#
#if(! defined $s)
#{
#	print "Content-type: text/html\n\n";
#        print "Prova sessione vuota";
#}
#else
#{
#        #my $username = getSessionName($s); 
#        #my $id = $s->id;
#        #my $name= getName($s);
#		#destroySession($s);
#	    print "Content-type: text/html\n\n";
#        print $s->param('username');
#       #print "Prova sessione trovata <br/> Username: $username <br/> ID: $id <br/>";
##        print "Prova sessione trovata <br/> Username: $username <br/> ID: $id <br/><br/>Ottenuto da Function<br/> Nome: $name <br/>";
#}
#