import os


PROJECT_PATH = os.path.abspath(os.path.join(__file__, *(os.path.pardir,) * 2))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, '{{ cookiecutter.project_name }}')
COOKIECUTTER_CONFIG_PATH = os.path.join(PROJECT_PATH, 'cookiecutter.json')
