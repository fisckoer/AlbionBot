
from vision.mount_vision import MountVision
from bot.bot_state import BotState
import time




class MountWatcher:
    """
    Hilo que monitorea constantemente la vida del jugador.
    """

    def __init__(self,script_dir, state:BotState):
        self.state = state
        self.mount_vision = MountVision(script_dir)


    def run(self):
        print("👁️ Mount watcher activo")

        while True:
            if self.mount_vision.is_mounted():
                self.state.is_mount = True
            else:
                self.state.is_mount = False
            time.sleep(0.1)