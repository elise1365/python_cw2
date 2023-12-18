# frontend
from backend import SmartHome, SmartLight, SmartPlug
from tkinter import *

smartHome = SmartHome()
mainWin = Tk()

# challenge - total number of devices on at one time
totalOn = 0

def setUpHome():
    '''Creates the five devices specified in the coursework table 1, adds each device to the smartHome variable'''
    sp1 = SmartPlug()
    sp2 = SmartPlug()
    sp3 = SmartPlug()
    c1 = SmartLight()
    c2 = SmartLight()
    smartHome.addDevice(sp1)
    smartHome.addDevice(sp2)
    smartHome.addDevice(sp3)
    smartHome.addDevice(c1)
    smartHome.addDevice(c2)

def gui():
    '''This creates the GUI dispayed to the user and calls the createWidgets() function'''
    numOfDevices = len(smartHome.devices)
    width = 600
    height = 70 * numOfDevices
    mainWin.title('Smart Home')
    mainWin.geometry('{}x{}'.format(width, height))
    createRow(numOfDevices + 4, mainWin)
    createColumn(4, mainWin)
    createWidgets()
    
def createWidgets():
    '''Creates the widgets that are displayed on the gui
    Creates 2 labels, one for the main title that says smart home, and one for the total number of devices on
    Creates 7 buttons, 5 toggle buttons and one to turn all devices on and another to turn all devices off
    Creates 5 text boxes that display the details of each device'''
    # Creates 2 buttons, an on button and an off button
    onButton = Button(mainWin, text = 'Turn all off', command = turnAllDevicesOff)
    onButton.grid(row = 0, column = 0, columnspan = 4)
    offButton = Button(mainWin, text = 'Turn all on', command = turnAllDevicesOn)
    offButton.grid(row = 1, column = 0, columnspan = 4)

    numOfDevices = len(smartHome.devices)
    # creates 5 text widgets, and displays the details of a device in each widget
    for i in range(numOfDevices):
        createTextWidget(i)
    
    # creates 5 toggle buttons
    for index in range(numOfDevices):
        # i=index means that the toggleThis function can be called without passing a parameter
        def toggleThis(i=index):
            '''toggleThis is called by the toggle buttons. This function is created because the toggle function must pass an index'''
            toggle(i)
        btn = Button(mainWin, text = 'Toggle this', command = toggleThis)
        btn.grid(row = index + 3, column = 1)

    # Challenge - Creates 5 buttons that allow each device to be modified
    for index in range(numOfDevices):
        # i=index means that the modifyThis function can be called without passing a parameter
        def modifyThis(i=index):
            '''modifyThis function calles modifyDevice function and allows it to pass an index'''
            modifyDevice(i)
        btn = Button(mainWin, text = 'Modify device', command = modifyThis)
        btn.grid(row = index + 3, column = 2)

    # Challenge - Creates a label that prints the total number of devices on
    totalOnLabel()

    # Challenge - add smart plug button
    addPlugBtn = Button(mainWin, text = 'Add smart plug', command = addPlug)
    addPlugBtn.grid(row = numOfDevices + 5, column = 0, columnspan = 3)
    # add smart light button
    addLightBtn = Button(mainWin, text = 'Add smart light', command = addLight)
    addLightBtn.grid(row = numOfDevices + 6, column = 0, columnspan = 3)

    # Challenge - remove device button
    for index in range(numOfDevices):
        # i=index means that the removeThis function can be called without passing a parameter
        def removeThis(i=index):
            '''removeThis function calles removeDevice function and allows it to pass an index'''
            removeDev(i)
        removeDevBtn = Button(mainWin, text = 'Remove this device', command = removeThis)
        removeDevBtn.grid(row = index + 3, column = 3)         

def removeDev(index):
    '''This function removes a device from the smartHome list'''
    # removeDevice method was created specfically for the challenge
    smartHome.removeDevice(index)
    
    global totalOn
    if totalOn == 0:
        pass
    else:
        totalOn -= 1

    # removes all the widgets on the window
    for widgets in mainWin.winfo_children():
        widgets.destroy()

    # makes the entire window, creates all the widgets again but this time the removed device is gone
    gui()

def addLight():
    '''called when the add smart light button is clicked. Creates a new smart light device and adds it to the smartHome variable'''
    devName = SmartLight()
    smartHome.addDevice(devName)

    # deletes all the widgets in the window
    for widgets in mainWin.winfo_children():
        widgets.destroy()
    # makes all the widgets again so that the new device added is also added underneath already existing devices
    gui()

def addPlug():
    '''adds a new smart plug device'''
    devName = SmartPlug()
    smartHome.addDevice(devName)

    # deletes all the widgets in the window
    for widgets in mainWin.winfo_children():
        widgets.destroy()
    # makes all the widgets again so that the new device added is also added underneath already existing devices
    gui()

def createRow(index, window):
    '''Creates a number of rows in a specified window. Number of rows specified by index'''
    for i in range(index):
        window.rowconfigure(index = i, weight = 1)

def createColumn(index, window):
    '''Creates a number of columns in a specified window. Number of columns specified by index'''
    for i in range(index):
        window.columnconfigure(index = i, weight = 1)

def createTextWidget(index):
    '''Creates a text widget which prints out the details of a device'''
    txt = Text(mainWin, height = 1, width = 30)
    txt.insert('1.0', smartHome.getDeviceAt(index))
    # i + 3 because the first text widget is in the 3rd row, then the 4th etc
    txt.grid(row = index + 3, column = 0)

def modifyDevice(index):
    '''This is the command called when the modify device button is clicked
    It creates a GUI that allows the user to toggle the device or change the brightness/consumption rate'''
    # creates the gui
    modifyWin = Tk()
    width = 200
    height = 200
    modifyWin.geometry('{}x{}'.format(width, height))
    mainWin.title('Modify device')
    # 3 rows, one for the toggle button, one for the textbox to input a value and one for the button to enter a value from the textbox
    createRow(3, modifyWin)
    # only one column is needed
    createColumn(1, modifyWin)

    # makes the toggle button
    def toggleThis():
        '''Because the toggle function must pass an index, toggleThis function is created to be called by the toggleButton command'''
        toggle(index)
    toggleButton = Button(modifyWin, text = 'Toggle light', command = toggleThis)
    toggleButton.grid(row = 0, column = 0)

    # Determines whether the device that is being modified is a smart plug or light
    item = smartHome.getDeviceAt(index)
    if 'Light' in str(item):
        itemType = 'light'
        limit = 100
    else:
        itemType = 'plug'
        limit = 150

    def getInput():
        '''called when the update button is clicked, takes whatever was entered into the textbox and updates either the consumption rate or brightness level'''
        # gets what has been typed into the textbox
        value = valueTxt.get('1.0', 'end-1c')
        value = int(value)
        # Checks whether the value entered by the user is higher than the limit for the consumption rate/brightness
        if value > limit:
            print('You cannot enter a value higher than {}'.format(limit))
        else:
            # If the device is a light, then the brightness is updated using the value from the text widget
            if itemType == 'light':
                item.setBrightness(value)
                txt = Text(mainWin, height = 1, width = 30)
                txt.insert('1.0', smartHome.getDeviceAt(index))
                txt.grid(row = index + 3, column = 0)
            else:
                # If the device isn't a light, it must be a smart plug so the consumption rate is updated
                item.setConsumptionRate(value)
                txt = Text(mainWin, height = 1, width = 30)
                txt.insert('1.0', smartHome.getDeviceAt(index))
                txt.grid(row = index + 3, column = 0)

    # Creates the text widget where the user will enter a value
    valueTxt = Text(modifyWin, height = 1, width = 30)
    valueTxt.insert('1.0', ' ')
    valueTxt.grid(row = 1, column = 0)

    # Creates the update button, getInput is called when the button is clicked
    btn = Button(modifyWin, text = 'Update', command = getInput)
    btn.grid(row = 2, column = 0)    
    
    # Stops the window lcosing until the user clicks the x
    modifyWin.mainloop()

def toggle(index):
    '''This function is used by the toggle buttons, passes the row number of the button, then toggles the device and reprints the label of that device.
    totalOn changes depending on whether the device was switched on or off'''
    smartHome.toggleSwitch(index)
    createTextWidget(index)

    # Challenge - the total devices on changes depending on whether the device toggled is now on or off
    global totalOn
    # determine if the device is on or off
    numOfDevices = len(smartHome.devices)
    item = smartHome.getDeviceAt(index)
    item = item.getSwitchedOn()
    if item == True:
        totalOn +=  1
    else:
        totalOn -=  1
    totalOnLabel()

def turnAllDevicesOn():
    '''Turns all devices on, sets total devices on as 5'''
    global totalOn
    smartHome.turnOnAll()
    for i in range(len(smartHome.devices)):
        createTextWidget(i)
    
    # challenge - sets total devices on as 5
    numOfDevices = len(smartHome.devices)
    totalOn = numOfDevices
    totalOnLabel()

def turnAllDevicesOff():
    '''This function turns all the devices in the smart home off, setting the total devices on as 0'''
    global totalOn
    smartHome.turnOffAll()
    for i in range(len(smartHome.devices)):
        createTextWidget(i)

    # Challenge - sets total on as 0
    totalOn = 0
    totalOnLabel()

def totalOnLabel():
    '''displays a label that shows how many devices are on'''
    global totalOn
    numOfDevices = len(smartHome.devices)
    totalDevicesOn = Label(mainWin, text = 'Number of devices on = {}'.format(totalOn), font = 'bold')
    totalDevicesOn.grid(row = numOfDevices+3, column = 0, columnspan = 2)

def main():
    '''main function, calls the setUpHome() function and the function that sets up the gui. Win.mainloop() stops the window from closing until the user chooses to exit'''
    setUpHome()
    gui()
    mainWin.mainloop()

main()