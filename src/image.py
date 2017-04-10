#!/usr/bin/env python3
from common import rc, ri, url
from gradient import gradient

# Generate an image
def image():
	if ri(0,1) == 0:
		return url()
	else:
		return gradient()