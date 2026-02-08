import pyautogui
import imagehash


class MinimapVision:
    def __init__(self):
        # Región del minimapa (x, y, ancho, alto)
        self.region = (1080, 650, 200, 150)

    def hash(self):
        # Captura solo el minimapa
        img = pyautogui.screenshot(region=self.region)

        # Normaliza tamaño y pasa a escala de grises
        img = img.resize((64, 64)).convert("L")

        # Genera hash perceptual
        return imagehash.phash(img)

    @staticmethod
    def is_similar(h1, h2, threshold=8) -> bool:
        # Compara hashes por distancia de Hamming
        return abs(h1 - h2) < threshold
