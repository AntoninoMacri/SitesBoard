#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI;


print "Content-type: text/html\n\n";


print <<FINE;
<!--file di redirect alla home-->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="refresh" content="0,URL=cgi-bin/home.cgi">
	</head>	
	<body>
	</body>
</html>


FINE
exit;