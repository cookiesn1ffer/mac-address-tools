# 🧠 MAC Address Tools

![Python](https://img.shields.io/badge/python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Linux-orange)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![Author](https://img.shields.io/badge/author-CookieSn1ffer-blueviolet)
![Repo Size](https://img.shields.io/github/repo-size/CookieSn1ffer/mac-address-tools?color=yellow)
![Last Commit](https://img.shields.io/github/last-commit/CookieSn1ffer/mac-address-tools?logo=github)

A clean and minimal collection of Python scripts to **view, change, or randomize** your system's MAC address — perfect for **ethical hacking labs**, **CTFs**, and **network testing**.

---

## ⚙️ Requirements

- Linux OS  
- Python 3.x  
- `macchanger` (for randomizer)

### 🧩 Install `macchanger`

**Debian / Ubuntu / Kali / Mint**
```bash
sudo apt update
sudo apt install macchanger
```

**Arch / Manjaro / EndeavourOS**
```bash
sudo pacman -Syu macchanger
```

**Scripts**
1. mac_address_changer_cli.py
   Change your MAC address using command-line arguments:
   ```bash
   sudo python3 mac_address_changer_cli.py -i eth0 -m 00:11:22:33:44:55
   ```

2. mac_address_changer_basic.py
   Simpler, interactive version:
    ```bash
    sudo python3 mac_address_changer_basic.py
    ```
3. mac_address_randomizer.py
    Randomizes your MAC using the macchanger tool:
    ```bash
    sudo python3 mac_address_randomizer.py
    ```
---

⚠️ Disclaimer

These tools are made for educational and ethical purposes only.
Do not use them on networks or systems you do not own or have permission to test.

---

👤 Author

CookieSn1ffer
💻 Student • Cybersecurity Enthusiast • Linux Explorer
📧 Reach me on GitHub

---

📄 License

Released under the MIT License.
