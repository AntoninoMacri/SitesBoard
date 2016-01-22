#!/usr/bin/perl  -w
require 'functions/session_function.cgi';
#my $session=getSession();
#destroySession($session);
destroySession();
print "Location: login.cgi\n\n";

print<<EOF;

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="refresh" content="0,URL=cgi-bin/login.cgi">
	</head>	
	<body>
	</body>
</html>
	
EOF
exit;