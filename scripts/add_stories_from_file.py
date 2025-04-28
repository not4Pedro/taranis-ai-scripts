#!/usr/bin/env python3

import json
import sys
import requests

def load_stories(path):
    with open(path, 'r') as f:
        return json.load(f)

def post_story(address, story, auth_token=None):
    url = f"{address}/api/worker/stories"
    headers = {}
    if auth_token:
        headers['Authorization'] = f"Bearer {auth_token}"
    response = requests.post(url, json=story, headers=headers)
    return response.status_code, response.text

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(f"Usage: {sys.argv[0]} <stories_file> <address> [auth_token]")
        sys.exit(1)

    stories_file = sys.argv[1]
    address = sys.argv[2]
    auth_token = sys.argv[3] if len(sys.argv) == 4 else None

    if not address.startswith('http://') and not address.startswith('https://'):
        address = 'http://' + address

    stories = load_stories(stories_file)

    for idx, story in enumerate(stories, start=1):
        status_code, text = post_story(address, story, auth_token)
        print(f"[{idx}/{len(stories)}] POST {address}/api/worker/stories -> Status: {status_code}")
        if status_code >= 400:
            print(f"Error: {text}")

if __name__ == "__main__":
    main()