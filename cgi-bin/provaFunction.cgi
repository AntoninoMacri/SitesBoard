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
print "<br/>";
print $var[4];
print "<br/>";
print $var[5];

print "<br/>checkLog(): ";	
print checkLog($username,$password);

print "<br/>".length $var[0];
$t=length $var[0]>7;
print "<br/>".$t."<br />";

print "<br /><br />";
print "getBoard(): <br />";
@board=getBoard();
print @{ $board[0] };
print "<br /><br />";

print "Lista annunci<br />";
print $board[0][0];
print "<br />";
print "TITOLO:   ".$board[0][1]."   OGGETTO:  ".$board[0][2];
print "<br /><br />";
print $board[1][0];
print "<br />";
print $board[1][1];

print "<br /><br />";
print $board[2][0];
print "<br />";
print $board[2][1];
print "<br /><br />";
print $board[3][0];
print "<br />";
print $board[3][1];