#!/bin/bash

scp  -P 30022   -r -p  cgi-bin/* gzecchin@localhost:tecweb/cgi-bin/
scp  -P 30022   -r -p  public_html/* gzecchin@localhost:tecweb/public_html/
scp  -P 30022   -r -p data/* gzecchin@localhost:tecweb/data/

