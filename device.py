from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name
        self.is_on = False

    @abstractmethod
    def operate(self) -> str:
        pass

    def __str__(self):
        return f"Device: {self.name} | Status: {'On' if self.is_on else 'Off'}"