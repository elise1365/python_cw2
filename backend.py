# backend

# These 2 classes are the original classes created for task 1 and 2. They have been commented out as one of the challenge features asks to use inheritence to shorten code.
# class SmartPlug:
#     '''
#     A smart plug class that can be turned on or off and has a consumption rate setting
#     '''
#     def __init__(self):
#         '''
#         Creates a switchedOn variable and a consumption rate variable
#         '''
#         self.switchedOn = False
#         self.consumptionRate = 0

#     def toggleSwitch(self):
#         '''
#         Sets the switchedOn variable either on or off
#         '''
#         self.switchedOn = not self.switchedOn

#     def getSwitchedOn(self):
#         '''
#         Returns the value of the switchedOn variable
#         '''
#         return self.switchedOn

#     def setSwitchedOn(self):
#         '''
#         Sets the switchedOn variable to true
#         '''
#         self.switchedOn = True

#     def setSwitchedOff(self):
#         '''
#         Sets the switchedOn variable to false/off
#         '''
#         self.switchedOn = False

#     def getConsumptionRate(self):
#         '''
#         Returns the consumption rate of the device
#         '''
#         return self.consumptionRate

#     def setConsumptionRate(self, consumptionRate):
#         '''
#         Sets the consumption rate to whatever is passed when this method is called
#         '''
#         self.consumptionRate = consumptionRate

#     def __str__(self):
#         '''
#         Returns the details of a device as a string
#         '''
#         onOrOff = ''
#         if self.switchedOn == True:
#             onOrOff = 'on'
#         else:
#             onOrOff = 'off'
#         output = 'Plug: {}, {} consumption'.format(onOrOff, self.consumptionRate)
#         return output

# class SmartLight:
#     '''
#     A smart light class that can be turned on or off and also has a brightness setting
#     '''
#     def __init__(self):
#         '''
#         Creates the brightness and switchedOn variables
#         '''
#         self.switchedOn = False
#         self.brightness = 0

#     def toggleSwitch(self):
#         '''
#         Turns the switch either on or off.
#         '''
#         self.switchedOn = not self.switchedOn

#     def getSwitchedOn(self):
#         '''
#         Accessor method that returns the value of the switchedOn variable
#         '''
#         return self.switchedOn
    
#     def setSwitchedOn(self):
#         '''
#         Mutator method that turns the light on
#         '''
#         self.switchedOn = True

#     def setSwitchedOff(self):
#         '''
#         Mutator method that switches the light off
#         '''
#         self.switchedOn = False

#     def getBrightness(self):
#         '''
#         Accessor method that returns the brightness of a smart light device
#         '''
#         return self.brightness

#     def setBrightness(self, brightness):
#         '''
#         Sets the device brightness of the light
#         Mutator method
#         '''
#         self.brightness = brightness

#     def __str__(self):
#         '''
#         Returns a string of the details of the smart light device
#         '''
#         onOrOff = ''
#         if self.switchedOn == True:
#             onOrOff = 'on'
#         else:
#             onOrOff = 'off'
#         output = 'Light: {}, {} brightness'.format(onOrOff, self.brightness)
#         return output

# Challenge
class SmartDevice:
    '''Parent class that creates a swithedOn variable. 
    It also has mutator and accessor methods for the switchedOn variable and toggles this variable as on or off'''
    def __init__(self):
        '''initializes a device created using the SmartDevice class'''
        self.switchedOn = False

    def toggleSwitch(self):
        '''sets switchedOn to either on or off depending on the variables current state'''
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        '''returns the value of the switchedOn variable'''
        return self.switchedOn

    def setSwitchedOn(self):
        '''sets the switchedOn variable as True'''
        self.switchedOn = True

    def setSwitchedOff(self):
        '''sets the switchedOn variable as False'''
        self.switchedOn = False

class SmartPlug(SmartDevice):
    '''Child class that inherits from SmartDevice parent class.
    SmartPlug also creates a consumptionRate variable and has mutator and accessor methods for this
    Also creates a __str__ method for printing details of a SmartPlug device'''
    def __init__(self):
        '''initializes a device created using the SmartPlug class, inherits from the SmartDevice class'''
        super().__init__()
        self.consumptionRate = 0

    def getConsumptionRate(self):
        '''Returns the consumption rate of the device'''
        return self.consumptionRate

    def setConsumptionRate(self, consumptionRate):
        '''Sets the consumption rate to whatever is passed when this method is called'''
        if consumptionRate > 150:
            print('The consumption rate cannot be set above 150')
        else:
            self.consumptionRate = consumptionRate

    def __str__(self):
        '''Returns the details of a device as a string'''
        onOrOff = ''
        if self.switchedOn == True:
            onOrOff = 'on'
        else:
            onOrOff = 'off'
        output = 'Plug: {}, {} consumption'.format(onOrOff, self.consumptionRate)
        return output

class SmartLight(SmartDevice):
    '''A child class that inherits from SmartDevice parent class
    Creates a variable called brightness, as well as the mutator and accessor methods for brightness
    Creates a __str__ method for printing details of a SmartLight device'''
    def __init__(self):
        '''initializes a device created using the SmartLight class, inherits from the SmartDevice class'''
        super().__init__()
        self.brightness = 0
    
    def getBrightness(self):
        '''Accessor method that returns the brightness of a smart light device'''
        return self.brightness

    def setBrightness(self, brightness):
        '''Sets the device brightness of the light'''
        if brightness > 100:
            print('Brightness cannot be higher than 100, try again!')
        else:
            self.brightness = brightness

    def __str__(self):
        '''Returns a string of the details of the smart light device'''
        onOrOff = ''
        if self.switchedOn == True:
            onOrOff = 'on'
        else:
            onOrOff = 'off'
        output = 'Light: {}, {} brightness'.format(onOrOff, self.brightness)
        return output

class SmartHome:
    '''Creates a list of devices in a smart home'''
    def __init__(self):
        '''Creates a list for all the devices to be stored in'''
        self.devices = []

    def getDevices(self):
        '''Returns all the devices in the list'''
        output = ''
        for i in range(len(self.devices)):
            output += str(self.getDeviceAt(i)) + '\n'
        return output

    def getDeviceAt(self, index):
        '''Returns the device at the index in the list'''
        return self.devices[index]

    def addDevice(self, object):
        '''Adds a device to the list of devices'''
        self.devices.append(object)

    def toggleSwitch(self, index):
        '''Takes an index as a parameter and toggles the device in the list that corresponds to the index'''
        item = self.devices[index]
        item.switchedOn = not item.switchedOn

    def turnOnAll(self):
        '''Turns all the devices in the class on'''
        for i in range(len(self.devices)):
            item = self.devices[i]
            item.switchedOn = True

    def turnOffAll(self):
        '''Turns all the devices in the class off'''
        for i in range(len(self.devices)):
            item = self.devices[i]
            item.switchedOn = False

    # Challenge
    def removeDevice(self, index):
        '''Removes a device from the smart home list'''
        self.devices.pop(index)

    def __str__(self):
        '''Outputs all the items in the smart home class'''
        output = ''
        for i in range(len(self.devices)):
            item = self.devices[i]
            output += str(item) + '\n'
        return output

def testSmartPlug():
    '''Tests the smart plug class '''
    smartPlug1 = SmartPlug()
    smartPlug1.toggleSwitch()
    print(SmartPlug.getSwitchedOn(smartPlug1))
    print(SmartPlug.getConsumptionRate(smartPlug1))
    smartPlug1.setConsumptionRate(10)
    print(SmartPlug.getConsumptionRate(smartPlug1))
    print(smartPlug1)

def testDevice():
    '''Tests the smart light class'''
    device1 = SmartLight()
    device1.toggleSwitch()
    print(SmartLight.getSwitchedOn(device1))
    print(SmartLight.getBrightness(device1))
    device1.setBrightness(40)
    print(SmartLight.getBrightness(device1))
    print(device1)

def testSmartHome():
    '''Tests the smart home class'''
    smartHome1 = SmartHome()
    plug1 = SmartPlug()
    plug2 = SmartPlug()
    light1 = SmartLight()
    plug2.toggleSwitch()
    plug2.setConsumptionRate(45)
    light1.setBrightness(35)
    smartHome1.addDevice(plug1)
    smartHome1.addDevice(plug2)
    smartHome1.addDevice(light1)
    print(smartHome1)
    smartHome1.turnOnAll()
    print(smartHome1)

# testSmartPlug()
# testDevice()
# testSmartHome()