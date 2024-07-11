#!/usr/bin/env python3
import os

#used for createing simple boot.py file for joystick.xl
def createBoot(axvarboot,buttonvarboot, hatsvarboot):
    with open("template/boot.py", "r") as boottemplate, open("output/boot.py", "x" ) as bootnew:
        varaxes = "axesvar = " + str(axvarboot)
        varbuttons = "\nbuttonsvar = " + str(buttonvarboot)
        varhats= "\nhatsvar = " + str(hatsvarboot)
        #used to write multiple lines from a list
        bootnew.writelines([varaxes, varbuttons, varhats])

        for line in boottemplate:    
            bootnew.write(line)
        
'''
#need to ask user which digital and analog pins will be used for inputs
def createCode(axvarcode, buttonvarcode, hatsvarcode, defaultvalues):
    with open("template/code.py", "r") as codetemplate, open("output/code.py", "a") as codenew:
        for line in codetemplate:
            codenew.write(line)

        codenew.write("js = Joystick()\n")
        #inputs = ""
        codenew.write("js.add_input( \n")

        if defaultvalues == "yes":
            customCode(axvarcode, buttonvarcode, hatsvarcode)
        else:
            basicCode(axvarcode, buttonvarcode, hatsvarcode)
        
   #strip the last 2 characters off of the end of the input delceartion, this takes care of getting rid of the new line and the comma
    with open("output/code.py", 'r') as file:
        data = file.read()
    data = data[:-2]
    with open("output/code.py", "w" ) as file:
        file.write(data)


    with open("output/code.py", "a") as codenew:
        codenew.write("\n)\n")
        codenew.write("while True:\n")
        codenew.write("    js.update()\n")

        #print(axvarcode, buttonvarcode, hatsvarcode)
'''

def customCode(one,two,three):
    with open("template/code.py", "r") as codetemplate, open("output/code.py", "a") as codenew:
        for line in codetemplate:
            codenew.write(line)

        codenew.write("js = Joystick()\n")
        #inputs = ""
        codenew.write("js.add_input( \n")
    
        print("create custom controller pinmaping")

            #simple axes input of analog pins
        #formated as such: Axis(board.A2),
        for i in range(one):
            analoginput = "    Axis(board.A" + input(f"please enter analog pin number for axis {i}: ") + "),\n"
            codenew.write(analoginput)

        #simple button input for digital pins
        # formated as such: Button(board.D10),
        for i in range(two):
            buttoninput = "    Button(board.D" + input(f"please enter Digital pin number for button {i}: ") + "),\n"
            codenew.write(buttoninput)

        #Hat input, same as setting up 4 buttons
        #formated as such: Hat(up=board.D2, down=board.D3, left=board.D4, right=board.D7)
        #will need to setup count for this one and remove trailing "," for last line

        for i in range(three):
            #print(i)
            #print(hatsvarcode)
            #this loop itterates though the nubmer of hats and since it is the last set of things to be decared it will write the last item without the trailing "," to finish the tuple
            #initalize string for hat items
            hatinput = "    Hat("
            #pulls in inputs for hat directions except for last value
            hatup = "up=board.D" + input("please enter Digital pin for up direction: ") + ", "
            hatdown = "down=board.D" + input("please enter Digital pin for the down direction: ") + ", "
            hatleft = "left=board.D" + input("please enter Digital pin for left directon: ") + ", "
            #determine if last hat, if it is, drop the trailing ","
            hatright = "right=board.D" + input("please enter Digital pin for the right direction: ") + "),\n"
            hatinput += hatup + hatdown + hatleft + hatright
            codenew.write(hatinput)

   #strip the last 2 characters off of the end of the input delceartion, this takes care of getting rid of the new line and the comma
    with open("output/code.py", 'r') as file:
        data = file.read()
    data = data[:-2]
    with open("output/code.py", "w" ) as file:
        file.write(data)


    with open("output/code.py", "a") as codenew:
        codenew.write("\n)\n")
        codenew.write("while True:\n")
        codenew.write("    js.update()\n")

        #print(axvarcode, buttonvarcode, hatsvarcode)


def basicCode(one, two, three):
    with open("template/code.py", "r") as codetemplate, open("output/code.py", "a") as codenew:
        for line in codetemplate:
            codenew.write(line)

        codenew.write("js = Joystick()\n")
        #inputs = ""
        codenew.write("js.add_input( \n")

        print("create default pin layout")

        for i in range(one):
            analoginput = "    Axis(board.A" + str(i) + "),\n"
            codenew.write(analoginput)
        
        digitalpincount = 0
        for i in range(two):
            buttoninput = "    Button(board.D" + str(i) + "),\n"
            codenew.write(buttoninput)
            digitalpincount += 1

        #Hat input, same as setting up 4 buttons
        #formated as such: Hat(up=board.D2, down=board.D3, left=board.D4, right=board.D7)
        #will need to setup count for this one and remove trailing "," for last line

        for i in range(three):
            #print(i)
            #print(hatsvarcode)
            #this loop itterates though the nubmer of hats and since it is the last set of things to be decared it will write the last item without the trailing "," to finish the tuple
            #initalize string for hat items
            hatinput = "    Hat("
            #pulls in inputs for hat directions except for last value
            hatup = "up=board.D" + str(i + digitalpincount) + ", "
            digitalpincount += 1
            hatdown = "down=board.D" + str(i + digitalpincount) + ", "
            digitalpincount += 1
            hatleft = "left=board.D" + str(i + digitalpincount) + ", "
            digitalpincount += 1
            #determine if last hat, if it is, drop the trailing ","
            hatright = "right=board.D" + str(i + digitalpincount) + "),\n"
            digitalpincount += 1
            hatinput += hatup + hatdown + hatleft + hatright
            codenew.write(hatinput)
   
   #strip the last 2 characters off of the end of the input delceartion, this takes care of getting rid of the new line and the comma
    with open("output/code.py", 'r') as file:
        data = file.read()
    data = data[:-2]
    with open("output/code.py", "w" ) as file:
        file.write(data)


    with open("output/code.py", "a") as codenew:
        codenew.write("\n)\n")
        codenew.write("while True:\n")
        codenew.write("    js.update()\n")

        #print(axvarcode, buttonvarcode, hatsvarcode)



def main():
    #used to overwrite boot.py if it already exists
    while os.path.exists("output/boot.py"):
        os.remove("output/boot.py")
    while os.path.exists("output/code.py"):
        os.remove("output/code.py")

    #pull down user input on how many of each input will be used
    axinput = int(input("input a number of axes between 0 and 8: "))
    buttoninput = int(input("input a number of buttons between 0 and 128: "))
    hatinput = int(input("input a number of hats between 0 and 4: "))
    defaultvalues = input("use default values? yes or no: ")

    ##create files
    #create boot.py
    createBoot(axinput, buttoninput, hatinput)
    #create code.py
    #if user enters anything aside from no it will use default values as described above
    #if user enters no they will be prompted to add custom pin mappins for all pins needed for controller
    if defaultvalues == "no":
        customCode(axinput, buttoninput, hatinput)
    else:
        basicCode(axinput, buttoninput, hatinput)






main()