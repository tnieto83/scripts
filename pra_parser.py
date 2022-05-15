
import json
import re
import sys
import csv

def raw(input):
    id=''; ref=''; hyp=''
    jsonData = []
    with open(input, encoding='latin-1') as fp:
        for l in fp:
            if l.startswith('id'):
                id = l.split(':')[1]
                id = re.sub("\(.*\.\/", "", id)
                id = re.sub("\)", ".wav", id)
                id = id.rstrip()
            if l.startswith('REF'):
                ref = l.split(':')[1]
                ref = ref.rstrip()
              
            if l.startswith('HYP'):
                hyp = l.split(':')[1]
                hyp = hyp.rstrip()
                
            if (id != '' and ref != '' and hyp  != '' ):
                jsonData.append({"id":id,"REF":ref,"HYP":hyp})
                id=''; ref=''; hyp=''
                
    
    f = csv.writer(open(input.split(".",)[0] + "_raw.csv", "w+", encoding="latin-1"), delimiter=';')

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["AUDIO","REFERENCE TRANSCRIPTION", "AUTOMATIC TRANSCRIPTION"])
    
    for d in jsonData:
        f.writerow([
                    d["id"],
                    d["REF"],
                    d["HYP"]         
                    ])

def format(input):
    id=''; ref=''; hyp=''
    jsonData = []
    with open(input, encoding='latin-1') as fp:
        for l in fp:
            if l.startswith('id'):
                id = l.split(':')[1]
                id = re.sub("\(.*\.\/", "", id)
                id = re.sub("\)", ".wav", id)
                id = id.rstrip()
            if l.startswith('REF'):
                ref = l.split(':')[1]
                ref = ref.rstrip()
                ref = ref.lower()
                ref = re.sub("\*", "", ref)
                ref = " ".join(ref.split())
                
              
            if l.startswith('HYP'):
                hyp = l.split(':')[1]
                hyp = hyp.rstrip()
                hyp = hyp.lower()
                hyp = re.sub("\*", "", hyp)
                hyp = " ".join(hyp.split())
                
            if (id != '' and ref != '' and hyp  != '' ):
                jsonData.append({"id":id,"REF":ref,"HYP":hyp})
                id=''; ref=''; hyp=''
                
    # print(jsonData)
    f = csv.writer(open(input.split(".",)[0] + "_format.csv", "w+", encoding="latin-1"), delimiter=';')

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["AUDIO","REFERENCE TRANSCRIPTION", "AUTOMATIC TRANSCRIPTION"])
    
    for d in jsonData:
        f.writerow([
                    d["id"],
                    d["REF"],
                    d["HYP"]         
                    ])

def help():
    
    print("python3 pra_parser.py R yourfile.pra >>> yourfile_raw.csv" + "\n\n" + "python3 pra_parser.py F yourfile.pra >>> yourfile_format.csv"  + "\n\n" + "python3 pra_parser.py help >> will display  info"  + "\n")

def main():
    if 'R' == (sys.argv[1]):
        print("Parsing your WER results!")
        raw(sys.argv[2])
    elif 'F' == (sys.argv[1]):
        print("Parsing your WER results!")
        format(sys.argv[2])
    elif "help" == (sys.argv[1]):
        help()
    else:
        print("not valid parameters")
main()
    
