#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys, random, json, time, urllib2, urllib
import httplib, threading, copy
import traceback
import datetime as dt
from flask import Flask, request, send_file
from time import clock
from math import *
reload(sys)
sys.setdefaultencoding('utf8')
app = Flask(__name__)

def initialize():
    pass

@app.route("/interface", methods=["GET", "POST"])
def get_prop_word_list():
    t_s = time.time()
    output = ""
    try:
        items = {}
        items.update(request.args)
        items.update(request.form)
        trade = items.get('trade', [''])[0]
        prop = items.get('prop', [''])[0]

        output = work(trade)
    except Exception, e:
        sys.stderr.write(traceback.format_exc())
    t_e = time.time()
    sys.stderr.write('process time: %f ms\n' % ((t_e-t_s)*1000))
    return json.dumps(output)

if __name__ == '__main__':
    initialize()
    p = 8299 if (len(sys.argv) <= 1) else int(sys.argv[1])
    app.run(host='0.0.0.0', port=p, threaded=True)

