#!/usr/bin/env python3
from string import ascii_uppercase as rndchars
from random import choice as rc
from random import randint as ri

elements = ("a", "abbr", "acronym", "address", "applet", "article", "aside",
"audio", "b", "basefont", "bdi", "bdo", "bgsound", "big", "blink", "blockquote",
"body", "button", "canvas", "caption", "center", "cite", "code", "colgroup",
"command", "content", "data", "datalist", "dd", "del", "details", "dfn",
"dialog", "dir", "div", "dl", "dt", "element", "em", "fieldset", "figcaption",
"figure", "font", "footer", "form", "frame", "frameset", "header", "hgroup",
"i",  "image", "ins", "kbd", "label", "legend", "li", "listing",  "main", "map",
"mark", "marquee", "menu", "menuitem", "meter", "multicol", "nav", "nobr",
"object", "ol", "optgroup", "option", "output", "p", "picture", "q", 
  "s", "samp", "section", "select", "shadow", "small", "spacer",
"span", "strike", "strong",  "sub", "summary", "sup", "table", "tbody", "td",
"template",  "tfoot", "th", "thead", "time",  "tr", "tt", "u", "ul", "var",
"video", "pre", "svg", "use", "rt", "ruby", "rp", "rtc",)

selfclosers = ("area", "base", "br", "col", "embed", "hr", "img", "input",
"keygen", "link", "meta", "param",  "source", "track", "wbr")

rules = (
	#"filter: drop-shadow(5px 5px 5px red);",
	#"filter: blur(3px);",
	"flex: content;",
	"flex: 2 2 10%;",
	"filter: contrast(900%);",
	"filter: hue-rotate(90deg) invert(75%);",
	"filter: contrast(175%) brightness(3%);",
	"height: 10em;",
	"height: 75%;",
	"width: 10em;",
	"width: 75%;",
	"background: rgba(255,0,0,0.5);",
	"background-blend-mode: overlay, lighten;",
	"background-blend-mode: color-dodge;",
	"border-inline-start: 90px solid;",
	"border: 1px solid red;",
	"transition: all 50ms;",
	"position: absolute; top: -10em; left: -10em;",
	"position: absolute; top: 1000px; left: -1000px;",
	"position: relative; top: 1000px; left: -1000px;",
	"box-sizing: content-box;",
	"outline-color: invert;",
	"outline-color: red;",
	"object-fit: fill;",
	"object-fit: contain;",
	"object-fit: cover;",
	"object-fit: none;",
	"object-fit: scale-down;",
	"object-position: 99px 99px;",
	"object-position: 90% 90%;",
	"box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);",
	"box-decoration-break: slice;",
	"zoom: 150%;",
	"word-spacing: 200%;",
	"box-decoration-break: clone;",
	"box-sizing: border-box;",
	"shape-margin: 60%;",
	"margin: 5em;",
	"padding: 5em;",
	"transform: translate(90px, 50%);",
	"transform: translateX(90em) translateY(3in);",
	"transform: scale(9, 0.1);",
	"transform: scaleX(2) scaleY(0.5);",
	"transform: rotate(1turn) perspective(90px);",
	"transform: skew(30deg, 20deg) skewX(90deg) skewY(7rad);",
	"transform: matrix3d(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0);",
	"transform: translate3d(12px, 50%, 3em);",
	"transform: translateZ(2px);",
	"transform: scale3d(2.5, 1.2, 0.3);",
	"transform: scaleZ(0.3);",
	"transform: rotate3d(1, 2.0, 3.0, 10deg);",
	"transform: rotateX(10deg) rotateY(10deg) rotateZ(10deg);",
	"transform: translateX(10px) rotate(10deg) translateY(5px);",
	"display: grid; grid: subgrid;",
	"display: grid; grid: 100px 1fr;",
	# "display: grid; grid: [linename1] 100px [linename2 linename3];",
	"display: grid; grid: 200px repeat(auto-fill, 100px) 300px;",
	"display: grid; grid: minmax(100px, max-content) repeat(auto-fill, 200px) 20%;",
	"display: grid; grid: dense minmax(300px, max-content);",
	"display: grid; grid: row 400px / 40%;",
	"display: grid; grid: column auto / minmax(mix-content, 1fr);",
	"font-size: xx-small;",
	"font-size: xx-large;",
	"font-size: 12px;",
	"font-size: 0.8em;",
	"perspective: 20px;",
	"perspective: 3.5em;",
	"break-inside: avoid;",
	"break-inside: avoid-page;",
	"break-inside: avoid-column;",
	"break-inside: avoid-region;",
	"clip-path: inset(100px 50px);",
	"clip-path: circle(50px at 0 100px);",
	"clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);",
	"clip-path: fill-box;",
	"clip-path: stroke-box;",
	"clip-path: view-box;",
	"columns: 1em;",
	"columns: 1;",
	"columns: auto;",
	"columns: 1 auto;",
	"columns: auto 12em;",
	"columns: auto auto;",
	"overflow: visible;",
	"overflow: hidden;",
	"overflow: scroll;",
	"orphans: 3;",
	"order: 5;",
	"order: -5; ",
	"z-index: 289;",
	"z-index: -1; ",
	"unicode-bidi: embed;",
	"unicode-bidi: isolate;",
	"unicode-bidi: bidi-override;",
	"unicode-bidi: isolate-override;",
	"suffix: \"sdfsdfsf\";",
	"suffix: \") \";",
	"outline: 1px solid white;",
)

combinators = (">", "+", "~", " ")

simplePseudo = (":active", "::after", "::before", ":checked", ":default",
":disabled", ":visited", ":valid", ":unresolved", ":target", ":selection",
":scope", ":root", ":right", ":repeat-item", ":required", ":repeat-index",
":read-only", ":read-write", ":out-of-range", ":optional", ":only-child",
":only-of-type", ":link", ":last-child", ":last-of-type", ":left", ":invalid",
":in-range", ":indeterminate", ":hover", ":fullscreen", ":focus", ":first",
":first-child", ":first-letter", ":first-line", ":first-of-type", ":enabled",
":empty", ":-moz-display-comboboxcontrol-frame", ":-moz-dropdown-list",
 "::-moz-line-frame")

complexPseudo = ( ":not", ":any" )

numericPseudo = ( ":nth-child", ":nth-last-child", ":nth-last-of-type", ":nth-of-type" )

def ranNam(): return "".join(rc(rndchars) for j in range(0,10))

def genSelector(recurseCount=0):
	global usedElements, usedClasses
	selStr = ""
	
	j = ri(1,5)
	if j == 1:
		selStr += "#" + rc(usedIds)
	elif j >= 2 and j < 4:
		selStr += rc(usedElements)
	else:
		selStr += "." + rc(usedClasses)

	if ri(1,4) == 1:
		selStr += rc(combinators)
		j = ri(1,5)
		if j == 1:
			selStr += "#" + rc(usedIds)
		elif j == 2:
			selStr += rc(usedElements)
		else:
			selStr += "." + rc(usedClasses)

	if ri(1,5) == 1:
		selStr += rc(numericPseudo) + "(" + str(ri(1,5)) + ")"

	if ri(1,5) == 1 and recurseCount <= 10:
		selStr += rc(complexPseudo) + "(" + genSelector(recurseCount=recurseCount+1) + ")"

	return selStr

def genElements(recurseCount=0):
	global usedIds, usedClasses, usedElements
	BADLEN        = 20
	usedElements += [rc(elements) for j in range(BADLEN)]

	divString = b"\n"
	closer    = b"\n"
	if recurseCount: BADLEN = int(BADLEN/2)
	for j in range(BADLEN):
		selfCloser = (ri(0,10) >= 7)
		tagName    = rc(selfclosers) if selfCloser else rc(elements)
		if tagName not in usedElements: usedElements.append(tagName)
		tagName    = tagName.encode("UTF-8")

		clsId = ri(1,2)
		divString += b"<%s %s=\"%s\">%s</%s>" % (
			tagName,
			b"class" if clsId == 1 else b"id",
			rc(usedClasses).encode("UTF-8") if clsId == 1 else rc(usedIds).encode("UTF-8"),
			genElements(recurseCount=recurseCount+1) if ri(1,10)==3 and recurseCount<=2 else genContent(),
			tagName
		)

		if not selfCloser: closer = b"</%s>\n" % tagName + closer if ri(1,2) == 1 else b""
	divString += closer + b"\n"

	return divString

def genContent():
	j = ri(1,2)
	if   j == 1: return ("X"*50).encode("UTF-8")
	elif j == 2: return bytes(ri(0,255) for x in range(100))

def genPart():
	# j = ri(1,15)
	# if j == 6:
	# 	return genSelector() + """
	# 	{animation-duration:.00001ms;animation-name:XYXX;animation-iteration-count: infinite;}
	# 	@keyframes XYXX { from { %s } to { %s } }
	# 	""" % (rc(rules),rc(rules))
	# else:
	return genSelector() + "{" + rc(rules) + "}"

# existingClasses = [
# 	"archives",
# 	"benefits",
# 	"css-resources",
# 	"design-archives",
# 	"designer-name",
# 	"design-name",
# 	"design-selection",
# 	"explanation",
# 	"extra1",
# 	"extra2",
# 	"extra3",
# 	"extra4",
# 	"extra5",
# 	"extra6",
# 	"indicator",
# 	"intro",
# 	"main",
# 	"next",
# 	"page-wrapper",
# 	"participation",
# 	"preamble",
# 	"requirements",
# 	"resources",
# 	"select",
# 	"sidebar",
# 	"summary",
# 	"supporting",
# 	"viewall",
# 	"view-css",
# 	"wrapper",
# 	"zen-accessibility",
# 	"zen-faq",
# 	"zen-github",
# 	"zen-license",
# 	"zen-resources",
# 	"zen-submit",
# 	"zen-translations",
# 	"zen-validate-css",
# 	"zen-validate-html"
# ]

# existingClasses = [
# 	"janrainShareContactSearchResults",
# 	"story-views",
# 	"popular",
# 	"tag",
# 	"janrain-provider-icon-24",
# 	"janrain-provider-icon-linkedin",
# 	"janrainProviderList",
# 	"btn",
# 	"btn-success",
# 	"sd-key-firehose-id",
# 	"janrainDrawerButton",
# 	"edit-bar",
# 	"doughnut-chart-label",
# 	"janrainShareSelectedContactsList",
# 	"janrainShareTextContainer",
# 	"novote",
# 	"janrainShareCloseButton",
# 	"tag-menu",
# 	"janrainReturnAddress",
# 	"icon-tag",
# 	"collapse",
# 	"thisday-yr",
# 	"janrainShareDescription",
# 	"janrainSharingProgressBar",
# 	"background-undefined",
# 	"janrainDrawerButtonContainer",
# 	"janrainShareCount",
# 	"logoDiv",
# 	"link-attribution",
# 	"type",
# 	"videoCube_aspect",
# 	"janrainProgressIndicator",
# 	"ellipsis-2",
# 	"topic",
# 	"janrainShareImage",
# 	"cmntcnt",
# 	"janrainProvider",
# 	"janrain_linkedinButton",
# 	"paginate",
# 	"story",
# 	"tag-bar",
# 	"none",
# 	"janrainContactList",
# 	"janrainProviderDestination",
# 	"janrainShareInputCounter",
# 	"janrainShareCaption",
# 	"janrainShareResponseMessage",
# 	"janrainError",
# 	"item-thumbnail-href",
# 	"tag-entry",
# 	"default",
# 	"btn-polls",
# 	"janrainShareContent",
# 	"story-controls",
# 	"details",
# 	"trc_rbox_header_span",
# 	"ellipsis-1",
# 	"janrainShareMessage",
# 	"trc_header_ext",
# 	"janrainSocialBar",
# 	"sf-size",
# 	"janrainComposeMessageHeader",
# 	"janrainSocialPlaceholder",
# 	"filter-firehose",
# 	"comment-bubble",
# 	"dept-text",
# 	"icon-beaker",
# 	"pop1",
# 	"ellipsis-3",
# 	"story-byline",
# 	"icon-chart-bar",
# 	"sodify",
# 	"janrain_facebookButton",
# 	"janrainShareInputCounterExcess",
# 	"row",
# 	"janrainShareTitle",
# 	"janrain_native-googleplusButton",
# 	"janrainShareSelectedContacts",
# 	"edit-toggle",
# 	"janrain_twitterButton",
# 	"link-adc",
# 	"clearfix",
# 	"meta",
# 	"article-foot",
# 	"janrainShareContactSearch",
# 	"thumbBlock",
# 	"janrainShareSubmitActions",
# 	"janrainShare",
# 	"border-undefined",
# 	"body",
# 	"fhitem",
# 	"fhitem-story",
# 	"article",
# 	"usermode",
# 	"thumbs",
# 	"grid_24",
# 	"p",
# 	"janrainShareForm",
# 	"janrainGravityEast",
# 	"janrainProvider_undefined",
# 	"story-details",
# 	"ico",
# 	"close",
# 	"sd-info-block",
# 	"janrainContent",
# 	"trc_rbox",
# 	"thumbnails-b",
# 	"trc-content-sponsored",
# 	"inactive",
# 	"more",
# 	"b",
# 	"user-access",
# 	"janrainShareSelectedContactsDetails",
# 	"branding",
# 	"trc_mobile_disclosure_link",
# 	"trc_attribution_position_top",
# 	"story-title",
# 	"video-label-box",
# 	"icon-angle-right",
# 	"story-sourcelnk",
# 	"janrainShareFromLine",
# 	"deals-wrapper",
# 	"actions",
# 	"janrainSocialRoot",
# 	"janrainOrientationHorizontal",
# 	"janrainFormFactorBar",
# 	"janrainProviders_5",
# 	"janrainModeBroadcast",
# 	"janrainShareCountHidden",
# 	"trc_logos_v_align",
# 	"thumbBlock_holder",
# 	"trc_adc_wrapper",
# 	"icon-book",
# 	"janrainShareUserInputArea",
# 	"janrainShareUrl",
# 	"text-undefined",
# 	"anon",
# 	"index2",
# 	"stories-view",
# 	"deals-rail",
# 	"slant",
# 	"item-label-href",
# 	"no",
# 	"extlnk",
# 	"janrainPage",
# 	"form-group",
# 	"thumbnail-overlay",
# 	"sr-only",
# 	"janrain_native-redditButton",
# 	"nav-label",
# 	"tag-menu-admin",
# 	"icon-quote-left",
# 	"video-label",
# 	"video-title",
# 	"tright",
# 	"tags",
# 	"trc_mobile_adc_link",
# 	"janrainShareCountContainer",
# 	"janrainReturnAddressEmail",
# 	"hide",
# 	"output",
# 	"link-disclosure",
# 	"attribution-disclosure-link-hybrid",
# 	"nav-secondary",
# 	"nothumbs",
# 	"trc_related_container",
# 	"trc_spotlight_widget",
# 	"trc_elastic",
# 	"trc_elastic_trc_93198",
# 	"nosort",
# 	"videoCube",
# 	"trc_spotlight_item",
# 	"origin-default",
# 	"thumbnail_top",
# 	"syndicatedItem",
# 	"textItem",
# 	"videoCube_5_child",
# 	"janrain-provider-icon-facebook",
# 	"trc_adc_s_logo",
# 	"deals-header",
# 	"story-tags",
# 	"trc_mobile_attribution_link",
# 	"providers",
# 	"message-bar",
# 	"nav-primary",
# 	"janrainHeader",
# 	"btn-close",
# 	"trc_rbox_outer",
# 	"janrain-provider-text-color-googleplus",
# 	"main-wrap",
# 	"has-rail-right",
# 	"nav-user",
# 	"container",
# 	"static-text",
# 	"top-right",
# 	"poll-choice",
# 	"sf_widget",
# 	"nav-wrap",
# 	"attribution-disclosure-link-sponsored",
# 	"thisday-tb",
# 	"push",
# 	"poll-controls",
# 	"videoCube_6_child",
# 	"nav-site",
# 	"trc_rbox_container",
# 	"nav-social",
# 	"rail-right",
# 	"ui-sortable",
# 	"fhroot",
# 	"trc_desktop_attribution_link",
# 	"nav-secondary-wrap",
# 	"janrain-provider-text-color-twitter",
# 	"doughnut-chart",
# 	"icon-twitter-squared",
# 	"form-inline",
# 	"nav-search-form",
# 	"janrain-provider-icon-twitter",
# 	"ui-icon",
# 	"trc_rbox_header",
# 	"trc_rbox_border_elm",
# 	"checkbox"
# ]

# existingClasses = [
# 	"alt_colour",
# 	"dcl",
# 	"login",
# 	"more",
# 	"adu",
# 	"dcmads",
# 	"GoogleActiveViewClass",
# 	"tweet_link",
# 	"fbook",
# 	"gplus",
# 	"linkin",
# 	"static",
# 	"nav_vulture",
# 	"black_vulture",
# 	"white_vulture",
# 	"nav_search",
# 	"black_search_icon",
# 	"white_search_icon",
# 	"front_nav",
# 	"sub_nav",
# 	"dtop_only",
# 	"story_row",
# 	"story_link",
# 	"data_cent_nav",
# 	"software_nav",
# 	"network_nav",
# 	"sec_nav",
# 	"infra_nav",
# 	"devops_nav",
# 	"bus_nav",
# 	"hard_nav",
# 	"sci_nav",
# 	"bootnotes_nav",
# 	"story_list",
# 	"story",
# 	"standfirst",
# 	"trailer",
# 	"large_story",
# 	"headlines",
# 	"headline_row",
# 	"first_headline",
# 	"section_name",
# 	"time_comments",
# 	"time_stamp",
# 	"headline",
# 	"comment",
# 	"news_bytes_column",
# 	"news_bytes_headline",
# 	"dont_miss_row",
# 	"dont_miss",
# 	"with_image",
# 	"story_grid_img",
# 	"hidden",
# 	"rhs_widget",
# 	"geo_gb",
# 	"move_left",
# 	"move_right",
# 	"promo_job",
# 	"content",
# 	"show",
# 	"job_title",
# 	"company",
# 	"inner",
# 	"job_content",
# 	"job_headline",
# 	"strap",
# 	"your_jobs",
# 	"text",
# 	"social",
# 	"twit",
# 	"circ",
# 	"rss_feed",
# 	"foot_list",
# 	"more_us",
# 	"last",
# 	"reg_foot",
# 	"copyr",
# 	"foot_desc",
# 	"alt_colour",
# 	"dcl",
# 	"login",
# 	"more",
# 	"adu",
# 	"dcmads",
# 	"GoogleActiveViewClass",
# 	"tweet_link",
# 	"fbook",
# 	"gplus",
# 	"linkin",
# 	"static",
# 	"nav_vulture",
# 	"black_vulture",
# 	"white_vulture",
# 	"nav_search",
# 	"black_search_icon",
# 	"white_search_icon",
# 	"front_nav",
# 	"sub_nav",
# 	"dtop_only",
# 	"story_row",
# 	"story_link",
# 	"data_cent_nav",
# 	"software_nav",
# 	"network_nav",
# 	"sec_nav",
# 	"infra_nav",
# 	"devops_nav",
# 	"bus_nav",
# 	"hard_nav",
# 	"sci_nav",
# 	"bootnotes_nav",
# 	"story_list",
# 	"story",
# 	"standfirst",
# 	"trailer",
# 	"large_story",
# 	"headlines",
# 	"headline_row",
# 	"first_headline",
# 	"section_name",
# 	"time_comments",
# 	"time_stamp",
# 	"headline",
# 	"comment",
# 	"news_bytes_column",
# 	"news_bytes_headline",
# 	"dont_miss_row",
# 	"dont_miss",
# 	"with_image",
# 	"story_grid_img",
# 	"hidden",
# 	"rhs_widget",
# 	"geo_gb",
# 	"move_left",
# 	"move_right",
# 	"promo_job",
# 	"content",
# 	"show",
# 	"job_title",
# 	"company",
# 	"inner",
# 	"job_content",
# 	"job_headline",
# 	"strap",
# 	"your_jobs",
# 	"text",
# 	"social",
# 	"twit",
# 	"circ",
# 	"rss_feed",
# 	"foot_list",
# 	"more_us",
# 	"last",
# 	"reg_foot",
# 	"copyr",
# 	"foot_desc",
# ]

usedIds      = ["A","B","C","D","E","F","G","H","I"]
existingClasses      = ["A","B","C","D","E","F","G","H","I"]
existingIds = existingClasses	
# existingIds = [
# 	"css-zen-garden",
# 	"zen-intro",
# 	"crapShoot",
# 	"zen-summary",
# 	"zen-preamble",
# 	"zen-supporting",
# 	"zen-explanation",
# 	"zen-participation",
# 	"zen-benefits",
# 	"zen-requirements",
# 	"design-selection",
# 	"design-archives",
# 	"zen-resources"
# ]

usedClasses  = existingClasses
# usedClasses  = existingClasses+["A","B","C","D","E","F","G","H","I"]

usedElements = [
	"html", "body", "div", "li", "a", "abbr", "h3", "nav", "span", "ul",
	"footer", "aside", "p", "section", "header", "h2", "h1", "img", "button",
	"span", "tr", "table", "td", "th", "noscript", "h4", "ol", "form"
]

def genBad():
	global usedIds, usedClasses, usedElements
	usedIds      = existingIds+["A","B","C","D","E","F","G","H","I"] # [ranNam() for j in range(0,BADLEN)]
	usedClasses  = existingClasses+["A","B","C","D","E","F","G","H","I"] # [ranNam() for j in range(0,BADLEN)]

	divString = genElements()

	headString = ""
	for j in range(10):
		headString += "\n<style>"
		for j in range(ri(1,5)): headString += genPart()+"\n"
		headString += "</style>"
	headString = headString.encode("UTF-8")

	return b"<style>*{transition:all 1ms;}</style>"+headString+divString
	# return b"<style>*{transition:all 1ms;}</style>"+headString
	# return headString

if __name__ == "__main__":
	x = genElements().decode("latin1")
	# print(x+" "*(10000))
	#print(genElements().decode("latin1"))