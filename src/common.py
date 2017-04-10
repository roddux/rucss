# https://developer.mozilla.org/en-US/docs/Web/CSS/Value_definition_syntax#Double_bar
# https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
from random import choice as rc, randint as ri, random as rand
from string import ascii_uppercase as allup

# Only simple types that depend on other simple types will be here, all others
# will get their own file

# Generate a percentage
def percent(allowNeg=True): return number(allowNeg)+"%"

# Generate a frequency
def frequency(): return number()+rc(("Hz","kHz"))

# Generate a time
def time(): return number()+rc(("s","ms"))

# Generate a shape
# According to MDN, the current spec is limited to only the rect() function
def shape(): return "rect(%s,%s,%s,%s)" % (length(),length(),length(),length())

# Generate an integer
def integer(allowNeg=True):
	ret = ""
	if allowNeg:
		if ri(0,2) == 2: ret += "-"
		elif ri(0,2) == 2: ret += "+"
	ret += "%d" % ri(1,10)
	return ret

# Generate a number
def number(allowNeg=True):
	ret = ""
	if allowNeg:
		if ri(0,2) == 2: ret += "-"
		elif ri(0,2) == 2: ret += "+"
	if ri(0,1) == 0: ret += "%.2f" % (rand() * ri(1,10))
	else: ret += "%d" % ri(1,10)
	if ri(0,3) == 3: ret += "e-5"
	elif ri(0,3) == 2: ret += "e5"
	return ret

# Generate a length
def length(allowNeg=True):
	return number(allowNeg) + rc(
		(
			"em","ex","ch","rem",
			"vh","vw","vmin","vmax",
			"px","mm","cm","in","pt","pc",
			"mozmm"
		)
	)

# Generate a blend pattern
def blendPattern():
	return rc(
		(
			"normal", "multiply", "screen", "overlay", "darken",
			"lighten", "color-dodge", "color-burn", "hard-light",
			"soft-light", "difference", "exclusion", "hue", "saturation",
			"color", "luminosity"
		)
	)

# Generate an angle
def angle(): return number() + rc( ("deg","grad","rad","turn") )

# Generate a string
def string(): return "".join(rc(allup) for j in range(0,50))

# Generate a URL
# TODO: Relative paths, data-blob URIs, ftp:// URIs, other image types 
def url():
	ret = "https://www.google.co.uk/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
	if ri(0,1) == 1: ret = "http" + ret[5:]
	return rc(("url(%s)","url(\"%s\")")) % ret