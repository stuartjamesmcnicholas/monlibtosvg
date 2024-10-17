import sys,os
from rdkit import Chem
from mol2svg import svgFromMol

strings = []

with open("smiles.db") as f:
   strings = f.readlines()

for s in strings:
    name,smiles = s.strip().split()
    smiles = smiles.strip('"').strip("'")
    output = os.path.join(name[0],name+".svg")
    print(output)
    try:
        mol = Chem.MolFromSmiles(smiles, sanitize=False)
        p = svgFromMol(mol)
        with open(output,"w+") as f:
            f.write(p)
    except:
        print("Failed with",name,smiles)
        sys.exit()
