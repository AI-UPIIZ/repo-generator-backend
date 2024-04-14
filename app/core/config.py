from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

# Backend metadata
APP_VERSION: str = config('APP_VERSION')
APP_NAME: str = config('APP_NAME')
API_PREFIX: str = config('API_PREFIX')

# API request configuration
API_KEY: str = config('API_KEY', cast=Secret)
IS_DEBUG: bool = config('IS_DEBUG')

# Github configuration
GITHUB_ORG_NAME: str = config('GITHUB_ORG_NAME')
GITHUB_ACCESS_TOKEN: str = config('GITHUB_ACCESS_TOKEN')
