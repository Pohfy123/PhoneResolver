#!/usr/bin/env python
import sys, json

# Load the data that PHP sent us
import base64


try:
    data = json.loads(base64.b64decode(sys.argv[1]))
except:
    print "ERROR"
    sys.exit(1)

# Generate some data to send to PHP
result = {
    'status': '200', 
    'data': [
        {
            'input': data['input'],
            'result': {
                'category': [
                    {'name':'Restaurant', 'score': 0.9042342}
                ]
            }
        }
    ]
}

# Send it to stdout (to PHP)
print json.dumps(result)