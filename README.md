# monitoring tailscale devices

This script monitors the status of devices connected via Tailscale by periodically running a PowerShell command to fetch the status, parsing the output, formatting it, and then sending the formatted information to a Telegram chat.

## Requirements
- Windows OS
- Python
- Tailscale