
import pyautogui
import time
import numpy as np
from PIL import Image
import cv2
import pytesseract
from bot.regions import Regions


class CombatVision:
    """
    Detecta combate usando únicamente la variación de la barra de vida.
    """
    _health_full = None
    health_now = None
    _regions = Regions()
    player_hp_percent =100

    def __init__(self, health_region, sample_delay=0.2):
        self.health_region = health_region
        self.sample_delay = sample_delay

        self._last_hp = None
        self._current_hp = None
        self._last_change_time = time.time()

    def _capture_health_bar(self,):
        img = pyautogui.screenshot(region=self._regions.HEALTH_BAR_2)
        #img.save(f"health_bar_ama.png")
        return np.array(img)
    
    def _health_percentage(self):
        img = self._capture_health_bar()
        # Convertir a gris
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Aumentar contraste
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        # OCR solo números y letras
        #config = "--psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/"
        config = "--psm 6 -c tessedit_char_whitelist=0123456789/"
        text = pytesseract.image_to_string(thresh, config=config)
        health_array = text.split("/")
        if len(health_array) != 2:
            return None
        if self._health_full is None:
            self._health_full = int(health_array[1])
        self.health_now = int(health_array[0])
        percent = int((self.health_now *100)/self._health_full)
        self.player_hp_percent = percent
        return percent


    def update(self):
        self._last_hp = self._current_hp
        self._current_hp = self._health_percentage()
        if self._last_hp is not None:
            if self._current_hp != self._last_hp:
                self._last_change_time = time.time()

    """def player_hp_percent(self,img_num) -> int:
        if self._current_hp is None:
            self.update()
        return self._current_hp"""

    def is_in_combat(self) -> bool:
        """
        Si la vida ha bajado recientemente → combate
        """
        if self._last_hp is None:
            return False

        return self._current_hp <= self._last_hp

    def is_out_of_combat(self) -> bool:
        """
        Si la vida sube o se mantiene estable durante un tiempo
        """
        #stable_time = time.time() - self._last_change_time
        if self._last_hp is None:
            return False
        return self._current_hp > self._last_hp


"""
if __name__ == "__main__":
    print("Test combat_vision")
    img = pyautogui.screenshot(region=(78, 70, 106, 15))

    # Convertir a gris
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

    # Aumentar contraste
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # OCR solo números y letras
    config = "--psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/"

    text = pytesseract.image_to_string(thresh, config=config)

    # Cargar imagen
    

    print(text)
#"""
