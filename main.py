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
        

#need to ask user which digital and analog pins will be used for inputs
def createCode(axvarcode, buttonvarcode, hatsvarcode):
    with open("template/code.py", "r") as codetemplate, open("output/code.py", "a") as codenew:
        for line in codetemplate:
            codenew.write(line)

        codenew.write("js = Joystick()\n")
        #inputs = ""
        codenew.write("js.add_input( \n")

        #simple axes input of analog pins
        #formated as such: Axis(board.A2),
        for i in range(axvarcode):
            analoginput = "    Axis(board.A" + input(f"please enter analog pin number for axis {i}: ") + "),\n"
            codenew.write(analoginput)

        #simple button input for digital pins
        # formated as such: Button(board.D10),
        for i in range(buttonvarcode):
            buttoninput = "    Button(board.D" + input(f"please enter Digital pin number for button {i}: ") + "),\n"
            codenew.write(buttoninput)

        #Hat input, same as setting up 4 buttons
        #formated as such: Hat(up=board.D2, down=board.D3, left=board.D4, right=board.D7)
        #will need to setup count for this one and remove trailing "," for last line

        for i in range(hatsvarcode):
                #print(i)
                #print(hatsvarcode)
                #this loop itterates though the nubmer of hats and since it is the last set of things to be decared it will write the last item without the trailing "," to finish the tuple
                if i != hatsvarcode -1 :
                    #initalize string for hat items
                    hatinput = "    Hat("
                    #pulls in inputs for hat directions
                    hatup = "up=board.D" + input("please enter Digital pin for up direction: ") + ", "
                    hatdown = "down=board.D" + input("please enter Digital pin for the down direction: ") + ", "
                    hatleft = "left=board.D" + input("please enter Digital pin for left directon: ") + ", "
                    hatright = "right=board.D" + input("please enter Digital pin for the right direction: ") + "),\n"
                    hatinput += hatup + hatdown + hatleft + hatright
                    # codenew.write(hatinput)
                else:
                    #initalize string for hat items
                    hatinput = "    Hat("
                    #pulls in inputs for hat directions
                    hatup = "up=board.D" + input("please enter Digital pin for up direction: ") + ", "
                    hatdown = "down=board.D" + input("please enter Digital pin for the down direction: ") + ", "
                    hatleft = "left=board.D" + input("please enter Digital pin for left directon: ") + ", "
                    hatright = "right=board.D" + input("please enter Digital pin for the right direction: ") + ")\n"
                    hatinput += hatup + hatdown + hatleft + hatright
                    # codenew.write(hatinput)
                codenew.write(hatinput)


            
        #print(inputs)

        
        #codenew.write(inputs[:-2])
        codenew.write(")\n")
        codenew.write("while True:\n")
        codenew.write("    js.update()\n")

        print(axvarcode, buttonvarcode, hatsvarcode)

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

    ##create files
    #create boot.py
    createBoot(axinput, buttoninput, hatinput)
    #create code.py
    createCode(axinput, buttoninput, hatinput)






main()