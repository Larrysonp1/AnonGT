from os import path
from core.config.functions import is_started, exec_command
from core.assets.alerts import ERROR, green, yellow

class OnionShare():
    def Share(self):
        # check if stopped
        if is_started() == 0:
            share = input(green("Submit the URL File/Folder: "))
            if path.exists(share):
                cmd = input(
                    f"{yellow('Do you want share with public? (Default: private) ')} "
                ).lower()
                if cmd == "y":
                    exec_command(f"onionshare-cli {share} --public")
                else:
                    exec_command(
                        f"onionshare-cli {share}")
        else:
            ERROR("Must AnonGT Be Stopped.")

    def Receive(self):
        # check if stopped
        if is_started() == 0:
            cmd = input(
                f"{yellow('Do you want receive with public? (Default: private) ')} "
            ).lower()
            if cmd == "y":
                exec_command(
                    f"onionshare-cli --receive --public")
            else:
                exec_command(
                    f"onionshare-cli --receive")
        else:
            ERROR("Must AnonGT Be Stopped.")

    def Chat(self):
        # check if stopped
        if is_started() == 0:
            cmd = input(
                f"{yellow('Do you want receive with public? (Default: private) ')} "
            ).lower()
            if cmd == "y":
                exec_command(
                    f"onionshare-cli --chat --public")
            else:
                exec_command(
                    f"onionshare-cli --chat")
        else:
            ERROR("Must AnonGT Be Stopped.")

    def Website(self):
        # check if stopped
        if is_started() == 0:
            website = input(green("Submit the URL Folder Of Website: "))
            if path.exists(website):
                cmd = input(
                    f"{yellow('Do you want share with public? (Default: private) ')} "
                ).lower()
                if cmd == "y":
                    exec_command(
                        f"onionshare-cli --website {website} --public")
                else:
                    exec_command(
                        f"onionshare-cli --website {website}")
            else:
                ERROR("Must AnonGT Be Stopped.")
