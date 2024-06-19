# monitoring tailscale devices

This script monitors the status of devices connected via Tailscale by periodically running a PowerShell command to fetch the status, parsing the output, formatting it, and then sending the formatted information to a Telegram chat.

## How it works
1. Get the status of your connections to other Tailscale devices.
2. get response infomation, parse and index result, print to my windows powershell screen, include: numerical order, tailscale ip, computer name, os, status.
3. send response infomation via telegram bot, using code format telegram chat.
4. Repeat the program after 60 minute.

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