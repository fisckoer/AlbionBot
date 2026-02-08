import pyautogui
import time
import os
from vision.vision_utils import VisionUtils
from bot.regions import Regions
from bot.bot_state import BotState




class FarmingVision:

    def __init__(self, script_dir,state:BotState):
        self.init_icon = os.path.join(script_dir, "img/RT.png")
        self.mount_icon = os.path.join(script_dir, "img/mount.png")
        self.regions = Regions() 
        self.state = state

        self.init_region = self.regions.INIT_FARMING_ICON
        self.progress_region = self.regions.PROGRESS_REGION

        self.farming_images = [
            os.path.join(script_dir, "img/cottonFarming.png"),
            os.path.join(script_dir, "img/leatherFarming.png"),
            os.path.join(script_dir, "img/woodFarming.png")
        ]

    def farming_available(self) -> bool:
        try:
            img = pyautogui.screenshot(region=self.init_region)
            img.save("farmingRT.png")
            pyautogui.locateOnScreen(
                self.init_icon,
                region=self.init_region,
                confidence=0.7,
                grayscale=True
            )
            
            
            return True
        except pyautogui.ImageNotFoundException:
            return False

    def wait_farming_end(self):
        active_icon = None
        for img in self.farming_images:
            try:
                pyautogui.locateOnScreen(
                    img,
                    region=self.progress_region,
                    confidence=0.8,
                    grayscale=True
                )
                active_icon = img
                break
            except pyautogui.ImageNotFoundException:
                pass

        if not active_icon:
            return
        print(f"Farming ::  {active_icon}")
        VisionUtils.wait_until_image_disappears(active_icon, self.progress_region,self.state)


    def wait_mount_end(self):
        VisionUtils.wait_until_image_disappears(self.mount_icon, self.progress_region,self.state)
