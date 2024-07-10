#!/usr/bin/env python3
import os

def createBoot(axvar,buttonvar, hatsvar):
    with open("template/boot.py", "r") as boottemplate, open("output/boot.py", "x" ) as bootnew:
        varaxes = "\naxesvar = " + axvar
        varbuttons = "\nbuttonsvar = " + buttonvar
        varhats= "\nhatsvar = " + hatsvar
        bootnew.writelines([varaxes, varbuttons, varhats])

        for line in boottemplate:    
            bootnew.write(line)
        



#def createCode():

def main():
    while os.path.exists("output/boot.py"):
        os.remove("output/boot.py")

    axinput = input("input a number of axes between 0 and 8: ")
    buttoninput = input("input a number of buttons between 0 and 128: ")
    hatinput = input("input a number of hats between 0 and 8: ")
    # open/create code.py and boot.py files
    # have user enter their board files
    createBoot(axinput, buttoninput, hatinput)






main()