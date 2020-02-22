#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
    config.py
    
    Andy Freeland and Dan Levy
    5 June 2010
    
    Contains the configuration information for the twenty questions game and
    the web interface.
'''

import web
web.config.debug = False
db = web.database(dbn='sqlite', db='data/bafe_20q.db')
DISPLAY_CANDIDATES = True
