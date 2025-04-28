#!/usr/bin/env python3

import json
import sys
import requests

def load_stories(path):
    with open(path, 'r') as f:
        return json.load(f)

def post_story(address, story):
    url = f"{address}/api/worker/stories"
    response = requests.post(url, json=story)
    return response.status_code, response.text

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <stories_file> <address>")
        sys.exit(1)

    stories_file = sys.argv[1]
    address = sys.argv[2]

    if not address.startswith('http://') and not address.startswith('https://'):
        address = 'http://' + address

    stories = load_stories(stories_file)

    for idx, story in enumerate(stories, start=1):
        status_code, text = post_story(address, story)
        print(f"[{idx}/{len(stories)}] POST {address}/worker/stories -> Status: {status_code}")
        if status_code >= 400:
            print(f"Error: {text}")


if __name__ == "__main__":
    main()