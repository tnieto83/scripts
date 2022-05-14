import csv
from os import dup
import pandas as pd
import sys


def ssm_duplicates(input):
    df = pd.read_csv(input, sep='\t', names=["text", "clas"])
    results = df.groupby("text")[["clas"]].agg(lambda x: set(x))


  
    results_1 = results.loc[lambda x: x['clas'].str.contains(",")]



    # print(results_1)
    results_1.to_csv("report.csv", sep=';', encoding='utf-8')


ssm_duplicates(sys.argv[1])
