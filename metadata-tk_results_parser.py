
import csv
import io
import sys
import json
from json.tool import main



def results_parser(input):
  
    x = io.open(input, encoding='latin-1')  
    data = json.load(x)       
    

    f = csv.writer(open(input.split(".",)[0] + ".csv", "w+", encoding="latin-1"), delimiter=';')
    
    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["text","success", "reference", "tags"])
   
    for d in data:
        f.writerow([
                    d["reference"]["text"],
                    d["success"],
                    d["reference"]["tags"],          
                    d["tags"]])



def main():
    results_parser(sys.argv[1])
    

main()