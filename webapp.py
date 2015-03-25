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
info = {    5001: "This is the normal case: you visit a site and it presents its genuine certificate, which is genuinely signed by the real Certificate Authority. This is also the certificate that you are served when you first visit this site, you could say this is the real one, if there would be such a thing.",
            5002: "In this case the issuing authority (or someone controlling it) produced a second website certificate. This could be because the previous website certificate expired or when the services is available via multiple servers. This could be legitimate or not: it depends on a case-by-case basis. If you deal with sensitive website (e.g. your bank), you might want to avoid services that use such practices. In the worst case someone has taken illegitimate control of the CA and produced a new certificate to intercept the communication between you and the website you are visiting. Notice how a default browser configuration doesn't even bother in firefox to throw a scary window.",
            5003: "This is a valid Certificate Authority that has been used to create another certificate for this website. This can happen with content delivery networks - which would be legitimate - but also during MITM attacks (i.e. when someone was able to trick the CA to beileve it issues the cert to the legal owner, or when some 3rd party coercing or controlling the issuing CA to issue a cert for interception). Another case when this happens, if you have some kind of enterprise firewall, that does content filtering, in such cases it is custom, to install a local CA in all the browsers of the enterprise, and using this cert, the proxy is continously mounting MITM attacks against the companies employers.",
            5004: "Here you go with a completely unknown Certificate Authority and certificate. Unknown in this case means, the certificate is not shipped by your browser. Basically this can mean also different things: [1] this is a legitimate site, which does not want to buy a certificate from a CA (and then you should verify the fingerprints of the site), or [2] this is a certificate from a valid CA, which is not favored by the ruling class of CAs, but if you trust the CA you can import this yourself (e.g. there's a lot of sites with certs from a CA called CAcert), or [3] this is really a MITM attack. However, if this would be a MITM attack on a cert with a trusted CA in your browser it would be naive from the attacker's point of view, yet for sites that use self-signed certificates it makes it quite easy to MITM the connection if the fingerprints of the genuine site are not verified dilligently.",
            5005: "This is a quite common CA (called CAcert) which is a community run CA, and is a pariah among the for-profit CA industry, so it's not included in any of the otherwise so community friendly browswers. However there is a strong community behind CAcert which makes it quite common online. This is indeed one of the few CAs that you might want to install, otherwise it's quite a good idea to remove CAs you'll never encounter naturally, like various CAs related to foreign governments. Which those are, depends of course on your current life, but a general purging of all such is neither a bad idea.",
            5006: "This is a completely forged certificate from a forged Certificate Authority. Basically the counterfeited certificate looks almost the same of the real one in scenario 1, except for the fingerprints and a few less obvious details. This situation simulates what could be a moderately sophisticated attack."
        }

def hostbase():
    cfg.get('app','hostbase')

def getport(host):
    try:
        with open("%s/%s" % (cfg.get('app','redirs'), host), 'r') as fd:
            port = int(fd.readline().strip())
    except IOError:
        port = 5001
    return port

def getcert(host):
    port = getport(host)
    return portmap[port]

def setcert(host, type):
    with open("%s/%s" % (cfg.get('app','redirs'), host), 'w') as fd:
        fd.write("%s\n" % mapports[type])

def getinfo(host):
    port = getport(host)
    return info[port]

@app.context_processor
def contex():
    global cfg, query
    return {'cfg': cfg, 'query': '','path': request.path}

@app.route('/', methods=['GET'])
def index():
    host = urlparse(request.url).hostname
    if host!='localhost' and not host.endswith('%s' % hostbase):
        raise ValueError("wrong host %s" % repr(host))
    if host in [hostbase, 'www.%s' % hostbase]:
        prefix = rnd(8)
        s = Snifer(cfg.get('app','redirs'))
        s.set(prefix, hostbase, "5001")
        resp = make_response(redirect('https://%s.%s/' % (prefix, hostbase)))
    else:
        cert = getcert(host)      
        info = getinfo(host)
        resp = make_response(render_template('index.html', error=None, cert=cert, info=info))
    resp.headers['Connection'] = 'close'
    return resp

@app.route('/<string:act>', methods=['GET'])
def change_cert(act):
    host = urlparse(request.url).hostname
    if act not in mapports: abort(404)
    if host!='localhost' and not host.endswith('%s' % hostbase):
        raise ValueError("wrong host %s" % repr(host))
    setcert(urlparse(request.url).hostname, act)

    resp = make_response(redirect('/'))
    resp.headers['Connection'] = 'close'
    return resp

if __name__ == "__main__":
    app.run(
            debug        = cfg.get('server', 'debug'),
            use_debugger = cfg.get('server', 'debug'),
            port         = int(cfg.get('server', 'port'))
        )
