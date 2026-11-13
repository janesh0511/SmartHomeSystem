from device import SmartDevice
from smart_light import SmartLight
from smart_thermostat import SmartThermostat

def main():
    print(" SMART HOME SYSTEM  \n")

    devices: list[SmartDevice] = [
        SmartLight("Living Room Light"),
        SmartThermostat("Master Bedroom Thermostat")
    ]

    print(" 1. Polymorphic Collection Loop (Dynamic Polymorphism) ")
    for device in devices:
        print(device)
        result = device.operate()
        print(f"Action Output: {result}")
        print(f"Updated State: {device}\n")

    print("2. Direct Method Overloading ")
    light_instance = SmartLight("Kitchen Light")
    thermostat_instance = SmartThermostat("Hallway Thermostat")

    print(f"Initial: {light_instance}")
    print(f"Overloaded Call Output: {light_instance.operate(85)}")
    print(f"Final: {light_instance}\n")

    print(f"Initial: {thermostat_instance}")
    print(f"Overloaded Call Output: {thermostat_instance.operate(68.5)}")
    print(f"Final: {thermostat_instance}\n")

    print("  REQUIREMENTS SUCCESSFULLY COMPLETED ")

if __name__ == "__main__":
    main()