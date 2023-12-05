#genetic code translator and comparer

#1. DNA -> RNA -> amin
#DNA -> Amino

#2.
#random mutaciones -> comparar si hay cambios con la original en la amino

#por 1000 y ver porcentaje de cambios en la amino säure


from random import randint

def DNAtoRNA(DNA):
    RNA = ""
    for i in range (len(DNA)):
        if DNA[i]=='A':
            RNA += 'U'
        elif DNA[i]=='T':
            RNA += 'A'
        elif DNA[i]=='C':
            RNA += 'G'
        elif DNA[i]=='G':
            RNA+='C'
    return RNA

def RNAtoAmino(RNA):

#agregar aquí cambiarlo DNA a RNA
    continuar = True
    codon = 0
    while continuar:
        if (RNA[codon]=='A' and RNA[codon+1]=='G' and RNA[codon+2]=='G') or (RNA[codon]=='A' and RNA[codon+1]=='G' and RNA[codon+2]=='A'):
            amino = amino + " Arg" #AGG , AGA
        elif (RNA[codon]=='A' and RNA[codon+1]=='G' and RNA[codon+2]=='C') or (RNA[codon]=='A' and RNA[codon+1]=='G' and RNA[codon+2]=='U'):
            amino = amino + " Ser"
        elif (RNA[codon]=='A' and RNA[codon+1]=='A' and RNA[codon+2]=='G') or (RNA[codon]=='A' and RNA[codon+1]=='A' and RNA[codon+2]=='A'):
            amino = amino + " Lys"
        elif (RNA[codon]=='A' and RNA[codon+1]=='A' and RNA[codon+2]=='C') or (RNA[codon]=='A' and RNA[codon+1]=='A' and RNA[codon+2]=='U'):
            amino = amino + " Asn"
        elif (RNA[codon]=='A' and RNA[codon+1]=='C' and RNA[codon+2]=='G') or (RNA[codon]=='A' and RNA[codon+1]=='G' and RNA[codon+2]=='A') or (RNA[codon]=='A' and RNA[codon+1]=='G' and RNA[codon+2]=='C') or (RNA[codon]=='A' and RNA[codon+1]=='G' and RNA[codon+2]=='U'):
            amino = amino + " Thr"
        elif (RNA[codon]=='A' and RNA[codon+1]=='U' and RNA[codon+2]=='G'): #methionine
            amino = " Met"
        elif (RNA[codon]=='A' and RNA[codon+1]=='U' and RNA[codon+2]=='A') or (RNA[codon]=='A' and RNA[codon+1]=='U' and RNA[codon+2]=='C') or (RNA[codon]=='A' and RNA[codon+1]=='U' and RNA[codon+2]=='U'):
            amino = amino + " Lle"
        elif (RNA[codon]=='C' and RNA[codon+1]=='G' and RNA[codon+2]=='G') or (RNA[codon]=='C' and RNA[codon+1]=='G' and RNA[codon+2]=='A') or (RNA[codon]=='C' and RNA[codon+1]=='G' and RNA[codon+2]=='C') or (RNA[codon]=='C' and RNA[codon+1]=='G' and RNA[codon+2]=='U'):
            amino = amino + " Arg"
        elif (RNA[codon]=='C' and RNA[codon+1]=='A' and RNA[codon+2]=='G') or (RNA[codon]=='C' and RNA[codon+1]=='A' and RNA[codon+2]=='A'):
            amino = amino + " Gln"
        elif (RNA[codon]=='C' and RNA[codon+1]=='A' and RNA[codon+2]=='C') or (RNA[codon]=='C' and RNA[codon+1]=='A' and RNA[codon+2]=='U'):
            amino = amino + " His"
        elif (RNA[codon]=='C' and RNA[codon+1]=='C' and RNA[codon+2]=='G') or (RNA[codon]=='C' and RNA[codon+1]=='C' and RNA[codon+2]=='A') or (RNA[codon]=='C' and RNA[codon+1]=='C' and RNA[codon+2]=='C') or (RNA[codon]=='C' and RNA[codon+1]=='C' and RNA[codon+2]=='U'):
            amino = amino + " Pro"
        elif (RNA[codon]=='C' and RNA[codon+1]=='U' and RNA[codon+2]=='G') or (RNA[codon]=='C' and RNA[codon+1]=='U' and RNA[codon+2]=='A') or (RNA[codon]=='C' and RNA[codon+1]=='U' and RNA[codon+2]=='C') or (RNA[codon]=='C' and RNA[codon+1]=='U' and RNA[codon+2]=='U'):
            amino = amino + " Leu"
        elif (RNA[codon]=='U' and RNA[codon+1]=='G' and RNA[codon+2]=='G'):
            amino = amino + " Trp"
        elif (RNA[codon]=='U' and RNA[codon+1]=='G' and RNA[codon+2]=='A'): #stop
            return amino
            continuar = False
        elif (RNA[codon]=='U' and RNA[codon+1]=='G' and RNA[codon+2]=='C') or (RNA[codon]=='U' and RNA[codon+1]=='G' and RNA[codon+2]=='U'):
            amino = amino + " Cys"
        elif (RNA[codon]=='U' and RNA[codon+1]=='A' and RNA[codon+2]=='G') or (RNA[codon]=='U' and RNA[codon+1]=='A' and RNA[codon+2]=='A'): #stop
            return amino
            continuar = False
        elif (RNA[codon]=='U' and RNA[codon+1]=='A' and RNA[codon+2]=='C') or (RNA[codon]=='U' and RNA[codon+1]=='A' and RNA[codon+2]=='U'):
            amino = amino + " Tyr"
        elif (RNA[codon]=='U' and RNA[codon+1]=='C' and RNA[codon+2]=='G') or (RNA[codon]=='U' and RNA[codon+1]=='C' and RNA[codon+2]=='A') or (RNA[codon]=='U' and RNA[codon+1]=='C' and RNA[codon+2]=='A') or (RNA[codon]=='U' and RNA[codon+1]=='C' and RNA[codon+2]=='U'):
            amino = amino + " Ser"
        elif (RNA[codon]=='U' and RNA[codon+1]=='U' and RNA[codon+2]=='G') or (RNA[codon]=='U' and RNA[codon+1]=='U' and RNA[codon+2]=='A'):
            amino = amino + " Leu"
        elif (RNA[codon]=='U' and RNA[codon+1]=='U' and RNA[codon+2]=='C') or (RNA[codon]=='U' and RNA[codon+1]=='C' and RNA[codon+2]=='U'):
            amino = amino + " Phe"
        elif (RNA[codon]=='G' and RNA[codon+1]=='G' and RNA[codon+2]=='G') or (RNA[codon]=='G' and RNA[codon+1]=='G' and RNA[codon+2]=='A') or (RNA[codon]=='G' and RNA[codon+1]=='G' and RNA[codon+2]=='C') or (RNA[codon]=='G' and RNA[codon+1]=='G' and RNA[codon+2]=='U'):
            amino = amino + " Gly"
        elif (RNA[codon]=='G' and RNA[codon+1]=='A' and RNA[codon+2]=='G') or (RNA[codon]=='G' and RNA[codon+1]=='A' and RNA[codon+2]=='A'):
            amino = amino + " Glu"
        elif (RNA[codon]=='G' and RNA[codon+1]=='A' and RNA[codon+2]=='C') or (RNA[codon]=='G' and RNA[codon+1]=='A' and RNA[codon+2]=='U'):
            amino = amino + " Asp"
        elif (RNA[codon]=='G' and RNA[codon+1]=='C' and RNA[codon+2]=='G') or (RNA[codon]=='G' and RNA[codon+1]=='C' and RNA[codon+2]=='A') or (RNA[codon]=='G' and RNA[codon+1]=='C' and RNA[codon+2]=='A') or (RNA[codon]=='G' and RNA[codon+1]=='C' and RNA[codon+2]=='U'):
            amino = amino + " Ala"
        elif (RNA[codon]=='G' and RNA[codon+1]=='U' and RNA[codon+2]=='G') or (RNA[codon]=='G' and RNA[codon+1]=='U' and RNA[codon+2]=='A') or (RNA[codon]=='G' and RNA[codon+1]=='U' and RNA[codon+2]=='C') or (RNA[codon]=='G' and RNA[codon+1]=='U' and RNA[codon+2]=='U'):
            amino = amino + " Val"
        codon += 3
    return amino

def compare(originalAmino, copyAmino):
    if len(originalAmino) != len(copyAmino):
        return False
    else:
        for i in range (len(originalAmino)):
            if originalAmino[i] != copyAmino[i]:
                return False
        return True

#MAIN translate DNA string to aminosäurenkette

DNA = input("Paste your DNA string here (include Methionine and stop signal): ")

if DNA[0]=='T' and DNA[1]=='A' and DNA[2]=='C':
    if (DNA[len(DNA)-3]=='A' and DNA[len(DNA)-2]=='T' and DNA[len(DNA)-1]=='T') or (DNA[len(DNA)-3]=='A' and DNA[len(DNA)-2]=='T' and DNA[len(DNA)-1]=='C') or (DNA[len(DNA)-3]=='A' and DNA[len(DNA)-2]=='C' and DNA[len(DNA)-1]=='C'):
        if len(DNA)%3 == 0:
            mRNA = DNAtoRNA(DNA)
            print(mRNA)
            Amino = RNAtoAmino(mRNA)
            print(Amino)
        else:
            print("incomplete sequence")
    else:
        print("no stop codon")
else:
    print("No methionine")

#create random single-mutation in DNA string, translating and 

originalDNA = input("Paste your original, non-mutated DNA string here (include Methionine and stop signal): ")

correctInput = False
if DNA[0]=='T' and DNA[1]=='A' and DNA[2]=='C':
    if (DNA[len(DNA)-3]=='A' and DNA[len(DNA)-2]=='T' and DNA[len(DNA)-1]=='T') or (DNA[len(DNA)-3]=='A' and DNA[len(DNA)-2]=='T' and DNA[len(DNA)-1]=='C') or (DNA[len(DNA)-3]=='A' and DNA[len(DNA)-2]=='C' and DNA[len(DNA)-1]=='C'):
        if len(DNA)%3 == 0:
            correctInput = True
        else:
            print("incomplete sequence")
    else:
        print("no stop codon")
else:
    print("no methionine")

if correctInput:
    originalmRNA = DNAtoRNA(DNA)
    originalAmino = RNAtoAmino(originalmRNA)
    numberMutation = 100
    misssenseMutation = 0
    methionineMutation = 0
    stopMutation = 0
    divMutation = 0
    generalMutation = 0


    for i in range (numberMutation):
        copyDNA = ""
        top = len(DNA)
        index = randint(0, top-1)
        mutType = randint(1, 6) #!possible that one base is changed by itself
        if(mutType==1):
            for i in range (len(DNA)):
                if i == index:
                    copyDNA += 'G'
                else:
                    copyDNA += DNA[i]
        elif (mutType==2):
            for i in range (len(DNA)):
                if i == index:
                    copyDNA += 'A'
                else:
                    copyDNA += DNA[i]
        elif (mutType==3):
            for i in range (len(DNA)):
                if i == index:
                    copyDNA += 'T'
                else:
                    copyDNA += DNA[i]
        elif (mutType==4):
            for i in range (len(DNA)):
                if i == index:
                    copyDNA += 'C'
                else:
                    copyDNA += DNA[i]
        elif (mutType==5):
            for i in range (len(DNA)):
                if i != index:
                    copyDNA += DNA[i]
        elif (mutType==6):
            for i in range (len(DNA)):
                nBase = randint(1, 4)
                if i == index:
                    if nBase==1:
                        copyDNA += 'G'
                    elif nBase==2:
                        copyDNA += 'A'
                    elif nBase==3:
                        copyDNA += 'T'
                    elif nBase==4:
                        copyDNA += 'C'
                elif i < index:
                    copyDNA += DNA[i]
                elif i > index:
                    copyDNA += DNA[i-1]

        #print(copyDNA)
        if(copyDNA[0]=='T' and copyDNA[1]=='A' and copyDNA[2]=='C'):
            if len(copyDNA)%3 == 0:
                if (copyDNA[len(copyDNA)-3]=='A' and copyDNA[len(copyDNA)-2]=='T' and copyDNA[len(copyDNA)-1]=='T') or (copyDNA[len(copyDNA)-3]=='A' and copyDNA[len(copyDNA)-2]=='T' and copyDNA[len(copyDNA)-1]=='C') or (copyDNA[len(copyDNA)-3]=='A' and copyDNA[len(copyDNA)-2]=='C' and copyDNA[len(copyDNA)-1]=='C'):
                    copymRNA = DNAtoRNA(copyDNA)
                    copyAmino = RNAtoAmino(copymRNA)
                    print(copyDNA)
                    print(copymRNA)
                    print(copyAmino)
                    if compare(originalAmino, copyAmino):
                        misssenseMutation += 1
                        generalMutation += 1
                else:
                    print(copyDNA)
                    print("no stop codon")
                    print("")
                    misssenseMutation += 1
                    stopMutation += 1
            else:
                print(copyDNA)
                print("no complete sequence")
                print("")
                misssenseMutation += 1
                divMutation += 1
        else:
            print(copyDNA)
            print("no methionine")
            print("")
            misssenseMutation += 1
            methionineMutation += 1

    #print(originalAmino)
    print(numberMutation)                   #print("There have been generated ", numberMutation, " single-mutations")
    print(misssenseMutation)                #print("There were ", misssenseMutation, " conditional Mutations")
    print(methionineMutation)               #print(methionineMutation, " are methionine mutations")
    print(stopMutation)                     #print(stopMutation, " are stop signal mutations")
    print(divMutation)                      #print(divMutation, " are size mutation")
    print(generalMutation)                  #print(generalMutation, " are mutation on aminoacid")
    print(misssenseMutation/numberMutation) #print("product: ", misssenseMutation/numberMutation)
        
else:
    print("Invalid Input")

# TACCACGTGGACTGAGGACTCCTCATT


