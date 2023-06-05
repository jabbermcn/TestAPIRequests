import logging

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для вывода логов в терминал
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Создание форматировщика
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(console_handler)
