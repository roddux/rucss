#!/usr/bin/env python3
import os, http.server, socketserver, getopt, random
from time import sleep
from threading import Thread
from urllib.parse import parse_qs
from collections import Counter
from time import localtime as lt
from sys import argv
from imp import reload as libreload

import colour, common, gradient, image, position, random

counter = Counter()
RUNNING = False
LASTTENFUZ = [None,None,None,None,None,None,None,None,None,None]
refreshMode = ""
gLFC = 0
serverHandle = None
timerThread = None
serveThread = None

dom  = b"""<!doctype html><html><body><style>
* { transition: all 20ms; }
div { width: 5em; height: 5em; display: block; }
</style><script>
var n = 1;
var junk="ABCDEFGHIJK"
function mswitch() {
	if (n >= 5) { return; }
	myList = document.getElementsByTagName("div");
	for (q in myList) {
		nClass = (junk.indexOf(q)+1) % 5;
		myList[q].className=junk[nClass];
	}
	n += 1;
	setTimeout(mswitch, 10);
}
mswitch();
setTimeout(window.location.reload.bind(window.location), 100);
</script>"""

divString = b"<div class=\"A\"></div><div class=\"B\"></div><div class=\"C\"><div class=\"D\"><div class=\"E\"></div></div></div>"

def genStyles():
	styles = b""
	randList = [
		("background: " + gradient.gradient() + ";").encode("utf-8"),
		("position: absolute; top: " + common.number() + "em; left: "  + common.number() + "em;").encode("utf-8"),
		("position: relative; top: " + common.number() + "em; left: "  + common.number() + "em;").encode("utf-8"),
		("height: " + common.length() + ";").encode("utf-8"),
		("height: " + common.percent() + ";").encode("utf-8"),
		("width: " + common.length() + ";").encode("utf-8"),
		("width: " + common.percent() + ";").encode("utf-8"),
		("max-width: " + common.length() + ";").encode("utf-8"),
		("max-height: " + common.length() + ";").encode("utf-8"),
		("transition: all " + common.time() + ";").encode("utf-8"),
	]
	for j in range(10): styles += random.choice(randList)
	return styles

def shitStyleGen():
	junk="ABCDEFGHIJK"
	ret = b"<style>"
	for x in range(5): ret += b".%s {" % junk[x].encode("UTF-8")+genStyles()+b"}\n"
	ret += b"</style>"
	return ret

def timerThread():
	global counter, RUNNING
	samehang = False
	while RUNNING:
		counter = 0
		sleep(5)
		print("\r%d total reqs/s\033[K" % int(counter/5), end="", flush=True)
		if counter < 5:
			if not samehang:
				print("\nCrudely detected a hang! Writing last 10 fuzzes to files...")
				writeLast()
				samehang = True
		else:
			samehang = False

class myHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		global counter, LASTTENFUZ, refreshMode, gLFC
		try:
			counter += 1
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			LASTTENFUZ[gLFC] = dom+shitStyleGen()+divString+b"</body></html>"
			self.wfile.write(LASTTENFUZ[gLFC])
			gLFC += 1
			gLFC = gLFC % 10
			return
		except (BrokenPipeError, ConnectionResetError):
			return
	def log_message(self, format, *args): return

def writeLast():
	try:
		for fuzData in LASTTENFUZ:
			lastfuznam = "LASTTENFUZ_"+badgen.ranNam()+".html"
			with open(lastfuznam, "wb") as x:
				x.write(fuzData)
				print("Saved to '%s'" % lastfuznam)
	except Exception:
		pass

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
	print("\nQuitting...")
	RUNNING = False
	serverHandle.shutdown()
	try:
		serveThread.join()
	except:
		pass
	try:
		timerThread.join()
	except:
		pass

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
	RUNNING = True
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
			print("\nWriting last 10 fuzzes to files...")
			writeLast()

	print("Bye!")
	exit(0)

if __name__ == "__main__":
	main()