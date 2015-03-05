#!/usr/bin/env python

# This file is part of saving-secure-a-lot
#
#  saving-secure-a-lot is free software: you can redistribute it and/or
#  modify it under the terms of the GNU Affero General Public License
#  as published by the Free Software Foundation, either version 3 of
#  the License, or (at your option) any later version.
#
#  saving-secure-a-lot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public
#  License along with saving-secure-a-lot If not, see
#  <http://www.gnu.org/licenses/>.
#
# (C) 2014- by Stefan Marsiske, <s@ctrlc.hu>

from flask import Flask, request, render_template, redirect, abort, make_response
from common import cfg
from urlparse import urlparse
import os, random, itertools, hmac, hashlib, string, sys
from snifer import Snifer

def rnd(size):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for i in range(size))

app = Flask(__name__)
app.secret_key = cfg.get('app', 'secret_key')

portmap = { 5001: "Default CA/cert",
            5002: "Default CA, similar cert",
            5003: "Similar CA, similar cert",
            5004: "Self-signed cert",
            5005: "Faked cert and CA",
            5006: "A valid but untrusted CA, real cert",
            }
mapports = { 'def': 5001,
             'sim': 5002,
             'res': 5003,
             'oth': 5004,
             'mtm': 5005,
             'cac': 5006,
            }

def getcert(host):
    hostbase = cfg.get('app','hostbase')
    uid = host #host[:-(len(hostbase)+1)]
    try:
        with open("%s/%s" % (cfg.get('app','redirs'), uid), 'r') as fd:
            port = int(fd.readline().strip())
    except IOError:
        port = 5001
    return portmap[port]

def setcert(host, type):
    hostbase = cfg.get('app','hostbase')
    uid = host #host[:-(len(hostbase)+1)]
    with open("%s/%s" % (cfg.get('app','redirs'), uid), 'w') as fd:
        fd.write("%s\n" % mapports[type])

@app.context_processor
def contex():
    global cfg, query
    return {'cfg'   : cfg
           ,'query' : ''
           ,'path'  : request.path
           }

@app.route('/', methods=['GET'])
def index():
    hostbase = cfg.get('app', 'hostbase')
    host = urlparse(request.url).hostname
    if not host.endswith('%s' % hostbase):
        raise ValueError("wrong host %s" % repr(host))
    if host in [hostbase, 'www.%s' % hostbase]:
        prefix = rnd(8)
        s = Snifer("/home/certcheck/snifer/redirs")
        s.set(prefix, 'certcheck.me', "5001")
        resp = make_response(redirect('https://%s.%s/' % (prefix, hostbase)))
    else:
        cert = getcert(host)
        resp = make_response(render_template('index.html', error=None, cert=cert))
    resp.headers['Connection'] = 'close'
    return resp

@app.route('/<string:act>', methods=['GET'])
def change_cert(act):
    hostbase = cfg.get('app', 'hostbase')
    host = urlparse(request.url).hostname
    if act not in mapports: abort(404)
    if not host.endswith('%s' % hostbase):
        raise ValueError("wrong host %s" % repr(host))
    setcert(urlparse(request.url).hostname, act)

    resp = make_response(redirect('/'))
    resp.headers['Connection'] = 'close'
    return resp

if __name__ == "__main__":
    app.run(debug        = cfg.get('server', 'debug')
           ,use_debugger = cfg.get('server', 'debug')
           ,port         = int(cfg.get('server', 'port'))
           #,host         = int(cfg.get('server', 'host'))
           )
