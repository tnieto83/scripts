import csv
import io
from playsound import playsound
import sys

def oq_review_transcriptions(corpus):
      
        dict_from_csv = {}
        flag = True


        file = corpus.split(".",)[0] + "_reviewed.csv"
        report = open(file, 'w')
        report.write("AUDIO,STATUS,ORIGINAL TRANSCRIPTION,CORRECTED TRANSCRIPTION" + "\n")


        with open(corpus, mode='r', encoding='latin-1') as inp:
            reader = csv.reader(inp)
            dict = {rows[0]:rows[1] for rows in reader}

        for (key, value) in dict.items():
            audio = str(key)
            print(" >>>>>  You are listening " + audio +  "\n")
            print(value)
            playsound(audio)
            
            try: 
        
                answer= int(input("If correct, type 0. If not correct, type 1 >> "))

                if answer == 0:
                    report = open(file, 'a')
                    report.write(str(audio)+ "," + "TRUE"+ "," + str(value) + "\n")

                #pide que metas la transcrcipcion correcta y se reproduce de nuevo el audio    
                elif answer == 1: 
                    audio = str(key)
                    print(" >>>>>  You are listening " + audio +  "\n")
                    print(value)
                    playsound(audio)
                    answer_2 = (input("Enter the right transcription >>> "))
                    report = open(file, 'a')
                    report.write(str(audio)+ "," + "FALSE" + "," + str(value) + "," + str(answer_2) + "\n")

                #si la respuesta es un numero distinto a 1 o 0, se reproduce de nuevo el audio, se vuelve a empezar
                else:  
                    print("\n" + "Answer must be 0 or 1, please try again")
                    audio = str(key)
                    print(" >>>>>  You are listening " + audio +  "\n")
                    print(value)
                    playsound(audio)
                    answer= int(input("\n" + "If correct, type 0. If not correct, type 1 >> "))
                    if answer == 0:
                        report = open(file, 'a')
                        report.write(str(audio)+ "," + "TRUE"+ "," + str(value) + "\n")
                    elif answer == 1: 
                        answer_2 = (input("Enter the right transcription >>> "))
                        report = open(file, 'a')
                        report.write(str(audio)+ "," + "FALSE" + "," + str(value) + "," + str(answer_2) + "\n")
                    continue
            
            except ValueError:
                print("\n" + "Answer must be 0 or 1, please try again")        
                audio = str(key)
                print(" >>>>>  You are listening " + audio +  "\n")
                print(value)
                playsound(audio)
                answer= int(input("\n" + "If correct, type 0. If not correct, type 1 >> "))
                if answer == 0:
                    report = open(file, 'a')
                    report.write(str(audio)+ "," + "TRUE"+ "," + str(value) + "\n")

                elif answer == 1: 
                    answer_2 = (input("Enter the right transcription >>> "))
                    report = open(file, 'a')
                    report.write(str(audio)+ "," + "FALSE" + "," + str(value) + "," + str(answer_2) + "\n")
                continue
                    

    
def main():
    oq_review_transcriptions(sys.argv[1])
    

main()





