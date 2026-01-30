import allure
import os
from datetime import datetime

def take_screenshot(drive, name):
    screenshot_path = f"reports/screenshots/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    drive.save_screenshot(screenshot_path)

    with open(screenshot_path,"rb") as f:
        allure.attach(f.read(), name = name, attachment_type=allure.attachment_type.PNG)