from dotenv import load_dotenv
from os import getenv
from os.path import abspath, dirname, sep, exists


PROJECT_NAME = getenv('PROJECT_NAME', 'Example')
API_PORT = int(getenv('API_PORT', '5000'))

SECRET_KEY = getenv(
    'SECRET_KEY',
    'BJeoP/3zVHPWJwnmeRurIt27vb8nu0M98BpYJE3xFE=' # noqa
)
ALGORITHM = getenv('ALGORITHM', 'HS256')
TOKEN_EXPIRE_MINUTES = int(getenv('TOKEN_EXPIRE_MINUTES', '30'))

ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))

ENV_FILE = ROOT_PATH + sep + ".env"

if exists(ENV_FILE):
    load_dotenv(dotenv_path=ENV_FILE)


def get_dsn(database_file: str) -> str:
    database_path = ROOT_PATH + sep + 'app' + sep + database_file
    return f'sqlite+aiosqlite:///{database_path}'


DATABASE_FILE = getenv('DATABASE_FILE', 'sqlite_example.db')
DSN = get_dsn(DATABASE_FILE)

TEST_DATABASE_FILE = getenv('TEST_DATABASE_FILE', 'test_sqlite_example.db')
TEST_DSN = get_dsn(TEST_DATABASE_FILE)

DB_CLEAR_AT_THE_END = getenv("CLEAR_DB_AT_THE_END", 'False').lower() \
                      in ('true', '1', 't')

TIME_HEADER_LOGGING = getenv("TIME_HEADER_LOGGING", 'False').lower() \
                      in ('true', '1', 't')

MODE = getenv('MODE', 'DEV')  # DEV / TEST / PROD

LOG_LEVEL = getenv('LOG_LEVEL', 'INFO')  # INFO / DEBUG

SENTRY_DSN = getenv('SENTRY_DSN', None)
