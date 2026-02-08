import time
from vision.combat_vision import CombatVision
from combat.combat_controller import CombatController
from bot.bot_state import BotState
import random



class CombatWatcher:
    """
    Hilo que monitorea constantemente la vida del jugador.
    """

    def __init__(self, combat_vision:CombatVision, combat_controller:CombatController, state:BotState):
        self.combat_vision = combat_vision
        self.combat_controller = combat_controller
        self.state = state

    def run(self):
        print("👁️ Combat watcher activo")
        while True:
            #Si estas sobre montura no puedes pelear
            if self.state.is_mount:
                self.state.is_in_combat = False
                self.state.is_escaping = False
                self.state.stop_movement = False
                time.sleep(0.2)
                continue
            self.combat_vision.update()


            # ENTRADA A COMBATE
            if self.state.moob_watch:
                if not self.state.is_in_combat:
                    print("⚔️ Combate detectado")
                    #señal para entrar en combate
                    self.state.is_in_combat = True
                    #señal para dejar detener el navigator
                    self.state.stop_movement = True
                    
            # SALIDA DE COMBATE
            if  not self.state.moob_watch and self.state.is_in_combat:
                print("⚔️ Combate detenido")
                #señal para detner acciones de combate
                self.state.is_in_combat = False
                #señal para dejar de espacar
                self.state.is_escaping = False
                #señal para detener movimiento
                self.state.stop_movement = False
            time.sleep(1)