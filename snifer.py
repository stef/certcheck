#!/usr/bin/env python

import os

class Snifer():
    def __init__(self,path):
        if not os.path.exists(path):
            raise IndexError("snifer redir path does not exist: %s" % path)
        self.redirs = path

    def set(self, uid, domain, value):
        with open(os.path.join(self.redirs, "%s.%s" % (uid,domain)), 'w') as fd:
            fd.write(value)

    def get(self, uid, domain):
        with open(os.path.join(self.redirs, "%s.%s" % (uid,domain)), 'r') as fd:
            return fd.read()

if __name__ == "__main__":
    s = Snifer("/home/certcheck/snifer/redirs")
    print s.get('www','certcheck.me')
