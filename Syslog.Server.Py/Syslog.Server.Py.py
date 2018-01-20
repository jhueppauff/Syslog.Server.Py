#!/usr/bin/env python

LogFile = 'c:\log\syslog.log'
Host = '0.0.0.0'
Port = 514

## Do not change anything beneath this line, unless you know what you are doing

import logging
import socketserver

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LogFile, filemode='a')


class UDPListener(socketserver.BaseRequestHandler):
	def handle(self):
		data = bytes.decode(self.request[0].strip())
		socket = self.request[1]
		print( "%s : " % self.client_address[0], str(data))
		logging.info(str(data))

if __name__ == "__main__":
	try:
		server = socketserver.UDPServer((Host,Port), UDPListener)
		server.serve_forever(poll_interval=0.5)
	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:print ("Crtl+C Pressed. Shutting down.")
