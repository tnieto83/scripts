import json
import re
import sys

    #Abre un fichero

def reporting(input):
    corpus = open(input, encoding='latin-1')
    corpus = (corpus.read())

    print("Creando reporte ..... ")
    ########################### REPORTE ############################

    #CREA UNA LISTA DE TAGS TIPO <AAA>
    tags = re.findall("\<\w+\>", corpus)
    file = input.split(".",)[0] + "_report.csv"
    report = open(file, 'w')
    report.write("LIST OF TAGS" + "\n")
    for item in tags:
        report.write(item + "\n")
    report.close()
    

    # CREAR LISTADO DE NÚMEROS 
    digits = re.findall("[0-9]{1,}", corpus)
    digits_1 = set(digits)
    digits_2 = list(digits_1)
    digits_2.sort(reverse = True)
    fichero = open(file, 'a')
    fichero.write("\n\n" + "LIST OF DIGITS" + "\n")
    for item in digits_2:
        fichero.write(item + "\n")
    fichero.close()

    # #CREA UNA LISTA DE SIGLAS
    acronyms = re.findall("\w[A-Z]{1,}", corpus) #>>>>>>>>>>>>>unicamente las siglas
    #acronyms = re.findall("[A-Z]{1,}\s\(.*\)", corpus) #>>>>>>>>>>>siglas + expansión entre paréntesis
    acronyms_list_1 = set(acronyms)
    acronyms_list_2 = list(acronyms_list_1)
    acronyms_list_2.sort(reverse = False)
    fichero = open(file, 'a')
    fichero.write("\n\n" + "LIST OF ACRONYMS" + "\n")
    for item in acronyms_list_2:
        fichero.write(item + "\n")
    fichero.close()

    #CREA UNA LISTA DE PALABRAS EN MAYÚSCULA
    capitalized = re.findall("[A-Z]{1}[a-záéíóúñ]{1,}", corpus)
    capitalized_list_1 = set(capitalized)
    capitalized_list_2 = list(capitalized_list_1)
    capitalized_list_2.sort(reverse = False)
    fichero = open(file, 'a')
    fichero.write("\n\n" + "LIST OF CAPITALIZED WORDS" + "\n")
    for item in capitalized_list_2:
        fichero.write(item + "\n")
    fichero.close()

   
    #CREA UNA LISTA DE SIMBOLOS
    symbols = re.findall("[^a-zA-ZáéíóúüñÁÉÍÓÚ\d\s:]", corpus)
    symbols_1 = set(symbols)
    report = open(file, 'a')
    report.write("\n\n" + "LIST OF SYMBOLS" + "\n")
    for item in symbols_1:
        report.write(item + "\n")
    report.close()


    # ##########################################LIMPIEZA#############################################################3

def cleaner(input):
    
    
    print("Limpiando corpus..... ")

    # EXPANDE LOS NÚMEROS DEL 1 AL 5000
    with open("dic_numeros.json", "r") as dict_file:
        d = json.load(dict_file)
    dict_file.close()

   
    list_file = open(input, "rt")
    f = list_file.read()
    list_file.close()

    digits = re.findall("[0-9]{1,}", f)

    file_2 = input.split(".",)[0] + "_cleaned.csv"
    corpus = open(file_2, "w")
    for (key, value) in d.items():
            for num in digits:
                if num == key:
                    f = f.replace(num,value)

    #EXPANDE LAS SIGLAS
    with open("dic_siglas.json", "r") as dict_file_siglas:
        e = json.load(dict_file_siglas)
    dict_file_siglas.close()

    acronyms = re.findall("\w[A-Z]{1,}", f)

    corpus = open(file_2, "w")
    for (key, value) in e.items():
            for acronym in acronyms:
                if acronym == key:
                    f = f.replace(acronym,value)

    
    #Elimina etiquetas tipo <AAA>
    b = re.sub("\<\w+\>", "", f)


    # REEMPLAZA LOS SIMBOLOS POR UN ESPACIO
    c = re.sub("[^a-zA-ZñüáéíóúñÁÉÍÓÚ\d\s:]", " ", b)
  
    #Elimina los dobles espacios  >>>>>>>>>>> hay que iterarlo para que no queden
    d = re.sub("  " , " ", c) 
   
  

    
    # #Genera un nuevo archivo con el corpus limpio
    fichero = open(file_2, 'w')
    fichero.write(d)
    fichero.close()

    ##########################################


def main():
    if 'reporting' == (sys.argv[1]): 
        reporting(sys.argv[2])
    if 'cleaner' == sys.argv[1]:
        cleaner(sys.argv[2])
    else:
        print("not valid parameters")
main()

