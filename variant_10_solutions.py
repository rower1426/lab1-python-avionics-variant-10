"""
Лабораторна робота: Варіант 10
Студент: Юрчак Артемій 
Група: EIP30
"""

# Задача 1: Ефективність сонячних батарей (if/elif/else)
def solar_panel_efficiency(theta: float, is_shaded: bool) -> str:
    """
    - is_shaded або theta > 60 -> "Генерація 0%"
    - theta <= 15 -> "Генерація 100%"
    - 15 < theta <= 60 -> "Генерація 50%"
    """
    ...

# Задача 2: Диспетчер радіокоманд (match-case)
def dispatch_radio_command(cmd_list: list) -> str:
    """
    Використовує match-case з розширеним розпакуванням:
    - ["PING"] -> "PONG"
    - ["SET_ATTITUDE", roll, pitch, yaw] -> "Attitude set: {roll}, {pitch}, {yaw}"
    - ["REBOOT", "FORCE"] -> "Forced reboot"
    """
    ...

# Задача 3: Перевірка каналів зв'язку (for / else)
def check_communication_channels(channels: list) -> str:
    """
    Перебирає список каналів. Якщо є True -> перериває break і повертає "Канал {idx} активний".
    Якщо активних немає -> через else повертає "Аварія: немає зв'язку".
    """
    ...

# Задача 4: Калібрування акселерометра на місці (range)
def calibrate_accelerometer_inplace(data: list) -> list:
    """
    Модифікує елементи списку data "на місці", додаючи +0.05 до кожного елемента через range(len(data)).
    """
    ...
