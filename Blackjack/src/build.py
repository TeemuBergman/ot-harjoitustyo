from repositories.user_repository import UserRepository


def build():
    file_init = UserRepository()
    file_init.init_user_settings()


if __name__ == '__main__':
    build()
