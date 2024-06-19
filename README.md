# monitoring tailscale devices

This script monitors the status of devices connected via Tailscale by periodically running a PowerShell command to fetch the status, parsing the output, formatting it, and then sending the formatted information to a Telegram chat.

## Requirements
- Windows OS
- Python
- Tailscale
- Telegram bot

## Install
- install tailscale on your devices
- on your windows pc:
    - install python
    - creat new virtualenv 
    - install packages
    ```
    pip install -r requirements.txt
    ```
    - replace your telegram bot token and id channel
    - run monitoring tailscale devices scipt
    ```
    python monitorTailScale.py
    ```