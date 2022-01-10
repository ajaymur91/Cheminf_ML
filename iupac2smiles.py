
import pandas as pd
from urllib.request import urlopen
from urllib.parse import quote
def CIRconvert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        return 'FAIL'

datafile = 'iupac'
df = pd.read_csv(datafile,delim_whitespace=True)

identifiers  = df.Iupac

print("Iupac", "Smiles")
for ids in identifiers :
    print(ids, CIRconvert(ids))

# Inspiration
# https://stackoverflow.com/questions/54930121/converting-molecule-name-to-smiles
# https://github.com/openbabel/openbabel/issues/2108
