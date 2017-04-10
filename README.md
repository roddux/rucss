# RuCSS : A CSS fuzzer with test generator and a web wrapper
---
This is yet another fuzzer aimed at blowing holes in Firefox and Chromium.

_Ruckus - A row or commotion_

# Usage
---
```$ rucss/generator.py <number of tests> <output directory> <split>```

Pretty self explanatory. The `<split>` option tells RuCSS how many processes you intend to run whilst fuzzing -- and splits up the output cases into an appropriate number of directories. Load the starting file in your browser and each test case will automatically load the next.

The output directory defaults to `tests` if unspecified and split defaults to `1` (no split).

```$ rucss/webhandler.py -r <refresh method> -p <port>```

Starts serving generated test cases on port 8080 until asked to stop. The web handler will keep an approximate count of how many requests per second the browser is making.

RuCSS performs a rough timeout check for the web handler. If the number of requests per second hits 0, it will save the last 10 outputs to file.

# Trophy case
---
DoS:
- https://bugzilla.mozilla.org/show_bug.cgi?id=1236224

Crashes (non-exploitable):
- https://bugzilla.mozilla.org/show_bug.cgi?id=1286889

Crashes (exploitable):
- ;)


# Further reading
---
http://ucaat.etsi.org/2015/presentations/HTB_HODOVAN.pdf
https://developer.mozilla.org/en-US/docs/Web/CSS/Reference