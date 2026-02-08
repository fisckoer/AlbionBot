from xbox_controller import XboxController
import random
import keyboard
import time
from pyautogui import *
import pyautogui
import os
import math
from PIL import ImageChops
import threading
import imagehash
#El bot esta hecho para una resolucion de 1200 x 800
# region donde aparece el icono mientras farmeas 
# region=(500, 500, 250, 100)
#regino donde aparece el simbolo para iniciar a farmear 
#region=(500, 250, 300, 200)
#region de minimapa
#region = (1080, 650, 200, 150)
class FarmingBot:
    # Intensidad máxima del joystick
    #Cargamos imagenes que vamos a utilizar para varias acciones
    
    def __init__(self):
        self.controller = XboxController()
        self.max_val = self.controller.MAX_AXIS_VALUE
        self.directions = self.controller.directions
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.farming_images = [
            os.path.join(self.script_dir, "img/cottonFarming.png"),
            os.path.join(self.script_dir, "img/leatherFarming.png"),
            os.path.join(self.script_dir, "img/woodFarming.png")
        ]
        self.init_icon_farming = os.path.join(self.script_dir, "img/pick.png")
        self.farming_icon_region = (500, 500, 250, 100)
        self.init_farming_icon_region = (500, 250, 300, 200)
        self.angle = 0.0            # ángulo actual en radianes
        self.angle_step = math.pi / 6  # 30 grados
        self.move_duration = 1.2
        self.stop_movement = False
        self.farming_lock = threading.Lock()
        self.minimap_region = (1080, 650, 200, 150)
        self.mount_icon= os.path.join(self.script_dir, "img/mount.png")


    def move_forward(self):
        """
        Movimiento continuo hacia una dirección calculada.
        """
        x = int(math.cos(self.angle) * self.max_val)
        y = int(math.sin(self.angle) * self.max_val)

        print(f"Moviendo hacia ángulo {round(math.degrees(self.angle), 1)}° -> ({x}, {y})")
        self.controller.move_left_stick_smooth(x, y,duration=self.move_duration,steps=60)

    def move_forward_interruptible(self):
        step_time = 0.1
        steps = int(self.move_duration / step_time)

        x = int(math.cos(self.angle) * self.max_val)
        y = int(math.sin(self.angle) * self.max_val)

        for _ in range(steps):
            if self.stop_movement:
                self.controller.release_left_stick()
                return

            self.controller.move_left_stick(x, y)
            time.sleep(step_time)

        self.controller.release_left_stick()


    def rotate_direction(self):
        """
        Gira el ángulo de movimiento para explorar nueva zona.
        """
        self.angle += self.angle_step
        if self.angle > math.tau:
            self.angle = 0    

    def minimap_hash(self):
        img = pyautogui.screenshot(region=self.minimap_region)
        img = img.resize((64, 64)).convert("L")
        return imagehash.phash(img)

    def minimap_is_similar(self, h1, h2, threshold=8):
        return abs(h1 - h2) < threshold

    def capture_minimap(self):
        return pyautogui.screenshot(region=(1080, 650, 200, 150))
    
    def minimap_changed(self, img1, img2, threshold=5):
        diff = ImageChops.difference(img1, img2)
        return diff.getbbox() is not None

    def farm_action(self):
        """Simula la acción de recolección (RT)."""
        print("Ejecutando acción de farmeo...")
        self.controller.release_left_stick();
        self.controller.press_rt(duration=0.3)
        time.sleep(1)
        self.farming_time()
        self.mount()

    def farming_watcher(self):
        """
        Hilo que detecta el icono de farmeo y detiene el movimiento.
        """
        while True:
            if self.search_icon_farming():
                if not self.stop_movement:
                    print("🛑 Icono detectado, deteniendo movimiento")
                    self.stop_movement = True
                    with self.farming_lock:
                        self.farm_action()
                    self.stop_movement = False
            time.sleep(0.5)    

    def search_icon_farming(self):
        #print('Buscando imagen para iniciar farmeo')
        try:    
            pyautogui.locateOnScreen(self.init_icon_farming ,region=self.init_farming_icon_region,
                                        grayscale=False,confidence=0.6)
            #print('Imagen para iniciar farmeo encontrada')
            return True
        except ImageNotFoundException: 
            #print('Imagen para iniciar farmeo NO encontrada')
            return False

    def farming_time(self):
        print('Farming time')
        farm_icon_progress = None
        for img in self.farming_images:
            try:
                pyautogui.locateOnScreen(img, region=self.farming_icon_region, grayscale=True, confidence=0.8)
                #print(f"Farming icon found: {img}" ) 
                farm_icon_progress = img
                break
            except ImageNotFoundException:
                print(f"Farming icon not found" )
        if farm_icon_progress != None :
            while True:
                try: 
                    if pyautogui.locateOnScreen(farm_icon_progress,region=self.farming_icon_region
                                            ,grayscale=True,confidence=0.8) != None: 
                        #print('Farming ....')
                        time.sleep(1) 
                except ImageNotFoundException: 
                    #print(f"End of Farming" ) 
                    pyautogui.sleep(0.5)
                    break;

    def mount(self):
        self.controller.press_left_stick(duration=0.5)
        print('Mounting ...')
        while True:
            try: 
                if pyautogui.locateOnScreen(self.mount_icon,region=self.farming_icon_region
                                            ,grayscale=True,confidence=0.8) != None: 
                    time.sleep(1) 
            except ImageNotFoundException: 
                #print(f"End of Farming" ) 
                pyautogui.sleep(0.5)
                break;
        time.sleep(1)

        
    def run(self):
        print("🤖 Bot iniciado")

        threading.Thread(
            target=self.farming_watcher,
            daemon=True
        ).start()

        last_hash = None

        while not keyboard.is_pressed("esc"):

            if self.stop_movement:
                time.sleep(0.1)
                continue

            self.move_forward_interruptible()

            try:
                current_hash = self.minimap_hash()

                if last_hash and self.minimap_is_similar(last_hash, current_hash):
                    print("🔄 Loop detectado → girando")
                    self.rotate_direction()

                last_hash = current_hash

            except Exception as e:
                print(f"Minimap error: {e}")

            time.sleep(0.2)

        print("🛑 Bot detenido")
        self.controller.release_left_stick()




def run_bot():
    bot = FarmingBot()
    print("Bot iniciado. Presiona 'esc' para detener.")
    bot.run()


if __name__ == "__main__":
    run_bot()