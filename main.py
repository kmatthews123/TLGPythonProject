#!/usr/bin/env python3
import os

#used for createing boot.py file for joystick.xl
def createBoot(axvarboot,buttonvarboot, hatsvarboot):
    with open("template/boot.py", "r") as boottemplate, open("output/boot.py", "x" ) as bootnew:
        varaxes = "\naxesvar = " + str(axvarboot)
        varbuttons = "\nbuttonsvar = " + str(buttonvarboot)
        varhats= "\nhatsvar = " + str(hatsvarboot)
        bootnew.writelines([varaxes, varbuttons, varhats])

        for line in boottemplate:    
            bootnew.write(line)
        

#need to ask user which digital and analog pins will be used for inputs
def createCode(axvarcode, buttonvarcode, hatsvarcode):
    with open("template/code.py", "r") as codetemplate, open("output/code.py", "a") as codenew:
        for line in codetemplate:
            codenew.write(line)

        codenew.write("js = Joystick()\n")
        inputs = ""

        #simple axes input of analog pins
        #formated as such: Axis(board.A2),
        for i in range(axvarcode):
            analoginput = "Axes.board(" + input(f"please enter analog pin for axis {i}: ") + "), "
            inputs += analoginput

        #simple button input for digital pins
        # formated as such: Button(board.D10),

        for i in range(buttonvarcode):
            buttoninput = "Button.board(" + input(f"please enter Digital pin for button {i}: ") + "), "
            inputs += buttoninput

        #Hat input, same as setting up 4 buttons
        #formated as such: Hat(up=board.D2, down=board.D3, left=board.D4, right=board.D7)

        for i in range(hatsvarcode):
            #initalize string for hat items
            hatinput = "Hat("
            #pulls in inputs for hat directions
            hatup = "up=board." + input("please enter Digital pin for up direction: ") + ", "
            hatdown = "down=board." + input("please enter Digital pin for the down direction: ") + ", "
            hatleft = "left=board." + input("please enter Digital pin for left directon: ") + ", "
            hatright = "right=board." + input("please enter Digital pin for the right direction: ") + "), "
            
            hatinput += hatup + hatdown + hatleft + hatright

            inputs += hatinput
        
        print(inputs)

        codenew.write("js.add_input(")
        codenew.write(inputs[:-2])
        codenew.write(")")

        print(axvarcode, buttonvarcode, hatsvarcode)


        '''

        #need to append the below to output/code.py

        js = Joystick()

        js.add_input(
            Button(board.D9),
            Button(board.D10),
            Axis(board.A2),
            Axis(board.A3),
            Hat(up=board.D2, down=board.D3, left=board.D4, right=board.D7)
            #no comma after last item
        )

        while True:
            js.update()
                
        '''
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