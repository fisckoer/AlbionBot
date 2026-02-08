import pyautogui
import time
from bot.bot_state import BotState


class VisionUtils:

    @staticmethod
    def wait_until_image_disappears(image_path, region,state:BotState, timeout=None):
        """
        Espera hasta que la imagen desaparezca.
        Si timeout es None, espera indefinidamente.
        """
        start_time = time.time()

        while True:
            if state.is_in_combat:
                #Si entramos en combate mientras la barra de carga esta activa salimos para atacar
                break
            
            try:
                pyautogui.locateOnScreen(
                    image_path,
                    region=region,
                    confidence=0.8,
                    grayscale=True
                )

                # Control de timeout
                if timeout is not None:
                    elapsed = time.time() - start_time
                    if elapsed >= timeout:
                        break 

            except pyautogui.ImageNotFoundException:
                break 

    @staticmethod            
    def img_search_on_screen(img_search,region_img,porcentage = 0.9) -> bool:
        try:
            pyautogui.locateOnScreen(
                img_search,
                region=region_img,
                confidence=porcentage,
                grayscale=True
            )
            return True
        except pyautogui.ImageNotFoundException:
            return False            