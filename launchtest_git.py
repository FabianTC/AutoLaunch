import subprocess
import pyautogui
import pydirectinput
import pygetwindow as gw
import time

def open_application_windows(application_path):
    subprocess.Popen(application_path, shell=True)

     # Wait for the application to open
    timeout = 10  # Adjust as needed based on the application's load time
    while timeout > 0:
        try:
            # Try to activate the window
            gw.getWindowsWithTitle("Your Application Title")[0].activate()
            break
        except IndexError:
            # Window not found, wait and try again
            time.sleep(1)
            timeout -= 1

# Function to perform the login
def perform_login(username, password):
    # Replace these coordinates with the actual coordinates of the username and password fields
    username_field = (1000, 300)
    password_field = (1000, 400)
    login_button = (800, 400)

    pyautogui.press('enter')
    pyautogui.click(username_field)
    clear_field(username_field, len(username))
    time.sleep(0.5) # Introduce a delay
    pyautogui.typewrite(username, interval=0.05) # Adjust interval as needed
    time.sleep(0.5) # Introduce a delay

    pyautogui.click(password_field)
    pyautogui.typewrite(password, interval=0.05)

    pyautogui.click(login_button)
    time.sleep(10) # Final login delay
    pyautogui.click(800, 400)

def clear_field(field_position, length):
    for _ in range(length):
        pyautogui.press('backspace')
        time.sleep(0.001)  # Introduce a small delay between backspace

# Example usage
if __name__ == "__main__":
    # Replace this with the actual path to your application and login credentials
    application_path = r"C:\Users\Fabian\AppData\Local\RuneLite\RuneLite.exe"
    username = "Your_User_Here"
    password = "Your_Pass_Here"

    open_application_windows(application_path)
    time.sleep(2)  # Adjust as needed based on the application's load time
    perform_login(username, password)
