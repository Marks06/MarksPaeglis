from abc import ABC, abstractmethod
import random

class Robot(ABC):
    def __init__(self,name): 
        self.name = name
        self.battery_level = random.randint(0, 100) 
    
    @abstractmethod 
    def perform_task(self):  
            pass
    def batteryStatus(self): 
        print(f"{self.name} baterijas līmenis: {self.battery_level}%")
    
class CleaningRobot(Robot):
    def perform_task(self):
        print(f"{self.name} tīra telpu ar putekļsūcēju!")
class SecurityRobot(Robot):
    def perform_task(self):
        print(f"{self.name} patrolē teritorijā un skenē apkārtni!")
class CookingRobot(Robot):
    def perform_task(self):
        print(f'{self.name} gatavo gardu ēdienu!')

roboti = [CleaningRobot("RoboCleaner"),
SecurityRobot("RoboGuard"),
CookingRobot("ChefBot")
]

for robots in roboti:
    robots.batteryStatus()
    robots.perform_task()
    print("-"*30)
