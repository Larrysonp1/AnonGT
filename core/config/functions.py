from os import getuid,system,path
from requests import get
import tempfile
import subprocess
from core.assets.alerts import *
from core.config.config import BACKUPDIR
from core.config.config import VERSION


# check root
def check_root():
    if getuid() != 0:
        ERROR("This script must be run as root")
        exit(1)


# execute command
def exec_command(cmd):
    system(cmd)


# clear terminal
def clear():
    system("clear")


# get terminal output
def get_process(cmd):
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd, stdout=tempf)
        proc.wait()
        tempf.seek(0)
        result = tempf.read().decode("utf-8").strip()
        return result

# get current user
def get_user():
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen("users", stdout=tempf)
        proc.wait()
        tempf.seek(0)
        result = tempf.read().decode("utf-8").strip()
        return result.split()[0]



# check if started
def is_started():
    if path.isfile(f"{BACKUPDIR}/started"):
        # Started
        return 1
    else:
        # Not Started
        return 0


# get anongt is-started
def anongt_isactive():
    if is_started() == 1:
        return f"{red('AnonGT:')} {green('started')}"

    else:
        return f"{red('AnonGT:')}  {yellow('stopped')}"


# get tor service is-active
def tor_isacttive():
    cmd = ["systemctl", "is-active", "tor"]
    TORSTATUS = get_process(cmd)

    if TORSTATUS == "active":
        return f"{red('TOR:')} {green(TORSTATUS)}"

    else:
        return f"{red('TOR:')} {yellow(TORSTATUS)}"


# check update
def check_update():
    MSG(f"Version: {VERSION}")
    MSG("Checking Update...")

    try:
        result = get(
            "https://raw.githubusercontent.com/GT0Day/AnonGT/main/version.txt",
            verify=True,
        ).content
        v = result.decode("utf-8").strip("\n")

        if v != VERSION:
            WARN("Please Update AnonGT!")
            INFO(f"VERSION: {v}")
            INFO("Go to https://github.com/GT0Day/AnonGT")
        else:
            MSG("AnonGT Latest Version.")

    except Exception as e:
        ERROR(e)
    except:
        ERROR("Please Check Your Internet Connection")


# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return str1.join(s)
