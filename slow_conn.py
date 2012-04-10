#!/usr/bin/env python

from httplib import HTTPSConnection as Connection
import time
import sys

# send data
conn = Connection(sys.argv[1])  # example.com:8090
conn.request('GET', '/', headers={})
resp = conn.getresponse()
total_len = int(resp.getheader('Content-Length'))
out = []
for i in range(total_len):
    out.append(resp.read(1))
    sys.stdout.write('\r%d' % i)
    sys.stdout.flush()
    time.sleep(2)
conn.close()
print ''.join(out)
