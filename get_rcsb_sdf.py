import sys, os
import urllib.request

ls = []

fn = "nosmiles.txt"
if len(sys.argv)> 1:
    fn = sys.argv[1]

with open(fn) as f:
    ls = f.readlines()

for l in ls:
    tlc = os.path.split(l)[-1].rstrip().rstrip(".cif")
    print(tlc)
    try:
       urllib.request.urlretrieve("https://files.rcsb.org/ligands/download/"+tlc+"_ideal.sdf", os.path.join("RCSB_SDF",tlc+".sdf"))
    except urllib.error.HTTPError:
       print(tlc,"not on server?")
