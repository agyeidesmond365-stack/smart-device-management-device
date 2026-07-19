# Smart Device Management System

## Project Overview
This project is an Object-Oriented Programming (OOP) mini project for **EL 162 / 234 Object Oriented Programming**, taught by Dr. Matthew Cobbinah.

The program simulates a smart home management system used by a technology company to control various smart devices. Each device shares common attributes (name, device ID, power status) but also has its own unique behavior depending on its type.

## Task Summary
The system was built to demonstrate the following OOP concepts:
- Variables and data types
- Input and output
- Conditional statements and loops
- Functions
- Classes and objects
- Constructors (`__init__`)
- Instance methods
- Inheritance and `super()`
- Encapsulation
- Getters/setters using the `@property` decorator

### Class Structure
- **`SmartDevice`** (parent class): holds the private `__device_id` and `__power_status` attributes, the public `name` attribute, and shared methods `turn_on()`, `turn_off()`, and `display_info()`. Access to the private attributes is controlled through `@property` getters/setters, including validation that a device ID cannot be empty.
- **`SecurityCamera`** (child class): adds a `recording_status` attribute along with `start_recording()` and `stop_recording()` methods.
- **`SmartLight`** (child class): adds a `brightness` attribute (validated to stay between 0 and 100) along with `increase_brightness()` and `decrease_brightness()` methods.
- **`TemperatureSensor`** (child class): adds a `temperature` attribute along with a `read_temperature()` method.

All child classes use `super().__init__()` to initialize the attributes inherited from `SmartDevice`.

### Menu-Driven Interface
When run, the program creates one sample device of each type (a security camera, a smart light, and a temperature sensor) and presents a menu:

1. Display Device Information
2. Turn Device On
3. Turn Device Off
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Exit

The menu loops until the user chooses to exit, using conditional statements to route the user's choice to the correct device method.

## How to Run the Program

### Requirements
- Python 3.7 or later (no external libraries required)

### Steps
1. Clone this repository:
   bash
   git clone https://github.com//agyeidesmond365/smart-device-management-system.git
   cd smart-device-management-system
   
2. Run the program:
   bash
   python3 smart_device_management_system.py
   
3. Follow the on-screen menu prompts to interact with the sample devices (turn devices on/off, read temperature, adjust brightness, start/stop recording, or view device information).

## File Structure
smart-device-management-system/
├── smart_device_management_system.py  
└── README.md                          

## Author
AGYEI DESMOND ANSONG
