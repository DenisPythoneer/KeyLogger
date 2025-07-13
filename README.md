# 🐍 KeyLogger Project

![Скриншот интерфейса server.py](https://raw.githubusercontent.com/DenisPythoneer/KeyLogger/main/image/screenshotOne.png)

### Простой проект кейлоггера, состоящий из трех основных компонентов❗

    Сервер (server.py) - принимает и сохраняет данные о нажатиях клавиш от клиента

    Клиент (client.py) - записывает нажатия клавиш и отправляет их на сервер

    Билдер (builder.py) - конвертирует клиентскую часть в исполняемый EXE-файл

### ⚙️ Особенности

    Логирование нажатий клавиш с временными метками

    Возможность удаленного управления через сервер

    Сохранение логов в файл

    Конвертация клиента в EXE для удобного распространения

    Цветной интерфейс с ASCII-баннерами

### 📦 Установка

Клонируйте репозиторий:

    bash

    git clone https://github.com/DenisPythoneer/KeyLogger.git
    
    cd keylogger-project

Установите зависимости:

    bash

    pip install -r requirements.txt

### 🚀 Использование

Запустите сервер:

    bash

    python server.py

Запустите клиент (или используйте скомпилированный EXE):
      
    bash

    python client.py

![Скриншот интерфейса client.py](https://raw.githubusercontent.com/DenisPythoneer/KeyLogger/main/image/ScreenshotTwo.png)

Для создания EXE-версии клиента:
    
    bash

    python builder.py

![Скриншот интерфейса builder.py](https://raw.githubusercontent.com/DenisPythoneer/KeyLogger/main/image/screenshotThree.png)

Команды сервера

    logs - получить логи с клиента

    break - отключить клиент

### ❗ Предупреждение

    Этот проект предназначен только для образовательных целей и тестирования на собственных системах. Использование кейлоггера без явного согласия пользователя может нарушать законы о конфиденциальности.

### 🔗 Ссылка на автора: https://t.me/denispythoneer
