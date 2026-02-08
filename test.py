import pyautogui
import time
import win32api

class ScreenAreaSelector:
    """
    Permite al usuario seleccionar un área de la pantalla
    arrastrando el mouse (click inicial + click final).
    """

    @staticmethod
    def select_area(log_callback=None, delay=0.3):
        """
        Permite al usuario definir la zona de seguimiento en la pantalla.
        El usuario debe arrastrar el mouse mientras mantiene presionada la barra espaciadora.

        :param log_callback: Función de callback para registrar mensajes en la GUI.
        """
        state_left = win32api.GetKeyState(0x20)  # Estado de la barra espaciadora
        image_coords = []

        if log_callback:
            log_callback('Please hold and drag space over tracking zone (top left to bottom right)')

        while True:
            a = win32api.GetKeyState(0x20)
            if a != state_left:  # Estado de la barra espaciadora cambiado
                state_left = a
                if a < 0:  # Barra espaciadora presionada
                    x, y = pyautogui.position()
                    image_coords.append((x, y))
                else:  # Barra espaciadora liberada
                    x, y = pyautogui.position()
                    image_coords.append((x, y))
                    break
            time.sleep(0.001)

        start_point = image_coords[0]
        end_point = image_coords[1]
        return  (start_point[0], start_point[1], end_point[0]-start_point[0], end_point[1]-start_point[1])
