from PIL import ImageGrab
import os

def screenshot(full_directory_save=""):
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(os.path.join(str(full_directory_save),str("screenshot.jpg")))
        screenshot.close()
    except Exception as e:
        print(f'SCREENSHOT ERROR: {e}')
