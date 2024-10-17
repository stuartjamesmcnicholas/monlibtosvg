How I made an SVG for every monomer library entry.

mkdir RCSB_SDF 0 1 2 3 4 5 6 7 8 9 A B C ... etc. This should probably be done 

for i in ~/Moorhen/checkout/monomers/*/*.cif; do grep " SMILES " $i| head -1| awk '{print $1" "$NF}'; done > smiles.db

Fixed quite a few problems in smiles.db by hand, in many cases the first SMILES entry is not valid.

for i in ~/Moorhen/checkout/monomers/*/*.cif; do if [ `grep -c " SMILES " $i` -eq 0 ]; then echo $i; fi; done > nosmiles.txt

python3 ./get_rcsb_sdf.py

cd RCSB_SDF

for i in *.sdf; do ~/openbabel_inst/bin/obabel $i -o smi -O ${i%.sdf}.smi; done

for i in *.smi ; do awk '{print $2" "$1}' $i; done >> ../smiles.db

cd ..

ccp4-python test_mol2svg.py

python3 build_html.py
