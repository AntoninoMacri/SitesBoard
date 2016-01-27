#!/bin/bash
scp  -P 30022   -r -p  cgi-bin/* amacri@localhost:tecweb/cgi-bin/
scp  -P 30022   -r -p  public_html/* amacri@localhost:tecweb/public_html/
scp  -P 30022   -r -p data/* amacri@localhost:tecweb/data/
