from sys import platform
from utils.log_utils import logger


class Config:

    @staticmethod
    def mode(mode_selection):
        def check_os():
            logger.info(f'Host Operating System Detected: {platform}')
            if platform == "linux" or platform == "linux2" or platform == "darwin":
                return "linux"

            elif platform == "win32" or platform == "win64":
                return "windows"
            else:
                return "windows"

        os_env = check_os()

        if mode_selection == 'development':
            return 1
        elif mode_selection == 'production':
            return 3
        elif mode_selection == 'staging':
            return 2
        elif mode_selection == 'testing':
            return 4

    @staticmethod
    def environment(mode_selection):
        if mode_selection == 'development':
            from environment import development
            return development
        elif mode_selection == 'production':
            from environment import production
            return production
        elif mode_selection == 'staging':
            from environment import staging
            return staging


if __name__ == '__main__':
    pass
