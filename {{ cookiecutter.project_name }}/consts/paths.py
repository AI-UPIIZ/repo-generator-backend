import os

PROJECT_PATH = os.path.abspath(os.path.join(__file__, *(os.path.pardir,) * 2))
DATA_PATH = os.path.join(PROJECT_PATH, "data")
RAW_DATA = os.path.join(DATA_PATH, "raw")
INTER_DATA = os.path.join(DATA_PATH, "inter")
PRO_DATA = os.path.join(DATA_PATH, "processed")
CONFIG_PATH = CONFIG_PATH = os.path.join(PROJECT_PATH, "config")
