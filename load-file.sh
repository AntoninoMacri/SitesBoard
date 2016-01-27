#!/bin/bash

scp  -P 30022   -r -p  cgi-bin/* ffasolat@localhost:tecweb/cgi-bin/
scp  -P 30022   -r -p  public_html/* ffasolat@localhost:tecweb/public_html/
scp  -P 30022   -r -p data/* ffasolat@localhost:tecweb/data/

