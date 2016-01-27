#!/usr/bin/perl  -w
require 'functions/session_function.cgi';
#my $session=getSession();
#destroySession($session);
destroySession();
print "Location: login.cgi\n\n";