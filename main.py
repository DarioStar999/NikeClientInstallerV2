import customtkinter as tk
import os
import subprocess
import threading
import textwrap
import json

username = os.getlogin()
app = tk.CTk()
app.title(f" benvenuto")
app.geometry("300x200")
app.grid_columnconfigure(0, weight=1)
app.resizable(False, False)

def download_premium():
    script = textwrap.dedent("""\
        set "minecraftpath=C:\\Users\\%username%\\AppData\\Roaming\\.minecraft"
        set "versionpath=%minecraftpath%\\versions"
        mkdir "%versionpath%\\1.8.9-forge1.8.9-11.15.1.2318-1.8.9" > nul
        mkdir "%minecraftpath%\\libraries\\net\\minecraftforge" > nul
        mkdir "%minecraftpath%\\libraries\\net\\minecraftforge\\forge" > nul
        mkdir "%minecraftpath%\\libraries\\net\\minecraftforge\\forge\\1.8.9-11.15.1.2318-1.8.9" > nul
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/1.8.9-forge1.8.9-11.15.1.2318-1.8.9.jar' -OutFile '%versionpath%\\1.8.9-forge1.8.9-11.15.1.2318-1.8.9\\1.8.9-forge1.8.9-11.15.1.2318-1.8.9.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/1.8.9-forge1.8.9-11.15.1.2318-1.8.9.json' -OutFile '%versionpath%\\1.8.9-forge1.8.9-11.15.1.2318-1.8.9\\1.8.9-forge1.8.9-11.15.1.2318-1.8.9.json' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/1.8.9.jar' -OutFile '%versionpath%\\1.8.9-forge1.8.9-11.15.1.2318-1.8.9\\1.8.9.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/logs.txt' -OutFile '%minecraftpath%\\NikeClient\\mods\\logs.txt' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/forge-1.8.9-11.15.1.2318-1.8.9.jar' -OutFile '%minecraftpath%\\libraries\\net\\minecraftforge\\forge\\1.8.9-11.15.1.2318-1.8.9\\forge-1.8.9-11.15.1.2318-1.8.9.jar' }"
        mkdir "%minecraftpath%\\NikeClient" > nul
        mkdir "%minecraftpath%\\NikeClient\\mods" > nul
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/install.ps1' -OutFile 'C:\\Users\\%username%\\Downloads\\install.ps1' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/NikeClient.jar' -OutFile '%minecraftpath%\\NikeClient\\mods\\NikeClient.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/Cosmetics.jar' -OutFile '%minecraftpath%\\NikeClient\\mods\\Cosmetics.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/FpsBoost.jar' -OutFile '%minecraftpath%\\NikeClient\\mods\\FpsBoost.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/gui.jar' -OutFile '%minecraftpath%\\NikeClient\\mods\\gui.jar' }"
    """).lstrip()
    process = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, shell=False)
    process.communicate(input=script.encode("utf-8"))
    download_folder = os.path.join(os.environ["USERPROFILE"], "Downloads")
    ps1_script = os.path.join(download_folder, "install.ps1")
    process2 = subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps1_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process2.communicate(input=script.encode("utf-8"))

def download_spremium():
    script = textwrap.dedent(r"""\
        set "minecraftpath=C:\Users\%username%\AppData\Roaming\.minecraft"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/NikeClient.jar' -OutFile '%minecraftpath%\mods\NikeClient.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/Cosmetics.jar' -OutFile '%minecraftpath%\mods\Cosmetics.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/FpsBoost.jar' -OutFile '%minecraftpath%\mods\FpsBoost.jar' }"
        powershell -Command "& { Invoke-WebRequest -Uri 'https://dariostar999.github.io/assets/src/gui.jar' -OutFile '%minecraftpath%\mods\gui.jar' }"
    """).lstrip() + "\n"
    process = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, shell=False)
    process.communicate(input=script.encode("utf-8"))

def show_settings():
    username = os.getlogin()
    settingsAPP = tk.CTk()
    settingsAPP.title("Settings")
    settingsAPP.geometry("300x200")
    settingsAPP.resizable(False, False)
    def exitSettings():
        settingsAPP.destroy()
    location = rf"C:\Users\{username}\AppData\Roaming\.minecraft\NikeClient\cloud\config.json"
    try:
        with open(location, "r") as settings:
            data = json.load(settings)
    except FileNotFoundError:
        print("File di configurazione non trovato.")
        settingsAPP.destroy()
        return
    def settingSet(choice):
        for mod in data["modConfigList"]:
            if mod["name"] == choice:
                mod["toggled"] = not mod["toggled"]
        with open(location, "w") as settings:
            json.dump(data, settings, indent=4)
    exit_button = tk.CTkButton(settingsAPP, text="Exit", command=exitSettings)
    exit_button.grid(column=0, row=2, sticky="w")
    settingoptionmenu = tk.CTkOptionMenu(settingsAPP, values=["FPS", "ToggleSprint"], command=settingSet)
    settingoptionmenu.grid(column=0, row=1, sticky="w")
    settingsAPP.mainloop()

def settings_thread():
    threading.Thread(target=show_settings, daemon=True).start()

def dowload(choice):
    if choice == "senza premium":
        threading.Thread(target=download_spremium, daemon=True).start()
        optionpremiumSP.destroy()
    elif choice == "premium":
        threading.Thread(target=download_premium, daemon=True).start()
        optionpremiumSP.destroy()

optionpremiumSP = tk.CTkOptionMenu(app, values=["premium", "senza premium"], command=dowload)
optionpremiumSP.grid(column=0, row=0, columnspan=2, pady=1)
optionpremiumSP.set("seleziona(solo una volta)")
settings_button = tk.CTkButton(app, text="Settings", command=settings_thread)
settings_button.grid(row=2, column=0, columnspan=2, pady=1)

app.mainloop()