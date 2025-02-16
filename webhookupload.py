#!/usr/bin/env python3
import os
import json
import requests

def send_haiku_to_discord(haiku, webhook_url):
   
    # Prepare haiku content
    data = {
        "content": haiku
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    # Send POST request
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    
    # Check 
    if response.status_code == 204:
        print("Haiku sent successfully!")
    else:
        print(f"Failed to send haiku. HTTP {response.status_code}: {response.text}")

def get_latest_haiku(file_path="haiku.txt"):
  
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                
                haiku_blocks = [block.strip() for block in content.split('\n\n') if block.strip()]
                if haiku_blocks:
                    return haiku_blocks[-1]
    return ("An old silent pond...\n"
            "A frog jumps into the pond,\n"
            "Splash! Silence again.")

if __name__ == "__main__":
    WEBHOOK_URL = "https://discord.com/api/webhooks"
    
    haiku_text = get_latest_haiku()
    
    send_haiku_to_discord(haiku_text, WEBHOOK_URL)
