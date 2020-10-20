import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO article (videoLink, urlExtension, title, content) VALUES (?,?,?,?)", ('https://www.youtube.com/embed/XmpsruNHdzo','bottlender-prototype', 'Bottlender-prototype', '''Usage
THIS IS PROTOTYPE!

This is mobile app code and hardware code + circuit for automatic air cannon. It was made during Sporthack 2020 to deliver small packages that would fall down from air using parachutes. The mechanical part is not included. This cannon is built like a turret and can be made to shoot at certain locations using formulas and right calculations.

App was made using Nativescript and Angular, hardware was made using Node MCU ESP32S in C.

Libraries used
For ESP32 I made 3 libraries for hardware control (they are in lib folder)

Bluetooth.h
Motor.h
Switch.h
Bluetooth.h
This library uses 3 additional ESP32 libraries, BLEDevice.h, BLEUtils.h, BLEServer.h for using Bluetooth v4 on ESP

void checkNewData() checks if vale in BTv4 characteristic has been changed
bool getNewData() if there are new data then returns true
int getXAxis() returns X axis value
int getYAxis() returns Y axis value
bool getShoot() returns bool if cannon should shoot
bool getReload() returns bool if cannon needs to be reload
void setup() starts Bluetooth and configures everything in object
void loop() checks for new data, must be in main loop
Motor.h
Used for controlling stepper motors with A4988 drivers

Motor(int stepsPerRevolution, byte stepPin, byte dirPin, int step) initialzies object
int StepsPerRevolution how many steps should motor do to make one full rotation for stepper itself or gear attached to it
byte stepPin goes to a4988 step pin
byte dirPin goes to a4988 dir pin
int step how many rotations should motor to to make one step (more than 1 if gears are attached to stepper motor)
void setup() setups motors
void loop() goes to set motor position
setPosition() sets new position for motors (0 - 360, received from bluetooth object)
Switch.h
Used for turning on and off relays

Switch(byte switchPin, int delayTime)
byte switchPin switch pin
int delayTime time in millis for how long should switch be turned on
void setup() starts object
void loop() runs switch
void toggle() turns on switch
Other libraries
For nativescript app NativeScriptUISideDrawerModule, Bluetooth was used

Setup
This repository contains code part only, not a whole build

ESP32
PlatformIO was used to upload and setup the code, put lib and src folders into corresponding places and it should work.

Android
Nativescript and Angular were used to make this app. Put the components and other files into corresponding places.

Install Nativescript Bluetooth plugin and RadSideDrawer plugin!!

To make connection with hardware go to Bluetooth page and wait for connection, if it doesn't work, press connect. After connection go to input and input how many ammunition you put in cannon. After that you can go to main page and control the turret. Hardware doesn't take two equal input, so you can't shoot twice and must reload after every time.'''))

cur.execute("INSERT INTO article (urlExtension, title, content) VALUES (?,?,?)", ('esp-console', 'ESP-Console', 'Epic snake'))
cur.execute("INSERT INTO article (urlExtension, title, content) VALUES (?,?,?)", ('roboarm', 'RoboArm', '''Usage
Hardware and mobile app code for Robotic Arm that is controlled by Arduino Nano. There are two main function that arm can do. One is manual control, where you can control all arm movements via app. Second function is auto, where has been programmed to take ball from bottom and put it on top of roller coaster, so the ball could roll back and be picked up again. There is no mechanical part description in this documentation. Bluetooth 4.0 module will be needed to receive data from app.

Libraries used
Hardware
BtClassic.h custom made library for receiving and processing incoming bluetooth data, described here
Servo.h standard Arduino Servo motor library
DcMotor.h custom made library for driving DC motors using l293d motor driver IC
Motor.h custom made library for driving stepper motors using A4988 driver
Arduino.h
App
The app was written in nativescript using Angular framework, following modules will be needed

Bluetooth
NativeScriptFormsModule
NativeScriptUISideDrawerModule
App build is located in App folder and hardware code is located in Hardware folder. In Hardware folder there is also epicSin folder. It contains arduino arm code that makes automatic movements of arm smoother by using sin function.

Setup
App setup
This repository contains whole build for app, because some recent releases were buggy and did not run the code properly. Other than that, you have to install all the app modules needed for the app. After that, app should be good to go.

Hardware setup
You should upload code to arduino using PlatformIO. This repository contains whole build.'''))

cur.execute("INSERT INTO article (urlExtension, title, content) VALUES (?,?,?)", ('attiny-led', 'Attiny-Led', 'Attiny13a register code examples.'))
cur.execute("INSERT INTO article (urlExtension, title, content) VALUES (?,?,?)", ('btclassich', 'BtClassic.h', '''Usage
Arduino library for receiving Serial data on Rx/Tx pins and processing it. Using custom made protocol, you can send up to 10 commands and parameters with them.

Methods
BtClassic() initializes BtClassic object
void checkNewData() gets new incoming data and assigns it to variables
bool getNewData() returns true if new data has been received and processed
void loop() main loop, must be placed in loop
byte getType() gets type value (0 - 9)
int getValue() gets main value (0 - 999)
Protocol
Data has to be sent in specific way in order for this library to process it. The way data needs to be sent looks like this:

<[yourType][yourValue]>

First must always come < sign and so must be > at the end

yourType must be one digit number

yourValue must be three digit number

If you want to send ```yourValue`` that is less than 100 or 10, additional zeros must be added, like 099 or 009

Examples
<2411> type = 2 value = 411

<0002> type = 0 value = 2

<0000> type = 0 value = 0'''))

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (1, 'Image 1', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (1, 'Image 2', 'https://ih1.redbubble.net/image.1573052278.8041/st,small,507x507-pad,600x600,f8f8f8.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (2, 'Image 3', 'https://ih1.redbubble.net/image.1573052278.8041/st,small,507x507-pad,600x600,f8f8f8.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (3, 'Image 4', 'https://ih1.redbubble.net/image.1681670101.0178/st,small,507x507-pad,600x600,f8f8f8.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (3, 'Image 5', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (4, 'Image 6', 'https://ih1.redbubble.net/image.1667702518.3342/st,small,507x507-pad,600x600,f8f8f8.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (5, 'Image 7s', 'https://ih1.redbubble.net/image.1681663462.0030/st,small,507x507-pad,600x600,f8f8f8.jpg')
            )
connection.commit()
connection.close()