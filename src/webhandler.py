#!/usr/bin/env python3
import badgen, os, http.server, socketserver, getopt, random
from time import sleep
from threading import Thread
from urllib.parse import parse_qs
from time import localtime as lt
from sys import argv
from imp import reload as libreload

# GLOBALS ARE BAD OK
gLFC        = 0
counter     = 0
RUNNING     = False
LASTTENFUZ  = [None,None,None,None,None,None,None,None,None,None]
refreshMode = ""
serverHandle = None
timerThread  = None
serveThread  = None

meta = b"<!doctype html><html><head><meta http-equiv=\"refresh\" content=\"0\"></head><body>"
dom  = b"<!doctype html><html><body><script>document.addEventListener('DOMContentLoaded',function(){document.location.reload()})</script>"

def timerThread():
	global counter, RUNNING
	samehang = False
	while RUNNING:
		counter = 0
		sleep(5)
		print("\r%d total reqs/s\033[K" % int(counter/5), end="", flush=True)
		if counter < 5:
			if not samehang:
				print("\nDetected a hang! Writing last 10 outputs to disk...")
				writeLast()
				samehang = True
		else: samehang = False

class myHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		global counter, LASTTENFUZ, refreshMode, gLFC
		try:
			counter += 1
			self.send_response(200)
			self.send_header("Access-Control-Allow-Origin", "*")
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			if refreshMode == "raw":
				LASTTENFUZ[gLFC] = badgen.genBad()
			elif refreshMode == "dom":
				LASTTENFUZ[gLFC] = dom+badgen.genBad()+b"</body></html>"
			else:
				LASTTENFUZ[gLFC] = meta+badgen.genBad()+b"</body></html>"
			self.wfile.write(LASTTENFUZ[gLFC])
			gLFC = (gLFC+1) % 10
			return
		except (BrokenPipeError, ConnectionResetError):
			return
	def log_message(self, format, *args): return

def writeLast():
	try:
		for q in range(len(LASTTENFUZ)):
			lastfuznam = "POTENTIAL/LASTTENFUZ_"+str(q)+"_"+badgen.ranNam()+".html"
			with open(lastfuznam, "wb") as x:
				x.write(LASTTENFUZ[q])
				print("Saved to '%s'" % lastfuznam)
	except Exception: pass

def usage():
	print("Usage: %s -r <refresh mode> -s <seed> -p <port>" % argv[0])
	exit(1)

def serveThread(): # So we can wait for keyboard input in the main thread
	global serverHandle
	serverHandle.serve_forever()
	serverHandle.shutdown()
	serverHandle.socket.close()

def quit():
	global RUNNING
	RUNNING = False
	print("\nQuitting...")
	serverHandle.shutdown()
	try:    timerThread.join()
	except: pass
	try:    serveThread.join()
	except: pass

def main():
	global refreshMode, serverHandle, RUNNING, badgen, serveThread, timerThread

	try: opts, args = getopt.getopt(argv[1:], "r:s:p:")
	except getopt.GetoptError: usage()

	refreshMode = "dom"
	rseed       = None
	port        = 8080

	for o, a in opts:
		if o == "-r":
			refreshMode = a
		elif o == "-s":
			rseed = int(a)
		elif o == "-p":
			port = int(a)
		else: usage()

	if rseed == None: rseed = random.randint(1,100000)

	server = socketserver.TCPServer(("", port), myHandler)

	print("RuCSS : Web handler\nUsing seed %d\nFuzzing on port %d, ^C or q to stop..." % (rseed,port))
	RUNNING      = True
	serverHandle = server
	
	tt = Thread(target=timerThread)
	tt.start()
	st = Thread(target=serveThread)
	st.start()

	timerThread = tt
	serveThread = st

	cmd = None
	while RUNNING:
		try:
			cmd = input("")
		except KeyboardInterrupt:
			quit()
		if cmd == "q":
			quit()
		elif cmd == "r":
			print("\nReloading fuzz library...")
			badgen = libreload(badgen)
		else:
			print("\nWriting last 10 outputs to disk...")
			writeLast()

	print("Bye!")
	exit(0)

if __name__ == "__main__": main()