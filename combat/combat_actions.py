import time
import vgamepad as vg
from controller.xbox_controller import XboxController



class CombatActions:
    TIME=0.5
    STEPS=10
    def __init__(self, controller: XboxController):
        self.controller = controller

    def basic_attack(self):
        self.controller.press_a()

    def skill_1(self):
        self.controller.press_x()

    def skill_2(self):
        self.controller.press_y()

    def skill_3(self):
        self.controller.press_b()

    def defensive_4(self):
        self.controller.lt_combo(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

    def defensive_5(self):
        self.controller.lt_combo(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    def escape(self):
        print("🏃‍♂️ Huyendo")
        self.controller.lt_combo(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        self.controller.move_left_stick_smooth(0, -32767, duration=5)
        self.controller.release_left_stick()


    def move_up(self):
        self.controller.move_left_stick_smooth( target_x=0,target_y=self.controller.MAX_AXIS_VALUE, duration=self.TIME, steps=self.STEPS)
    
    def move_down(self):
        self.controller.move_left_stick_smooth( target_x=0,target_y=-self.controller.MAX_AXIS_VALUE, duration=self.TIME, steps=self.STEPS)

    def move_rigth(self):
        self.controller.move_left_stick_smooth( target_x=self.controller.MAX_AXIS_VALUE,target_y=0, duration=self.TIME, steps=self.STEPS)

    def move_left(self):
        self.controller.move_left_stick_smooth( target_x=-self.controller.MAX_AXIS_VALUE,target_y=0, duration=self.TIME, steps=self.STEPS)

    def stop_all(self):
        self.controller.release_left_stick()

