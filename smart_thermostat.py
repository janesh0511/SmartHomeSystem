from device import SmartDevice

class SmartThermostat(SmartDevice):
    def __init__(self, name: str, target_temp: float = 72.0):
        super().__init__(name)
        self.target_temp = target_temp

    def operate(self, target_temp=None) -> str:
        if target_temp is not None:
            self.target_temp = target_temp
            self.is_on = True
            return f"{self.name} target temperature updated to {self.target_temp}°F."
        else:
            self.is_on = True
            return f"{self.name} operating at preset temperature {self.target_temp}°F."