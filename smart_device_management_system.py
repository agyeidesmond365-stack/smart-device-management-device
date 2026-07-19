class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = None
        self.__power_status = False
        self.device_id = device_id

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        if value is None or str(value).strip() == "":
            raise ValueError("Device ID cannot be empty.")
        self.__device_id = str(value).strip()

    @property
    def power_status(self):
        return self.__power_status

    def turn_on(self):
        self.__power_status = True
        print(self.name + " is now ON.")

    def turn_off(self):
        self.__power_status = False
        print(self.name + " is now OFF.")

    def display_info(self):
        if self.__power_status == True:
            status = "ON"
        else:
            status = "OFF"
        print("Name: " + self.name)
        print("Device ID: " + self.__device_id)
        print("Power Status: " + status)


class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.__recording_status = False

    @property
    def recording_status(self):
        return self.__recording_status

    def start_recording(self):
        if self.power_status == False:
            print("Cannot start recording, device is OFF.")
            return
        self.__recording_status = True
        print(self.name + " started recording.")

    def stop_recording(self):
        self.__recording_status = False
        print(self.name + " stopped recording.")

    def display_info(self):
        super().display_info()
        if self.__recording_status == True:
            print("Recording Status: Recording")
        else:
            print("Recording Status: Not Recording")


class SmartLight(SmartDevice):
    def __init__(self, name, device_id, brightness):
        super().__init__(name, device_id)
        self.__brightness = 0
        self.brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if value < 0 or value > 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness = value

    def increase_brightness(self):
        new_value = self.__brightness + 10
        if new_value > 100:
            new_value = 100
        self.__brightness = new_value
        print(self.name + " brightness is now " + str(self.__brightness))

    def decrease_brightness(self):
        new_value = self.__brightness - 10
        if new_value < 0:
            new_value = 0
        self.__brightness = new_value
        print(self.name + " brightness is now " + str(self.__brightness))

    def display_info(self):
        super().display_info()
        print("Brightness: " + str(self.__brightness))


class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature):
        super().__init__(name, device_id)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    def read_temperature(self):
        if self.power_status == False:
            print("Cannot read temperature, device is OFF.")
            return None
        print(self.name + " temperature is " + str(self.__temperature))
        return self.__temperature

    def display_info(self):
        super().display_info()
        print("Temperature: " + str(self.__temperature))


def make_devices():
    devices = []
    cam = SecurityCamera("Front Door Camera", "CAM001")
    light = SmartLight("Living Room Light", "LGT001", 40)
    sensor = TemperatureSensor("Kitchen Sensor", "TMP001", 23.5)
    devices.append(cam)
    devices.append(light)
    devices.append(sensor)
    return devices


def pick_device(devices):
    print("Select a device:")
    i = 1
    for d in devices:
        print(str(i) + ". " + d.name)
        i = i + 1
    print("0. Cancel")
    choice = input("Enter number: ")
    if choice.isdigit() == False:
        print("Invalid input.")
        return None
    choice = int(choice)
    if choice == 0:
        return None
    if choice >= 1 and choice <= len(devices):
        return devices[choice - 1]
    print("Invalid selection.")
    return None


def show_menu():
    print("")
    print("SMART DEVICE MANAGEMENT SYSTEM")
    print("1. Display Device Information")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start Recording")
    print("7. Exit")


def main():
    devices = make_devices()
    print("Devices created:")
    for d in devices:
        d.display_info()

    running = True
    while running == True:
        show_menu()
        choice = input("Choose option 1-7: ")

        if choice == "1":
            for d in devices:
                d.display_info()

        elif choice == "2":
            d = pick_device(devices)
            if d != None:
                d.turn_on()

        elif choice == "3":
            d = pick_device(devices)
            if d != None:
                d.turn_off()

        elif choice == "4":
            temp_devices = []
            for d in devices:
                if isinstance(d, TemperatureSensor):
                    temp_devices.append(d)
            if len(temp_devices) == 0:
                print("No temperature sensors.")
            else:
                d = pick_device(temp_devices)
                if d != None:
                    d.read_temperature()

        elif choice == "5":
            light_devices = []
            for d in devices:
                if isinstance(d, SmartLight):
                    light_devices.append(d)
            if len(light_devices) == 0:
                print("No smart lights.")
            else:
                d = pick_device(light_devices)
                if d != None:
                    up_or_down = input("Type up or down: ")
                    if up_or_down == "up":
                        d.increase_brightness()
                    elif up_or_down == "down":
                        d.decrease_brightness()
                    else:
                        print("Invalid option.")

        elif choice == "6":
            camera_devices = []
            for d in devices:
                if isinstance(d, SecurityCamera):
                    camera_devices.append(d)
            if len(camera_devices) == 0:
                print("No cameras.")
            else:
                d = pick_device(camera_devices)
                if d != None:
                    start_or_stop = input("Type start or stop: ")
                    if start_or_stop == "start":
                        d.start_recording()
                    elif start_or_stop == "stop":
                        d.stop_recording()
                    else:
                        print("Invalid option.")

        elif choice == "7":
            print("Goodbye!")
            running = False

        else:
            print("Invalid option.")


main()
