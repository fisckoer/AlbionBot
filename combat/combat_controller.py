#EXPLORE → FARM → COMBAT → (ESCAPE) → EXPLORE

import time
from combat.combat_state import CombatState
from combat.combat_actions import CombatActions
from vision.combat_vision import CombatVision
import keyboard
import time
import random

class CombatController:
    """
    Orquestador principal del combate.
    """

    LOOP_DELAY = 0.15  # segundos

    def __init__(self, vision:CombatVision, actions:CombatActions,state:CombatState):
        self.vision = vision
        self.actions = actions
        self.state = state
        self._running = False

    def execute(self):
        print(f"Combating: ")
        self.vision.update()

        if self.vision.player_hp_percent <= 15 and not self.state.is_escaping:
            self.state.is_escaping = True
            self.escape()
            #continue

        if self.vision.player_hp_percent <= 30:
            self.defensive()
                
        self.attack_rotation(random.randint(1,4))

        if not self.state.is_in_combat:
            print("✅ Combate terminado")
            self.stop_all_actions()
    

    def attack_rotation(self,step=1):
        match step:
            case 1:
                self.actions.basic_attack()
                self.actions.skill_1()
                self.actions.move_up()
            case 2:
                self.actions.basic_attack()
                self.actions.skill_2()
                time.sleep(0.1)
                self.actions.move_down()
            case 3:
                self.actions.basic_attack()
                self.actions.skill_3()
                time.sleep(1.5)
                self.actions.move_left()
            case 4:
                self.actions.basic_attack()
                self.actions.skill_1()
                self.actions.move_rigth()
                

    def defensive(self):
        self.actions.defensive_5()

    def escape(self):
        self.actions.escape()

    def stop_all_actions(self):
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.release('s')    

