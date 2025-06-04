import customtkinter as tk
import os
import subprocess
import threading
import textwrap
import json
import time
import requests

username = os.getlogin()
app = tk.CTk()
app.title(f"{username} benvenuto")
app.geometry("300x200")
app.grid_columnconfigure(0, weight=1)
app.resizable(False, False)

def download_file_con_barra(url, save_path, progress_bar, current_index, total_files):
    filename = os.path.basename(save_path)
    if "install.ps1" in filename:
        save_path = os.path.join(os.environ["USERPROFILE"], "Downloads", filename)
    response = requests.get(url, stream=True)
    total_length = int(response.headers.get('content-length', 0))
    downloaded = 0
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=4096):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                progress = ((current_index - 1) + downloaded / total_length) / total_files
                progress_bar.set(progress)
    if "install.ps1" in filename:
        subprocess.Popen([
            "powershell.exe",
            "-ExecutionPolicy", "Bypass",
            "-File", save_path
        ])

def download_premium():
    files = [
        ("https://dariostar999.github.io/assets/src/1.8.9-forge1.8.9-11.15.1.2318-1.8.9.jar", "1.8.9-forge.jar"),
        ("https://dariostar999.github.io/assets/src/1.8.9-forge1.8.9-11.15.1.2318-1.8.9.json", "1.8.9-forge.json"),
        ("https://dariostar999.github.io/assets/src/1.8.9.jar", "1.8.9.jar"),
        ("https://dariostar999.github.io/assets/src/logs.txt", "logs.txt"),
        ("https://dariostar999.github.io/assets/src/forge-1.8.9-11.15.1.2318-1.8.9.jar", "forge.jar"),
        ("https://dariostar999.github.io/assets/src/install.ps1", "install.ps1"),
        ("https://dariostar999.github.io/assets/src/NikeClient.jar", "NikeClient.jar"),
        ("https://dariostar999.github.io/assets/src/Cosmetics.jar", "Cosmetics.jar"),
        ("https://dariostar999.github.io/assets/src/FpsBoost.jar", "FpsBoost.jar"),
        ("https://dariostar999.github.io/assets/src/gui.jar", "gui.jar")
    ]
    progress_window = tk.CTkToplevel(app)
    progress_window.title("Download in corso...")
    progress_window.geometry("300x100")
    progress_label = tk.CTkLabel(progress_window, text="Download in corso...")
    progress_label.pack(pady=10)
    progress_bar = tk.CTkProgressBar(progress_window, width=250)
    progress_bar.set(0)
    progress_bar.pack(pady=5)
    mcpath = os.path.join(os.environ["APPDATA"], ".minecraft")
    mods_path = os.path.join(mcpath, "NikeClient", "mods")
    os.makedirs(mods_path, exist_ok=True)
    total_files = len(files)
    for index, (url, filename) in enumerate(files, start=1):
        if "install.ps1" in filename:
            save_path = os.path.join(os.environ["USERPROFILE"], "Downloads", filename)
        elif filename in ["1.8.9-forge.jar", "1.8.9-forge.json", "1.8.9.jar"]:
            save_path = os.path.join(mcpath, "versions", "1.8.9-forge", filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
        elif filename == "forge.jar":
            save_path = os.path.join(mcpath, "libraries", "net", "minecraftforge", "forge", "1.8.9-11.15.1.2318-1.8.9", filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
        elif filename == "logs.txt":
            save_path = os.path.join(mods_path, filename)
        else:
            save_path = os.path.join(mods_path, filename)
        download_file_con_barra(url, save_path, progress_bar, index, total_files)
    progress_label.configure(text="Download completato ✅")
    progress_bar.set(1.0)

def download_spremium():
    files = [
        ("https://dariostar999.github.io/assets/src/NikeClient.jar", "NikeClient.jar"),
        ("https://dariostar999.github.io/assets/src/Cosmetics.jar", "Cosmetics.jar"),
        ("https://dariostar999.github.io/assets/src/FpsBoost.jar", "FpsBoost.jar"),
        ("https://dariostar999.github.io/assets/src/gui.jar", "gui.jar")
    ]
    progress_window = tk.CTkToplevel(app)
    progress_window.title("Download S-Premium in corso...")
    progress_window.geometry("300x100")
    progress_label = tk.CTkLabel(progress_window, text="Download in corso...")
    progress_label.pack(pady=10)
    progress_bar = tk.CTkProgressBar(progress_window, width=250)
    progress_bar.set(0)
    progress_bar.pack(pady=5)
    mcpath = os.path.join(os.environ["APPDATA"], ".minecraft")
    mods_path = os.path.join(mcpath, "mods")
    os.makedirs(mods_path, exist_ok=True)
    total_files = len(files)
    for index, (url, filename) in enumerate(files, start=1):
        save_path = os.path.join(mods_path, filename)
        download_file_con_barra(url, save_path, progress_bar, index, total_files)
    progress_label.configure(text="Download completato ✅")
    progress_bar.set(1.0)

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
                toggled_value = mod["toggled"]  # Salvo valore per la notifica
                break

        with open(location, "w") as settings:
            json.dump(data, settings, indent=4)
            
        notif = tk.CTkLabel(settingsAPP, text=f"Mod '{choice}' toggled: {toggled_value}",
                            fg_color="#2ecc71", text_color="white", corner_radius=8, font=("Arial", 14),
                            width=250, height=30)
        notif.place(relx=0.5, rely=0.85, anchor="center")

        settingsAPP.after(3000, notif.destroy)
    exit_button = tk.CTkButton(settingsAPP, text="Exit", command=exitSettings)
    exit_button.grid(column=0, row=2, sticky="w")
    settingoptionmenu = tk.CTkOptionMenu(settingsAPP, values=["FPS", "ToggleSprint", "ToggleSneak", "Keystrokes", "Armor Status", "Fullbright", "Snaplook", "Coordinates", "Server Address", "Ping", "CPS", "Speed Indicator", "Animation", "Freelook", "Crosshair", "Motionblur", "BlockOverlay"], command=settingSet)
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
