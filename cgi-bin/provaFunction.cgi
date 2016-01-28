#!/usr/bin/perl -w

use CGI::Carp qw(fatalsToBrowser);

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
print "numero elementi riga : ".@board;
print "<br/>numero elementi colonna : ".@{ $board[0] };
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

my $data1='2015-10-07';
my $data2='2015-10-17';
print "<br />isMin(): ";
print isMin($data1,$data2);
print "<br />";
$giorno1=substr($data1, 8, 2);
$giorno2=substr($data2, 8, 2);
print $giorno1."<br />";
print $giorno2."<br />";
$b=$giorno1<$giorno2;
print $b;

#print "<br />";
#print $data1;
#print "<br />";
#$anno1=substr($data1, 0, 4);
#$anno2=substr($data2, 0, 4);
#print "<br />";
#$mese1=substr($data1, 5, 2);
#print "<br />";
#$giorno1=substr($data1, 8, 2);
#print "<br />";
#print $anno1;
#print "<br />";
#print $mese1;
#print "<br />";
#print $giorno1;
#
#print "<br />";
#print $anno1<$anno2;


print "<br /> InsertionSort: <br />";
@order=InsertionSort(\@board);
print "<br />";
print "<br />Numero elementi in \@order: ";
print scalar @order ;
print "<br />";
for (my $i=0; $i <scalar(@order); $i++) {
	#print @{ $order[i] };
	print $i.") ";
	print $order[$i][5];
	print "<br />";
}

print "<br />";
print "<br />";
print "test se viene passata correttamente una matrice(\@order)";
print "<br />";
print @{@order[0]};
print "<br />";
print @{@order[1]};
print "<br />";
print @{@order[2]};
print "<br />";
print @{@order[3]};
print "<br />";

# print @{ $board[0] };


print "<br />";
print "<br />";
print "<br />";
print "<br />";
for (my $i=0; $i <scalar(@order); $i++) {
	print @{ $board[$i] };
	print "<br />";
}



print "<br />";
print "<br />";
print "<br />";
print "<br />";
print "<br />Social: <br/>";

$tipo='Social';
@social=getBoardTipologia($tipo);
for (my $i=0; $i <scalar(@social); $i++) {
	print @{ $social[$i] };
	print "<br />";
}
