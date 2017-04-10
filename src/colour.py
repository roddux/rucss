#!/usr/bin/env python3
from common import rc, ri, integer, number, percent

def hexcol(n=6): return "#" + "".join(rc("ABCDEF") for j in range(0,n))

class colourC():
	# Mozilla specific colours taken from MDN
	moz = (
		"-moz-ButtonDefault", "-moz-ButtonHoverFace", "-moz-ButtonHoverText", "-moz-CellHighlight",
		"-moz-CellHighlightText", "-moz-Combobox", "-moz-ComboboxText", "-moz-Dialog", "-moz-DialogText",
		"-moz-dragtargetzone", "-moz-EvenTreeRow", "-moz-Field", "-moz-FieldText", "-moz-html-CellHighlight",
		"-moz-html-CellHighlightText", "-moz-MenuHover", "-moz-MenuHoverText", "-moz-MenuBarText",
		"-moz-MenuBarHoverText", "-moz-nativehyperlinktext", "-moz-OddTreeRow", "-moz-win-communicationstext", 
		"-moz-win-mediatext"
	)

	# 'Deprecated' colours taken from MDN
	deprecated = (
		"ActiveBorder", "ActiveCaption", "AppWorkspace", "Background", "ButtonFace",
		"ButtonShadow", "ButtonText", "CaptionText", "GrayText", "Highlight", "HighlightText",
		"InactiveBorder", "InactiveCaption", "InactiveCaptionText", "InfoBackground", "InfoText",
		"Menu", "MenuText", "Scrollbar", "ThreeDDarkShadow", "ThreeDFace", "ThreeDHighlight",
		"ThreeDLightShadow", "ThreeDShadow", "Window", "WindowFrame", "WindowText", "ButtonHighlight"
	)

	# Named colours
	named = (
		"black", "silver", "gray", "white", "maroon", "red", "purple",
		"fuchsia", "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua",
		"orange", "aliceblue", "antiquewhite", "aquamarine", "azure", "beige", "bisque",
		"blanchedalmond", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse",
		"chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "darkblue",
		"darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki",
		"darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred",
		"darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey",
		"darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey",
		"dodgerblue", "firebrick", "floralwhite", "forestgreen", "gainsboro",
		"ghostwhite", "gold", "goldenrod", "greenyellow", "grey", "lightseagreen",
		"lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue",
		"lightyellow", "limegreen", "linen", "mediumaquamarine", "mediumblue",
		"mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue",
		"mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue",
		"mintcream", "mistyrose", "moccasin", "navajowhite", "oldlace", "olivedrab",
		"orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise",
		"palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum",
		"powderblue", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown",
		"seagreen", "seashell", "sienna", "skyblue", "slateblue", "slategray",
		"slategrey", "snow", "springgreen", "steelblue", "tan", "thistle", "tomato",
		"turquoise", "violet", "wheat", "whitesmoke", "yellowgreen", "rebeccapurple"
	)

	colours = (
		rc((
			lambda: "rgb({},{},{})".format(
				integer(),
				integer(),
				integer(),
			),
			lambda: "rgb({},{},{})".format(
				percent(),
				percent(),
				percent(),
			)
		)),
		rc((
			lambda: "rgba({},{},{},{})".format(
				integer(),
				integer(),
				integer(),
				number()
			),
			lambda: "rgba({},{},{},{})".format(
				percent(),
				percent(),
				percent(),
				number()
			),
		)),
		lambda: "hsl({},{},{})".format(
			number(),
			percent(),
			percent()
		),
		lambda: "hsla({},{},{},{})".format(
			number(),
			percent(),
			percent(),
			number(),
		),
		lambda: hexcol(rc((3,6))),
		lambda: rc(colourC.named),
		lambda: rc(colourC.deprecated),
		lambda: rc(colourC.moz),
		lambda: rc(("currentcolor", "transparent"))
	)

	# Generate a random colour
	def __str__(self):
		return rc(self.colours)()

def colour():
	return(str(colourC()))