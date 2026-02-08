import time
import threading
from vision.farming_vision import FarmingVision


class FarmingWatcher:

    def __init__(self, controller, state,script_dir):
        self.controller = controller
        self.state = state
        self.farming_lock =threading.Lock()
        self.vision = FarmingVision(script_dir,state)

    def run(self):
        print("👁️ Farming watcher activo")
        while self.state.running:
            if self._should_trigger_farming():
                self.state.request_farming = True  
                #self._signal_farming()
            #print(self.state.request_farming)
            time.sleep(0.3)
    # -------------------------
    # 🔍 lógica de detección
    # -------------------------

    def _should_trigger_farming(self) -> bool:
        return (
            self.vision.farming_available()
            and not self.state.is_farming
            and not self.state.is_in_combat
        )

    # -------------------------
    # 🚨 señal al sistema
    # -------------------------

    def _signal_farming(self):
        """
        Marca que hay un nodo disponible para farmear.
        No ejecuta acciones.
        """
        #with self.farming_lock:  
        self.state.request_farming = True  


    
