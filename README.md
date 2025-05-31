<h1>Custom Minecraft Mod Downloader</h1>

<p>A user-friendly desktop application built with <strong>CustomTkinter</strong> that allows you to easily download Minecraft mods and manage mod settings.</p>

<h2>Features</h2>
<ul>
  <li>Download Minecraft mod files with progress bar and status updates</li>
  <li>Two download options: <em>Premium</em> (full mod pack) and <em>Without Premium</em> (basic mods)</li>
  <li>Automatically creates required directories in your Minecraft folder</li>
  <li>Launches PowerShell script automatically when needed</li>
  <li>Interactive settings window to toggle individual mod options saved in JSON config</li>
  <li>Runs downloads and settings in separate threads for smooth UI experience</li>
</ul>

<h2>How to Use</h2>
<ol>
  <li>Launch the app; it shows your username in the title bar.</li>
  <li>Select the download option ("premium" or "senza premium") from the dropdown menu.</li>
  <li>Watch the download progress in the popup progress bar window.</li>
  <li>Click <strong>Settings</strong> to toggle mod options interactively.</li>
</ol>

<h2>Requirements</h2>
<ul>
  <li><code>customtkinter</code> library</li>
  <li><code>requests</code> library</li>
  <li>Windows OS (due to PowerShell script integration)</li>
  <li>Python 3.x</li>
</ul>

<h2>Example Screenshot</h2>
<img src="https://i.imgur.com/uuvS4XC" alt="App Screenshot" width="400"/>

<h2>Notes</h2>
<p>Make sure Minecraft is installed and you have access to your <code>%APPDATA%\.minecraft</code> directory. This app automatically handles folder creation and places mods accordingly.</p>
