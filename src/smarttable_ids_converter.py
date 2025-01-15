import sys
import pandas as pd

try:
    input_file = sys.argv[1]        
    # Read TXT file as dataframe, by splitting by // ,by ignoring the first line that says Genes of pathway and by using python engine for the specific seperator
    df = pd.read_csv(input_file, header=None, sep=" // ", comment="Genes of pathway", engine='python')

    # Convert columns to rows
    df_t = df.T

    # Write the dataframe to the text file efficiently
    with open(input_file, 'w') as f:
        f.write(
            df_t.to_csv(sep="\t", lineterminator="\n", index=False, doublequote= False, header=False)
        )      

except Exception as e:
    print("ERROR: " f"{str(e)}")
