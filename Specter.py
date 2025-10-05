import os
import shutil
import getpass

def spectertop():
    print("""
███████╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████╗██████╔╝█████╗  ██║        ██║   █████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗
███████║██║     ███████╗╚██████╗   ██║   ███████╗██║  ██║
╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")

def show_menu():
    print("\033[92m[1] > Очистить файлы в диске С: (.wexside, ExcellentRecode и т.д)") #zzzz
    print("[2] > Очистить файлы в папке .minecraft (котлован не очищаит)") # workaet
    print("[3] > Очистить %temp%") # works
    print("[4] > Ресурспаки") # works
    print("[5] > accounts.json (lunarclient)") # works
    print("[6] > Модификации") #works
    print("[7] > TopkaProduct") # works
    print("[9] > Автор") # works
    print("[10] > Гитхаб") # nn


def lunar():
    print("https://www.dropbox.com/scl/fi/m62apm8aqcwrte2zqayjr/accounts.json?rlkey=tc41zq66uuikhmrcqdfy920zb&st=m4jy1pdx&dl=1 \n(вставь в браузер)")
    input("Нажмите enter что-б выйти")

def mainchistilka():
        disk_ce = os.path.join("C\\")
        wexside_bust = os.path.join(disk_ce, ".wexside")
        cotlovan = os.path.join(disk_ce, "цвццвцв")
        deltaclient = os.path.join(disk_ce, "delta")
     #   shevulchina = os.path.join(disk.ce, "excellent")

        try:
            if os.path.exists(wexside_bust):
                shutil.rmtree(wexside_bust)
                print("[+] wexside удалён.")
            else:
                print("[!] Не найдена папка чита wexside  .")

                if os.path.exists(deltaclient):
                    shutil.rmtree(deltaclient)
                    print("[+] Папка чита удалена (deltaclient).")
                else:
                    print("[!] Папка чита не нашлась (deltaclient).")



            if os.path.exists(cotlovan):
                shutil.rmtree(cotlovan)
                print("[+] Папка чита удалена (catlavan).")
            else:
                print("[!] Папка Чита не найдена (catlavan).")
        except Exception as e:
            print(f"[Ошибка] Не удалось удалить (catlavan): {e}")



        input("Нажмите Enter для выхода...")


def cleaner_barik():
    print("[!] Успешно, Баритон удалён!")
    user_profile = os.getenv('USERPROFILE')
    mcpath = os.path.join(user_profile, "AppData", "Roaming", ".minecraft")
    baritone_path = os.path.join(mcpath, "baritone")
    logs_path = os.path.join(mcpath, "logs")

    try:
        if os.path.exists(baritone_path):
            shutil.rmtree(baritone_path)
            print("[+] Baritone удалён.")
        else:
            print("[!] Папка Baritone не найдена.")
            print("[!] Не найдено .wexside .")

        if os.path.exists(logs_path):
            shutil.rmtree(logs_path)
            print("[+] Logs удалены.")
        else:
            print("[!] Папка Logs не найдена.")
    except Exception as e:
        print(f"[Ошибка] Не удалось удалить: {e}")

    input("Нажмите Enter для выхода...")


def cleaner_expa():
    expansiec = os.path.join(mcpath, "expensive")
    print("[!] Успешно, baritone и т.д удалены!")
    try:
        shutil.rmtree(baritone_path)
        shutil.rmtree(expansiec)
    except Exception as e:
        print(f" Не удалось удалить файл baritone: {e}")

    input("Нажмите Enter для выхода...")


def temp_cleaner():
    temp_path = os.getenv('TEMP')
    print("[*] Удаляю %TEMP%...")
    try:
        for filename in os.listdir(temp_path):
            path = os.path.join(temp_path, filename)
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
            except Exception as e:
                print(f"Не удалось : {path}: {e}")
        print("[+] temp очищен!")
    except Exception as e:
        print(f"[Ошибка] {e}")
    input("Нажмите Enter для выхода...")



username = getpass.getuser()
mcpath = os.path.join("C:\\Users", username, "AppData", "Roaming", ".minecraft")
baritone_path = os.path.join(mcpath, "baritone")

spectertop()
show_menu()
vibor = input("> ")

if vibor == "1":
    mainchistilka()
elif vibor == "2":
    cleaner_barik()
elif vibor == "3":
    temp_cleaner()
elif vibor == "4":
    print("Bedrock & java: t.me/rpParkipack  ")
    input("by @")
elif vibor == "5":
    lunar()
elif vibor == "8":
    donat()
elif vibor == "9":
   cleaner_barik()
elif vibor == "7":
    print("@topkamod_bot")
    input("Нажмите enter что-б выйти")

elif vibor == "6":
    print("t.me/collapseloader \nt.me/download_cheats")
    input("Нажмите enter что-б выйти")

elif vibor == "10":
    print("https://github.com/utcsvc/Specter-Tool")
    input("Нажмите enter что-б выйти")
else:
    print("[!] Неизвестный выбор.")
    input("Нажмите enter что-б выйти")


