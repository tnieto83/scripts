#!/bin/bash

# Requirements:
# -python3
# -jq-1.6
# Condition the parameter passed in the script call must have a _

function csvTojson { python3 -c "
import csv, json, sys
csv.field_size_limit(sys.maxsize)

csv_file = open('$1', 'r')
field_names = ('name','value')
reader = csv.DictReader(csv_file, field_names)

json_file = open('json_template.txt', 'r')
json_object = json.load(json_file)
json_file.close()

for row in reader:
    json_object['audio']['file_content'] = row['value']
    json_aux = open(row['name']+'.json', 'w+')
    json.dump(json_object, json_aux)
    json_aux.close()
"; }

reports="report-"`date +%d-%m-%Y`".csv"

# inicio addfile
a=$1
if [ ${a%%_*} == "addfile" ];then
   cd "$a";AUX=addfile
   rm $reports 
   for f in *.wav; do base64 $f -w 0 >> $f.csv; done
   for f in *.csv
      do 
         printf "${f%%.*}," | cat - $f > temp && mv temp $f
         $(csvTojson $f)
      done
   rm *.wav.csv
   echo "Go have a coffee ..."
   for f in *.json
      do
         curl \
            -d "@$f" \
            -H "Accept: application/json" \
            -H "Content-Type: application/json" \
            -XPOST -Ss http://192.168.2.139:6789/$AUX \
            | jq --arg audio "${f%%.*}.wav" -r '{audio: $audio} + .|. | [.[] | tostring] | join("; ")' >> $reports
     done
   # rm *.json
# generador de json
elif [ "$a" == "jsongenerator" ];then
   cd "$a"
   for f in *.wav; do base64 $f -w 0 >> $f.csv; done
   for f in *.csv
      do
         printf "${f%%.*}," | cat - $f > temp && mv temp $f
         $(csvTojson $f)
      done
   rm *.wav.csv
# verify
elif [ ${a%%_*} == "verify" ];then
   mkdir "$a"
   cd "$a";AUX=verify
   rm $reports
   cp ../jsongenerator/*.json .
   echo "Go have a coffee ..."
   for f in *.json
      do
         curl \
            -d "@$f" \
            -H "Accept: application/json" \
            -H "Content-Type: application/json" \
            -XPOST -Ss http://192.168.2.139:6789/$AUX \
            | jq --arg audio "${f%%.*}.wav" -r '{audio: $audio} + .|. | [.[] | tostring] | join("; ")' >> $reports
     done
else
   echo "there is no such functionality!"
fi
