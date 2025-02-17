#!/usr/bin/env python3
from core.scripts.Anonymous import Anonymous
from core.scripts.Onion import ONION
from core.scripts.OnionShare import OnionShare
from core.scripts.Encryption import encrypt_file_aes, decrypt_file_aes, encrypt_folder_aes, decrypt_folder_aes, getpass
from core.scripts.Keylogger import start_keylogger, stop_keylogger
from core.assets.banners import HomeBanner, AnonymousModeBanner, DarkWebBanner,OnionShareBanner, EncryptionBanner, KeyloggerBanner,logo, UpdateLogo, AnonymousLogo
from core.config.functions import clear, check_root, check_update, is_started, ERROR, exec_command
from core.assets.about import about
from core.assets.colors import red
from core.assets.alerts import MSG

def AnonGT():
    check_root()
    while 1:
        try:
            # ========================= MAIN MENU ========================= #
            clear()
            print(HomeBanner())
            choice = int(input(red("[AnonGT] ")))

            # Anonymous Mode
            if choice == 1:
                while 1:
                    try:
                        clear()
                        print(AnonymousModeBanner())
                        choice = int(input(red("[AnonGT/Anonymous] ")))
                        if choice == 1:
                            # Anonymous Mode Start
                            Anonymous.Start(1)
                            input(red("Press enter to continue"))

                        elif choice == 2:
                            # Anonymous Mode Start With Secure Tor Bridges
                            Anonymous.StartPlus(1)
                            input(red("Press enter to continue"))

                        elif choice == 3:
                            # Anonymous Mode Stop
                            Anonymous.Stop(1)
                            input(red("Press enter to continue"))

                        elif choice == 4:
                            # Watch Tor Traffic
                            Anonymous.Status(1)
                            input(red("Press enter to continue"))

                        elif choice == 5:
                            # Get Your #IP Address
                            Anonymous.MyIP(1)
                            input(red("Press enter to continue"))

                        elif choice == 6:
                            # Change Tor Identity
                            Anonymous.Change_ID(1)
                            input(red("Press enter to continue"))

                        elif choice == 7:
                            # Change #IP Automatically
                            # Check IF Stopped
                            if is_started() == 0:
                                ERROR("Anonymous Mode is already stopped")
                            else:
                                exec_command(
                                    f"sudo xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'AnonGT Auto #IP Changer' -geometry 150x35 -e 'sudo python3 /usr/share/AnonGT/core/sources/auto-change.py' &")
                            input(red("Press enter to continue"))

                        elif choice == 8:
                            # Memory Wipe & Clear Logs
                            Anonymous.Wipe(1)
                            input(red("Press enter to continue"))

                        elif choice == 9:
                            # Fix If Shutdown Without Stop
                            Anonymous.Fix(1)
                            input(red("Press enter to continue"))

                        elif choice == 0:
                            break
                    except KeyboardInterrupt:
                        continue
                    except ValueError:
                        continue

            # DarkWeb
            elif choice == 2:
                while 1:
                    try:
                        clear()
                        print(DarkWebBanner())
                        choice = int(input(red("[AnonGT/DarkWeb] ")))
                        if choice == 1:
                            # Search Engine
                            query = input(red("Enter your search query: "))
                            ONION.ahmia_engine(query)
                            input(red("Press enter to continue"))

                        elif choice == 2:
                            # Onion Links Checker
                            clear()
                            print(red(logo))
                            ONION.check(1)
                            input(red("Press enter to continue"))

                        elif choice == 0:
                            break
                    except KeyboardInterrupt:
                        continue
                    except ValueError:
                        continue

            # Onion Share
            elif choice == 3:
                while 1:
                    try:
                        clear()
                        print(OnionShareBanner())
                        choice = int(input(red("[AnonGT/OnionShare] ")))
                        if choice == 1:
                            # Anonymous Share Files
                            OnionShare.Share(1)
                            input(red("Press enter to exit"))

                        if choice == 2:
                            # Anonymous Receive Files
                            OnionShare.Receive(1)
                            input(red("Press enter to exit"))

                        if choice == 3:
                            # Anonymous Chat
                            OnionShare.Chat(1)
                            input(red("Press enter to exit"))

                        if choice == 4:
                            # Host A Website
                            OnionShare.Website(1)
                            input(red("Press enter to exit"))

                        elif choice == 0:
                            break
                    except KeyboardInterrupt:
                        continue
                    except ValueError:
                        continue
            # Encryption
            elif choice == 4:
                while 1:
                    try:
                        clear()
                        print(EncryptionBanner())
                        choice = int(input(red("[AnonGT/Encryption] ")))

                        # Encrypt File (AES with Password)
                        if choice == 1:
                            file_path = input(red("Enter file path: "))
                            password = getpass.getpass(red("Enter encryption password: "))
                            encrypt_file_aes(file_path, password)
                            input(red("Press enter to continue"))

                        # Decrypt File (AES with Password)
                        elif choice == 2:
                            file_path = input(red("Enter encrypted file path: "))
                            password = getpass.getpass(red("Enter decryption password: "))
                            decrypt_file_aes(file_path, password)
                            input(red("Press enter to continue"))

                        # Encrypt Folder (AES with Password)
                        elif choice == 3:
                            folder_path = input(red("Enter folder path: "))
                            password = getpass.getpass(red("Enter encryption password: "))
                            encrypt_folder_aes(folder_path, password)
                            input(red("Press enter to continue"))

                        # Decrypt Folder (AES with Password)
                        elif choice == 4:
                            file_path = input(red("Enter encrypted folder file path: "))
                            password = getpass.getpass(red("Enter decryption password: "))
                            decrypt_folder_aes(file_path, password)
                            input(red("Press enter to continue"))

                        elif choice == 0:
                            break
                    except KeyboardInterrupt:
                        continue
                    except ValueError:
                        continue

            # Keylogger
            elif choice == 5:
                while 1:
                    try:
                        clear()
                        print(KeyloggerBanner())
                        choice = int(input(red("[AnonGT/Keylogger] ")))

                        # Start Keylogger
                        if choice == 1:
                            start_keylogger()
                            input()

                        # Stop Keylogger
                        elif choice == 2:
                            stop_keylogger()
                            input()

                        elif choice == 0:
                            break

                    except KeyboardInterrupt:
                        continue
                    except ValueError:
                        continue

            # Check Update
            elif choice == 6:
                try:
                    clear()
                    print(red(UpdateLogo))
                    check_update()
                    input(red("Press enter to continue"))
                except KeyboardInterrupt:
                    continue
                except ValueError:
                    continue

            # About US
            elif choice == 7:
                try:
                    clear()
                    print(red(AnonymousLogo))
                    print(about())
                    input(red("Press enter to continue"))
                except KeyboardInterrupt:
                    continue
                except ValueError:
                    continue

            elif choice == 0:
                break

            else:
                continue

        except KeyboardInterrupt:
            continue
        except ValueError:
            continue




if __name__ == "__main__":
    AnonGT()