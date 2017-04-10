#!/usr/bin/env python3
from colour import colour
from position import position
from common import percent, length, angle, rc, ri

# The extents that can be applied to a radial gradient
extents = ("closest-corner", "closest-side", "farthest-corner", "farthest-side")

# A tuple containing the different options a colour stop can be
colourStop = (
	colour(),
	colour()+" "+percent(),
	colour()+" "+length()
)

# Generate a series of colour stops
def nOrMoreColourStops(n=1):
	#if ri(0,1) == 1 or n == 1:
	#	return rc(colourStop)
	#else:
	#	return "".join((lambda: rc(colourStop))()+", " for x in range(0,ri(n,10))) + rc(colourStop)
	return "".join((lambda: rc(colourStop))()+", " for x in range(0,ri(n,10))) + rc(colourStop)

radials = (
	lambda: "radial-gradient(at {}, {})".format(
		position(),
		nOrMoreColourStops(2)
	),
	lambda: "radial-gradient({} {}, {})".format(
		rc((
			rc(("circle","ellipse")) + " " + rc(extents),
			rc(extents) + " " + rc(("circle","ellipse"))
		)),
		
		rc(("at " + position(), "")),
		nOrMoreColourStops(2)
	),
	lambda: "radial-gradient({} {}, {})".format(
		rc((
			"ellipse", rc((length(allowNeg=False) + " " + length(allowNeg=False), percent(allowNeg=False) + " " + percent(allowNeg=False))),
			rc((length(allowNeg=False) + " " + length(allowNeg=False), percent(allowNeg=False) + " " + percent(allowNeg=False))) + " ellipse",
			"ellipse",
			rc((length(allowNeg=False) + " " + length(allowNeg=False), percent(allowNeg=False) + " " + percent(allowNeg=False)))
		)),
		rc(("at " + position(), "")),
		nOrMoreColourStops(2)
	),
	lambda: "radial-gradient({} {}, {})".format(
		rc((
			rc(("circle", length(allowNeg=False))),
			"circle " + length(allowNeg=False),
			length(allowNeg=False) + " circle"
		)),
		rc(("at " + position(), "")),
		nOrMoreColourStops(2)
	)
)

# Generate a radial gradient
def radialGradient():
	return rc(radials)()

# Generate a linear gradient
def linearGradient():
	return "linear-gradient({}, {})".format(
		rc((
			angle(),
			"to " + rc((rc(("left","right")), rc(("top","bottom"))))
		)),
		nOrMoreColourStops(2)
	)

# Generate a random gradient
def gradient():
	ret = ""
	if ri(0,2) == 2:
		ret = "repeating-"
	return ret+rc((linearGradient, radialGradient))()