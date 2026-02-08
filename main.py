from bot.farming_bot import FarmingBot
import os
import pyautogui
from test import ScreenAreaSelector
#"""
if __name__ == "__main__":

    FarmingBot(os.path.dirname(os.path.abspath(__file__))).run() 
#"""
#"""
#region (616, 266, 65, 8) barra salud personaje montado 
#region (608, 300, 66, 7)
#region (328, 764, 54, 50) icono de montura

"""
if __name__ == "__main__":
    
    #area =  ScreenAreaSelector.select_area()
    area = (303, 82, 112, 12)
    iml = pyautogui.screenshot(region=area)
    iml.save("screenshot.png")
    print(area)                                                                                                                                          
    #run_bot()"""