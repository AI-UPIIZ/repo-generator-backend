import os

PROJECT_PATH = os.path.abspath(os.path.join(__file__, *(os.path.pardir,) * 2))
DATA_PATH = os.path.join(PROJECT_PATH, "data")
OUTPUT_PATH = os.path.join(PROJECT_PATH, "mlruns")
CONFIG_PATH = os.path.join(PROJECT_PATH, "config")


class Paths:
    dataset_path = os.path.join(DATA_PATH, "dataset")
    models_path = os.path.join(OUTPUT_PATH, "models")
