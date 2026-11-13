from device import SmartDevice

class SmartLight(SmartDevice):
    def __init__(self, name: str, brightness: int = 50):
        super().__init__(name)
        self.brightness = brightness

    def operate(self, brightness_level=None) -> str:
        if brightness_level is not None:
            self.brightness = brightness_level
            self.is_on = True
            return f"{self.name} brightness set to {self.brightness}%."
        else:
            self.is_on = not self.is_on
            state = "turned on" if self.is_on else "turned off"
            return f"{self.name} light has been {state}."