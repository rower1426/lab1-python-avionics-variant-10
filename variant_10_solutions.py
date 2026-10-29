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
    if theta>60 or is_shaded:
        return '0 % generation'
    if theta <= 15:
        return '100 % generation'
    if 15 < theta <=60:
        return '60 % generation'

# Задача 2: Диспетчер радіокоманд (match-case)
def dispatch_radio_command(cmd_list: list) -> str:
    """
    Використовує match-case з розширеним розпакуванням:
    - ["PING"] -> "PONG"
    - ["SET_ATTITUDE", roll, pitch, yaw] -> "Attitude set: {roll}, {pitch}, {yaw}"
    - ["REBOOT", "FORCE"] -> "Forced reboot"
    """
    match cmd_list:
        case ["PING"]:
            return 'PONG'
        case ["SET_ATTITUDE", *params]:
            return f"Attitude set: {params[0]:.2f}, {params[1]:.2f}, {params[2]:.2f}" 
        case ["REBOOT", "FORCE"]:
            return "Forced reboot"

# Задача 3: Перевірка каналів зв'язку (for / else)
def check_communication_channels(channels: list) -> str:
    """
    Перебирає список каналів. Якщо є True -> перериває break і повертає "Канал {idx} активний".
    Якщо активних немає -> через else повертає "Аварія: немає зв'язку".
    """
    for channel in enumerate(channels):
        if channel[1]:
            return f'Channel {channels.index(channel[1])+1} is active' #повертає номер елемента
            break
        else:
            if channel[0]==len(channels)-1: 
                return 'Аварія: немає зв`язку'

# Задача 4: Калібрування акселерометра на місці (range)
def calibrate_accelerometer_inplace(data: list) -> list:
    """
    Модифікує елементи списку data "на місці", додаючи +0.05 до кожного елемента через range(len(data)).
    """
    ...
