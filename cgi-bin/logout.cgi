#!/usr/bin/perl
require "functions/session_function.cgi";
destroySession();
print "Location: home.cgi\n\n";

print<<EOF;

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="refresh" content="0,URL=cgi-bin/home.cgi">
	</head>	
	<body>
	</body>
</html>
	
EOF
exit;