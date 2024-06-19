import subprocess
import re
import requests
import time

def run_tailscale_status():
    # Run the PowerShell command and capture the output
    result = subprocess.run(['powershell', '-Command', 'tailscale status'], capture_output=True, text=True)
    return result.stdout

def parse_tailscale_output(output):
    lines = output.strip().split('\n')
    devices = []
    for i, line in enumerate(lines, 1):
        # Use regular expressions to parse each line
        match = re.match(r'(\S+)\s+(\S+)\s+\S+@\s+(\S+)\s+(.+)', line)
        if match:
            tailscale_ip, computer_name, os, status = match.groups()
            # Clean status by removing unnecessary details after semicolon if present
            status = status.split(';')[0].strip()
            devices.append({
                'index': i,
                'tailscale_ip': tailscale_ip,
                'computer_name': computer_name,
                'os': os,
                'status': status
            })
    return devices

def format_devices(devices):
    formatted_devices = []
    for device in devices:
        formatted_devices.append(f"{device['index']}. {device['tailscale_ip']} {device['computer_name']} {device['os']} {device['status']}")
    return "\n".join(formatted_devices)

def format_devices_code(devices):
    formatted_devices = []
    for device in devices:
        formatted_devices.append(f"{device['index']}. `{device['tailscale_ip']}` `{device['computer_name']}` `{device['os']}` `{device['status']}`")
    return "\n".join(formatted_devices)

def send_to_telegram(message, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "MarkdownV2"
    }
    response = requests.post(url, data=data)
    return response.json()

def main():
    # Replace with your actual bot token and chat ID
    bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
    chat_id = 'YOUR_TELEGRAM_CHAT_ID'
    
    while True:
        output = run_tailscale_status()
        devices = parse_tailscale_output(output)
        formatted_devices = format_devices(devices)
        formatted_devices_code = format_devices_code(devices)
        
        # Print to PowerShell screen
        print(formatted_devices)
        
        # Send the parsed information via Telegram bot
        response = send_to_telegram(f"```\n{formatted_devices_code}\n```", bot_token, chat_id)
        print(response)
        
        # Wait for 60 minutes before repeating the process
        time.sleep(3600)

if __name__ == "__main__":
    main()
