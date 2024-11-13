import os, os.path
import pandas as pd

print(f'Total number of files: {len(os.listdir(path="."))}')

df = (pd.DataFrame(
    {
        'name': [x for x in os.listdir(path=".")], 
        'size':[os.path.getsize(x)/1024 for x in os.listdir(path=".")]
     }
     )
     .sort_values(by='size', axis=0, ascending=False)
     ).reset_index(drop=True)

print(f'Top 10 largest files(in KB):')

for i in range(10):
    print(f'{df['name'][i]}: {round(df['size'][i], 2)} KB')