import os

dirname = os.path.dirname(__file__)

USER_REPOSITORY_FILENAME = os.getenv('USER_REPOSITORY_FILENAME') or 'user_repository.dat'
USER_REPOSITORY_FILE_PATH = os.path.join(dirname, 'data', USER_REPOSITORY_FILENAME)