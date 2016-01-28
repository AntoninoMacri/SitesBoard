#!/usr/bin/perl  -w
require 'functions/session_function.cgi';

#chiama la funzione che distrugge la sessione corrente se esiste
destroySession();

#redirect alla home
print "Location: home.cgi\n\n";