<h1>🧩 NikeClient Installer</h1>

<p>A user-friendly 🖥️ desktop application built with <strong>CustomTkinter</strong> that lets you easily download Minecraft mods 🛠️ and manage your mod settings ⚙️.</p>

<h2>✨ Features</h2>
<ul>
  <li>⬇️ Download Minecraft mod files with a progress bar 📊 and live status updates.</li>
  <li>🎮 Two download options: <em>Premium</em> (full mod pack) and <em>Without Premium</em> (basic mods).</li>
  <li>🗂️ Automatically creates the required folders in your <code>.minecraft</code> directory.</li>
  <li>⚡ Launches a PowerShell script automatically when needed.</li>
  <li>🛠️ Interactive settings window to toggle mod options stored in a JSON config.</li>
  <li>🧵 Runs downloads and settings in separate threads for a smooth and responsive UI experience.</li>
</ul>

<h2>📌 How to Use</h2>
<ol>
  <li>🚀 Launch the app — your username will appear in the title bar.</li>
  <li>🎯 Select the download option (<code>premium</code> or <code>senza premium</code>) from the dropdown menu.</li>
  <li>📈 Watch the download progress in the popup window.</li>
  <li>⚙️ Click <strong>Settings</strong> to toggle individual mod options interactively.</li>
</ol>

<h2>🧰 Requirements</h2>
<ul>
  <li><code>customtkinter</code> 📦</li>
  <li><code>requests</code> 📦</li>
  <li>💻 Windows OS (due to PowerShell integration)</li>
  <li>🐍 Python 3.x</li>
</ul>

<h2>🖼️ Example Screenshot</h2>
<img src="https://i.imgur.com/2SGaM4e_d.webp?maxwidth=760&fidelity=grand" alt="App Screenshot" width="400"/>

<h2>📝 Notes</h2>
<p>Make sure Minecraft is installed 🎮 and you have access to your <code>%APPDATA%\.minecraft</code> directory. The app automatically handles folder creation and places mods correctly 📂.</p>
