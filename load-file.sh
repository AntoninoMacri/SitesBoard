#!/bin/bash
scp  -P 30022   -r -p  cgi-bin/* drigoni@localhost:tecweb/cgi-bin/
scp  -P 30022   -r -p  public_html/* drigoni@localhost:tecweb/public_html/
scp  -P 30022   -r -p data/* drigoni@localhost:tecweb/data/

