import time
from pynput import mouse, keyboard
from pynput.keyboard import Key
import pyautogui

def pynput_to_pyautogui_key(pynput_key):
    if hasattr(pynput_key, "char"):
        return pynput_key.char
    elif pynput_key == Key.space:
        return "space"
    elif pynput_key == Key.enter:
        return "enter"
    elif pynput_key == Key.cmd:  # Tecla Windows
        return "win"
    return None

mouse_events = []
keyboard_events = []

def on_move(x, y):
    mouse_events.append(("move", time.time(), x, y))

def on_click(x, y, button, pressed):
    if pressed:
        mouse_events.append(("click", time.time(), x, y, button))

def on_press(key):
    pyautogui_key = pynput_to_pyautogui_key(key)
    if pyautogui_key is not None:
        keyboard_events.append(("press", time.time(), pyautogui_key))

def on_release(key):
    pyautogui_key = pynput_to_pyautogui_key(key)
    if pyautogui_key is not None:
        keyboard_events.append(("release", time.time(), pyautogui_key))

mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener.start()
keyboard_listener.start()

print("Gravando eventos por 15 segundos...")
time.sleep(15)

mouse_listener.stop()
keyboard_listener.stop()
print("Eventos Gravados")
print("Aguarde 5 segundos...")
time.sleep(5)

print("Reproduzindo eventos...")

combined_events = keyboard_events + mouse_events
combined_events.sort(key=lambda x: x[1])  # Ordena os eventos pela ordem do tempo

for event in combined_events:
    if event[0] in ["press", "release"]:
        if event[0] == "press":
            pyautogui.keyDown(event[2])
        elif event[0] == "release":
            pyautogui.keyUp(event[2])
    elif event[0] == "move":
        pyautogui.moveTo(event[2], event[3])
    elif event[0] == "click":
        pyautogui.click(event[2], event[3], button=event[4].name.lower())

