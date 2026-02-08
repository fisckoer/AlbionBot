
from bot.regions import Regions
import pyautogui
import os



class MountVision:
    """
    Detecta si el jugador está montado basándose en el icono de montura.
    """

    def __init__(self, script_dir):
        self.mount_icon = os.path.join(script_dir, "img/mount_icon.png")
        # Región donde suele aparecer el icono de estado de montura
        self.mount_region = Regions.MOUNT_ICON


    def is_mounted(self) -> bool:
        try:
            img = pyautogui.screenshot(region=self.mount_region)
            img.save("mount_icon.png")
            pyautogui.locateOnScreen(
                self.mount_icon,
                region=self.mount_region,
                confidence=0.9,
                grayscale=False
            )
            return True
        except pyautogui.ImageNotFoundException:
            return False
