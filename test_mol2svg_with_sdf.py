import sys
import os
import glob
import traceback

from rdkit import Chem
from mol2svg import svgFromMol

files = sorted(glob.glob(os.path.join("RCSB_SDF/*.sdf")))

#files = ["RCSB_SDF/ZEM.sdf"]

for fn in files:
    name = os.path.basename(fn).split(".")[0]
    output = os.path.join("FROM_SDF",name[0],name+".svg")
    os.makedirs(os.path.join("FROM_SDF",name[0]), exist_ok=True)
    try:
        with open(fn) as f:
           b = f.read()
        mol = Chem.MolFromMolBlock(b, sanitize=False)
        p = svgFromMol(mol)
        with open(output,"w+") as f:
            f.write(p)
    except:
        print("Failed with",name,fn)
        exc_type, exc_value,exc_tb = sys.exc_info()[:3]
        sys.stderr.write(str(exc_type)+'\n')
        sys.stderr.write(str(exc_value)+'\n')
        traceback.print_tb(exc_tb)
        
