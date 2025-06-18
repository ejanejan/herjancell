Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import zipfile
import os

# Struktur direktori virtual yang akan dikompresi
base_dir = "/mnt/data/HerjanCellUnlocker"
os.makedirs(f"{base_dir}/tools", exist_ok=True)
os.makedirs(f"{base_dir}/assets", exist_ok=True)

... # Isi file tools .bat
... unlock_bat = "@echo off\necho [*] Unlocking Bootloader...\nadb wait-for-device\nfastboot oem unlock\npause"
... relock_bat = "@echo off\necho [*] Relocking Bootloader...\nadb wait-for-device\nfastboot oem lock\npause"
... format_bat = "@echo off\necho [*] Formatting Data...\nadb wait-for-device\nfastboot format userdata\npause"
... 
... # Simpan file .bat
... with open(f"{base_dir}/tools/unlock.bat", "w") as f: f.write(unlock_bat)
... with open(f"{base_dir}/tools/relock.bat", "w") as f: f.write(relock_bat)
... with open(f"{base_dir}/tools/format_data.bat", "w") as f: f.write(format_bat)
... 
... # Simpan file icon dummy
... with open(f"{base_dir}/assets/icon.png", "wb") as f: f.write(b"")
... 
... # Simpan file .js dan .html dari dokumen
... with open(f"{base_dir}/main.js", "w") as f:
...     f.write(canmore_docs["herjan_unlocker_gui"])
... with open(f"{base_dir}/preload.js", "w") as f:
...     f.write(canmore_docs["preload"])
... with open(f"{base_dir}/index.html", "w") as f:
...     f.write(canmore_docs["index"])
... 
... # Buat file README
... with open(f"{base_dir}/README.txt", "w") as f:
...     f.write("Herjan Cell MTK Unlocker - Jalankan dengan `npx electron .` atau compile ke EXE.\n")
... 
... # Buat file ZIP
... zip_path = "/mnt/data/HerjanCellUnlocker_v1.zip"
... with zipfile.ZipFile(zip_path, 'w') as zipf:
...     for foldername, subfolders, filenames in os.walk(base_dir):
...         for filename in filenames:
...             filepath = os.path.join(foldername, filename)
...             arcname = os.path.relpath(filepath, base_dir)
...             zipf.write(filepath, arcname)
... 
... zip_path
