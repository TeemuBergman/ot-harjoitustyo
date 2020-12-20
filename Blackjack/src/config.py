from os import path, getenv

dirname = path.dirname(__file__)

USER_REPOSITORY_FILENAME = getenv('USER_REPOSITORY_FILENAME') or 'user_repository.dat'
USER_REPOSITORY_FILE_PATH = path.join(dirname, 'data', USER_REPOSITORY_FILENAME)
