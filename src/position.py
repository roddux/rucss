#!/usr/bin/env python3
from common import percent, length, rc, ri

positions = (
	lambda: "{}".format(
		rc( ("left", "center", "right", "top", "bottom", percent(), length()) )
	),
	lambda: "{} {}".format(
		rc( ("left", "center", "right", percent(), length()) ),
		rc( ("top", "center", "bottom", percent(), length()) )
	),
	rc((
		lambda: "{} {}".format(
			rc( ( "center", rc(("left","right")) ) ),
			rc( ( "", rc( ( percent(), length() ) ) ) )
		),
		lambda: "{} {}".format(
			rc( ( "center", rc(("top","bottom")) ) ),
			rc( ( "", rc( ( percent(), length() ) ) ) )
		)
	))
)

# Generate a position
# TODO: Implement optional ordering of keywords
# TODO: Investigate invalid generations for radial-gradient
def position(): return rc(positions)()