import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
CONFIG_PATH = os.path.join(ROOT_DIR, 'configuration.conf')
TEMP_PATH = os.path.join(ROOT_DIR, 'tmp')
DATABASE_CONFIG_PATH = os.path.join(ROOT_DIR, 'database_config.ini')