import subprocess
import constants


def signal_handler():
    print('You pressed Ctrl+C!')


def spawn_chrome_browser():

    chrome_process = subprocess.Popen(
        [constants.chrome_path, f'--user-data-dir={constants.chrome_tmp_path}'])

    print("Chrome process started", chrome_process)
    return chrome_process
