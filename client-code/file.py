#!usr/bin/env python

from ftplib import FTP, error_perm
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LAEST.tar.gz'

def main():
	try:
		f = FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print 'ERROR: cannot reach', HOST
		return
	print 'connect to ', HOST

	try:
		f.login()
	except error_perm:
		print 'wrong'
		f.quit()
		return

	try:
		f.cwd(DIRN)
	except error_perm:
		print 'wrong'
		f.quit()
		return

	try:
		f.retrbinary('RETR %s' %FILE, open(FILE, wb).write)
	except error_perm:
		print 'wrong'
		os.unlink(FILE)

	f.quit()

if __name__ == '__main__':
	main()