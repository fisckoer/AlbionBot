import vgamepad as vg
import time

class XboxController:
    """
    Controlador Xbox virtual usando ViGEm + vgamepad.
    """

    MAX_AXIS_VALUE = 32767
    MAX_TRIGGER_VALUE = 255
    # 8 direcciones (x, y)
    directions = [
        (0, MAX_AXIS_VALUE),          # Arriba -> N
        # (MAX_AXIS_VALUE, MAX_AXIS_VALUE),        # Arriba-Derecha -> NE
        (MAX_AXIS_VALUE, 0),          # Derecha -> E
        #(MAX_AXIS_VALUE, -MAX_AXIS_VALUE),       # Abajo-Derecha -> SE
        (0, -MAX_AXIS_VALUE),         # Abajo -> S
        #(-MAX_AXIS_VALUE, -MAX_AXIS_VALUE),      # Abajo-Izquierda ->SW
        (-MAX_AXIS_VALUE, 0),         # Izquierda -> W
        #(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)        # Arriba-Izquierda -> NW
    ]

    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
        self._reset_controller()

    def _reset_controller(self):
        self.gamepad.left_joystick(0, 0)
        self.gamepad.right_joystick(0, 0)
        self.gamepad.left_trigger(0)
        self.gamepad.right_trigger(0)
        self.gamepad.update()

    def move_left_stick_smooth(
        self,
        target_x: int,
        target_y: int,
        duration: float = 1.0,
        steps: int = 120
    ):
        for step in range(steps):
            t = step / steps
            self.gamepad.left_joystick(
                x_value=int(target_x * t),
                y_value=int(target_y * t)
            )
            self.gamepad.update()
            time.sleep(duration / steps)

        for step in range(steps):
            t = 1 - (step / steps)
            self.gamepad.left_joystick(
                x_value=int(target_x * t),
                y_value=int(target_y * t)
            )
            self.gamepad.update()
            time.sleep(duration / steps)

        self.gamepad.left_joystick(0, 0)
        self.gamepad.update()

    def press_rt(self, duration: float = 0.2):
        self.gamepad.right_trigger(self.MAX_TRIGGER_VALUE)
        self.gamepad.update()
        time.sleep(duration)
        self.gamepad.right_trigger(0)
        self.gamepad.update()

    def press_left_stick(self, duration: float = 0.2):
        """
        Presiona el stick izquierdo (L3).

        :param duration: Tiempo que se mantiene presionado (segundos)
        """
        self.gamepad.press_button(
            button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
        )
        self.gamepad.update()

        time.sleep(duration)

        self.gamepad.release_button(
            button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
        )
        self.gamepad.update()

    def release_left_stick(self):
        """
        Suelta el stick izquierdo (posición neutra).
        """
        self.move_left_stick(0, 0)    

    def move_left_stick(self, x: int, y: int):
        """
        Mueve el stick izquierdo a una posición exacta (no smooth).
        """ 
        self.gamepad.left_joystick(x_value=x, y_value=y)
        self.gamepad.update()

    """
    Agregamos presion de botos para ataques, parte del bot para poder defenderse si es atacando 
    Botones de acción 
    """
    def press_a(self, duration=0.15):
        self._press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, duration)

    def press_x(self, duration=0.15):
        self._press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X, duration)

    def press_y(self, duration=0.15):
        self._press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y, duration)

    def press_b(self, duration=0.15):
        self._press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B, duration)


    def press_lt(self, value=255):
        self.gamepad.left_trigger(value)
        self.gamepad.update()


    def release_lt(self):
        self.gamepad.left_trigger(0)
        self.gamepad.update()


    def lt_combo(self, button, duration=0.15):
        self.press_lt()
        time.sleep(0.05)
        self._press_button(button, duration)
        self.release_lt()


    def _press_button(self, button, duration):
        self.gamepad.press_button(button=button)
        self.gamepad.update()
        time.sleep(duration)
        self.gamepad.release_button(button=button)
        self.gamepad.update()
