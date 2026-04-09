import json
import os

def find_keys(data, keys_to_find, results):
    if isinstance(data, dict):
        for key, value in data.items():
            if key in keys_to_find:
                results[key] = value
            find_keys(value, keys_to_find, results)
    elif isinstance(data, list):
        for item in data:
            find_keys(item, keys_to_find, results)

def credentials_search():
    file_name = 'logs.json'
    
    if not os.path.exists(file_name):
        return

    try:
        with open(file_name, 'r') as f:
            content = f.read()
            if not content.strip(): # Check if empty
                return
            data = json.loads(content)
    except (json.JSONDecodeError, ValueError):
        return

    found_credentials = {}
    target_keys = ["password", "secret"]
    find_keys(data, target_keys, found_credentials)

    if found_credentials:
        with open('credentials.json', 'w') as f:
            json.dump(found_credentials, f, indent=2)
