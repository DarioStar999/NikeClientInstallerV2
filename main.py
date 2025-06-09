import customtkinter as tk
import os
import subprocess
import threading
import json
import requests

username = os.getlogin()

app = tk.CTk()
app.title(f"Benvenuto {username}")
app.geometry("500x400")
app.resizable(False, False)

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

frame = tk.CTkFrame(app, corner_radius=15)
frame.pack(expand=True, fill="both", padx=20, pady=20)

title = tk.CTkLabel(frame, text="NikeClient Launcher", font=("Arial", 22, "bold"))
title.pack(pady=(10, 20))

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
    progress_window.geometry("350x120")
    label = tk.CTkLabel(progress_window, text="Download in corso...")
    label.pack(pady=10)
    progress = tk.CTkProgressBar(progress_window, width=280)
    progress.set(0)
    progress.pack()
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
        else:
            save_path = os.path.join(mods_path, filename)
        download_file_con_barra(url, save_path, progress, index, total_files)
    label.configure(text="Download completato ✅")
    progress.set(1.0)

def download_spremium():
    files = [
        ("https://dariostar999.github.io/assets/src/NikeClient.jar", "NikeClient.jar"),
        ("https://dariostar999.github.io/assets/src/Cosmetics.jar", "Cosmetics.jar"),
        ("https://dariostar999.github.io/assets/src/FpsBoost.jar", "FpsBoost.jar"),
        ("https://dariostar999.github.io/assets/src/gui.jar", "gui.jar")
    ]
    progress_window = tk.CTkToplevel(app)
    progress_window.title("Download S-Premium in corso...")
    progress_window.geometry("350x120")
    label = tk.CTkLabel(progress_window, text="Download in corso...")
    label.pack(pady=10)
    progress = tk.CTkProgressBar(progress_window, width=280)
    progress.set(0)
    progress.pack()
    mods_path = os.path.join(os.environ["APPDATA"], ".minecraft", "mods")
    os.makedirs(mods_path, exist_ok=True)
    total_files = len(files)
    for index, (url, filename) in enumerate(files, start=1):
        save_path = os.path.join(mods_path, filename)
        download_file_con_barra(url, save_path, progress, index, total_files)
    label.configure(text="Download completato ✅")
    progress.set(1.0)

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
                toggled_value = mod["toggled"]
                break
        with open(location, "w") as settings:
            json.dump(data, settings, indent=4)
        notif = tk.CTkLabel(settingsAPP, text=f"Mod '{choice}' toggled: {toggled_value}",
                            fg_color="#2ecc71", text_color="white", corner_radius=8, font=("Arial", 14),
                            width=250, height=30)
        notif.place(relx=0.5, rely=0.85, anchor="center")
        settingsAPP.after(3000, notif.destroy)

    tk.CTkOptionMenu(settingsAPP, values=[
        "FPS", "ToggleSprint", "ToggleSneak", "Keystrokes", "Armor Status", "Fullbright",
        "Snaplook", "Coordinates", "Server Address", "Ping", "CPS", "Speed Indicator",
        "Animation", "Freelook", "Crosshair", "Motionblur", "BlockOverlay"
    ], command=settingSet).grid(column=0, row=1, sticky="w", padx=10, pady=10)

    tk.CTkButton(settingsAPP, text="Esci", command=exitSettings).grid(column=0, row=2, sticky="w", padx=10)
    settingsAPP.mainloop()

def settings_thread():
    threading.Thread(target=show_settings, daemon=True).start()

def dowload(choice):
    if choice == "senza premium":
        threading.Thread(target=download_spremium, daemon=True).start()
    elif choice == "premium":
        threading.Thread(target=download_premium, daemon=True).start()

def start_launcher():
    launcher_path = r"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe"
    if os.path.exists(launcher_path):
        subprocess.Popen([launcher_path])
    else:
        tk.CTkLabel(frame, text="Launcher non trovato ❌", text_color="red").pack(pady=(5, 0))

optionmenu = tk.CTkOptionMenu(frame, values=["premium", "senza premium"], command=dowload)
optionmenu.pack(pady=10)
optionmenu.set("Seleziona versione")

tk.CTkButton(frame, text="⚙️ Impostazioni", command=settings_thread).pack(pady=(5, 5))

tk.CTkButton(frame, text="⬇️ Scarica", command=lambda: dowload(optionmenu.get())).pack(pady=(0, 10))

tk.CTkButton(frame, text="▶ Avvia Minecraft", command=start_launcher, fg_color="#27ae60", hover_color="#219150").pack(pady=(5, 10))

footer = tk.CTkLabel(frame, text="Made with ❤️ by te", font=("Arial", 10), text_color="gray")
footer.pack(side="bottom", pady=(10, 5))

app.mainloop()
