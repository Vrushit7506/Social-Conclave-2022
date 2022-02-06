#Test-Application

#import os
#import sys

#sys.path.insert(0, os.path.dirname(file))

#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#    message = 'Website Under Construction!\n'
#    version = 'Python %s\n' % sys.version.split()[0]
#    response = '\n'.join([message, version])
#    return [response.encode()]

#Main-Application
import imp
import os
import sys
from SocialConclave.wsgi import application