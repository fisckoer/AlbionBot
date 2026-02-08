
from bot.bot_state import BotState
from vision.vision_utils import VisionUtils
from bot.regions import Regions
import time
import os




class MoobWatcher:
    """
    Hilo que monitorea constantemente la vida del jugador.
    """

    def __init__(self,script_dir, state:BotState):
        self.state = state
        self.mobb_ring_ico = os.path.join(script_dir, "img/moob_energie.png")
        self.regions = Regions() 




    def run(self):
        print("👁️  Moob watcher activo")

        while True:
            if VisionUtils.img_search_on_screen(self.mobb_ring_ico,self.regions.MOOB_HEALTH,0.6):
                self.state.moob_watch = True
                print("👁️  Moob detectado")
            else:
                self.state.moob_watch = False
            time.sleep(0.8)

