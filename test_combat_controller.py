import os

from watcher.moob_wacher import MoobWatcher
from bot.bot_state import BotState
from combat.combat_controller import CombatController
from combat.combat_actions import CombatActions
from watcher.combat_watcher import CombatWatcher
from bot.regions import Regions
from vision.combat_vision import CombatVision
from controller.xbox_controller import XboxController
import threading

if __name__ == "__main__":
    #Test mobbwatcher
    botstate = BotState()
    botstate.is_mount = False
    moobWatcher = MoobWatcher(os.path.dirname(os.path.abspath(__file__)),botstate)
    combat_vision=CombatVision(Regions.HEALTH_BAR)
    
    threading.Thread(
            target=moobWatcher.run,
            daemon=True,
            name="moob_watcher"
        ).start()
    
    print(botstate)

    combatWatcher = CombatWatcher(
            combat_vision=CombatVision(Regions.HEALTH_BAR),
            combat_controller=CombatController(combat_vision,CombatActions(XboxController()),botstate),
            state=botstate
        )

    combatWatcher.run()