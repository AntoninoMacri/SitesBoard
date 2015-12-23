#!/bin/bash
scp  -P 30022   -r  cgi-bin/* drigoni@localhost:tecweb/cgi-bin/
scp  -P 30022   -r  public_html/* drigoni@localhost:tecweb/public_html/
scp  -P 30022   -r  data/* drigoni@localhost:tecweb/data/
