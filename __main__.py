from gui import LoginWindow
from gui import SignUpWindow
import os.path


if __name__ == "__main__":
    if os.path.exists("pass.kalina"):
        LoginWindow()
    else:
        SignUpWindow()
