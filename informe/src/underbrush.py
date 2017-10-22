import numpy as np
import pandas as pd
infile ="/Users/josepplloo/Documents/scripts/xab_clean.csv"
df = pd.read_csv(infile, header = 0)
for aux in df.DxPrincipal.unique():
    print aux
    bee = df[df['DxPrincipal']==aux]
    bee.to_csv("/Users/josepplloo/Documents/scripts/RIPS_2013_1/2splitDx/%s.csv" %aux,index=False)




#debo de filtar la data para solo un diagnostico
