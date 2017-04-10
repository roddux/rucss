#!/usr/bin/env python3
from sys import argv
from os import mkdir, getcwd
from badgen import genBad
import getopt
import random

def setup(outdir, tsplits=1):
	try:
		mkdir(outdir)
		for j in range(0,tsplits):
			mkdir(outdir+"/"+str(j))
	except FileExistsError as ex:
		print("ERROR: Output directory '%s' already exists!" % ex.filename)
		return False
	return True

def getTestName(csplit, counter):
	return "rucss_%d_%d.html" % (csplit,counter)

def writeTest(counter, outdir, csplit, refreshMode):
	meta = ("<!doctype html><html><head><meta http-equiv=\"refresh\" content=\"0; url=%s\"></head><body>" % getTestName(csplit,counter+1)).encode("UTF-8")
	dom = ("<!doctype html><html><body><script>document.addEventListener('DOMContentLoaded',function(){document.location = '%s'})</script>" % getTestName(csplit,counter+1)).encode("UTF-8")
	with open(outdir+"/"+str(csplit)+"/"+getTestName(csplit,counter), "wb") as x:
		if refreshMode == "meta": x.write(meta)
		if refreshMode == "dom": x.write(dom)
		x.write(bytes(genBad()))
		x.write("</body></html>".encode("UTF-8"))

def usage():
	print("Usage: %s -n <number of tests> -o <output directory> -p <split> -r <refresh mode> -s <seed>" % argv[0])
	exit(1)

def main():
	print("RuCSS : Generator")

	try: opts, args = getopt.getopt(argv[1:], "n:o:p:r:s:")
	except getopt.GetoptError: usage()

	total   = None
	outdir  = "tests"
	tsplits = 1
	refreshMode = "dom"
	rseed   = None

	for o, a in opts:
		if o == "-n":
			total = int(a)
		elif o == "-o":
			outdir = a
		elif o == "-p":
			tsplits = int(a)
		elif o == "-r":
			refreshMode = a
		elif o == "-s":
			rseed = int(a)
		else: usage()

	if total == None: usage()
	if not setup(outdir, tsplits): exit(1)

	if rseed == None: rseed = random.randint(1,100000)
	print("Using random seed %d" % rseed)
	random.seed(rseed)

	current = 0
	csplit  = 0
	RUNNING = True
	print("Starting files: (may not yet all be present)")
	cwd = getcwd()
	for j in range(0,tsplits): print("\t%s/%s/%d/rucss_%d_0.html" % (cwd,outdir,j,j))
	print("")
	while csplit < tsplits and RUNNING:
		try:
			while current < total/tsplits:
				print("\rGenerating test case %s (%d/%d), ^C to stop..." %
					(getTestName(csplit,current), current, total), end="", flush=True)
				writeTest(current, outdir, csplit, refreshMode)
				current += 1
			csplit += 1
			current = 0
		except KeyboardInterrupt:
			print("\nQuitting...")
			RUNNING = False
	print("")
	exit(0)

if __name__ == "__main__":
	main()