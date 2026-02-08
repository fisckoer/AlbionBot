import threading
import time
import keyboard
import os

#Vision
from vision.farming_vision import FarmingVision
from vision.minimap_vision import MinimapVision
from vision.combat_vision import CombatVision

#Watchers
from watcher.mount_wacher import MountWatcher
from watcher.farming_watcher import FarmingWatcher
from watcher.combat_watcher import CombatWatcher
from watcher.moob_wacher import MoobWatcher


#Controllers
from controller.xbox_controller import XboxController
from combat.combat_controller import CombatController

from combat.combat_actions import CombatActions

#Utils
from movement.navigator import Navigator
from bot.regions import Regions
from bot.bot_state import BotState





class FarmingBot:

    def __init__(self,script_dir):
        self.controller = XboxController()
        self.farming_lock = threading.Lock()
        # 🧠 Estado global
        self.state = BotState()
        self.script_dir =script_dir
        self.minimap = MinimapVision()
        self.navigator = Navigator(
            self.controller,
            self.controller.MAX_AXIS_VALUE
        )
        # ⚔️
        self.combat_vision = CombatVision(Regions.HEALTH_BAR)
        self.combat_actions = CombatActions(self.controller)
        self.combat_controller = CombatController(self.combat_vision,self.combat_actions,self.state)

        self.combat_watcher = CombatWatcher(
            combat_vision=self.combat_vision,
            combat_controller=self.combat_controller,
            state=self.state
        )
        self.farming_watcher = FarmingWatcher(self.controller,self.state,script_dir)
        self.mount_watcher = MountWatcher(script_dir,self.state)
        self.farming_vision = FarmingVision(script_dir,self.state)
        self.mob_watcher = MoobWatcher(script_dir,self.state)






    
    def run(self):
        print("🤖 Bot iniciado")

        threading.Thread(
            target=self.farming_watcher.run,
            daemon=True,
            name="farming_watcher"
        ).start()

        threading.Thread(
            target=self.mount_watcher.run,
            daemon=True,
            name="mount_watcher"
        ).start()
        threading.Thread(
            target=self.mob_watcher.run,
            daemon=True,
            name="moob_watcher"
        ).start()

        threading.Thread(
            target=self.combat_watcher.run,
            daemon=True,
            name="combat_watcher"
        ).start()

        last_hash = None
        print("🤖 Bot iniciado")
        while not keyboard.is_pressed("esc"):
            ##self.clear_console()
            
            #print(f"#BotState# \n {self.state}")

            if self.state.is_in_combat:
                self.combat_controller.execute()
                continue

            if self.state.stop_movement:
                time.sleep(0.2)
                continue

            
            #self.navigator.move_interruptible(lambda: self.state.stop_movement)

            current_hash = self.minimap.hash()

            if last_hash and self.minimap.is_similar(last_hash, current_hash):
                self.navigator.rotate()

            last_hash = current_hash

            if self.state.request_farming :
                    self.state.is_farming = True
                    self._farm()
                    
                    

            if not self.state.request_farming and not self.state.is_in_combat and not self.state.is_mount:
                print("Mounting ...")
                self.controller.press_left_stick(0.3)
                self.farming_vision.wait_mount_end()
                self.state.is_mount = True
                self.state.is_farming = False
                



            
            time.sleep(1)

        self.controller.release_left_stick()
        print("🛑 Bot detenido")

    def _farm(self):
        self.controller.release_left_stick()
        self.controller.press_rt(0.3)
        self.farming_vision.wait_farming_end()
        self.state.request_farming = False

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')    
        
        #
