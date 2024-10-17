import os
import glob
import itertools

dirs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
"U", "V", "W", "X", "Y", "Z"]

tHeader = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>SVG</title>
    <link rel="stylesheet" href="../style.css">
  </head>
  <body>
"""

tTail = """  </body>
</html>
"""


for d in dirs:
    os.chdir(d)

    svgs = sorted(glob.glob("*.svg"))
    batches = itertools.batched(svgs,100)
    ibatch = 1
    tMain = tHeader
    tMain += '<ul>\n'
    for b in batches:
        t = tHeader
        for s in b:
            t += '<figure>\n'
            t += '<img src="'+s+'" alt="'+s+'" />\n'
            t += '<figcaption>'+s.rstrip(".svg")+'</figcaption>\n'
            t += '</figure>\n'

        t += tTail

        with open("index-"+str(ibatch)+".html","w+") as f:
            f.write(t)

        indexLabel = b[0].rstrip(".svg")+'-'+b[-1].rstrip(".svg")

        tMain += '<li><a href="'+'index-'+str(ibatch)+'.html">'+indexLabel+'</a></li>'+'\n'

        ibatch += 1

    tMain += '</ul>\n'
    tMain += tTail
    with open("index.html","w+") as f:
        f.write(tMain)

    os.chdir("..")

