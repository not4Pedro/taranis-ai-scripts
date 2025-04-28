#!/usr/bin/env python3

import json
import sys
import requests

def post_connector(address, connector_payload, auth_token=None):
    url = f"{address}/api/worker/connectors"
    headers = {'Content-Type': 'application/json'}
    if auth_token:
        headers['Authorization'] = f"Bearer {auth_token}"
    response = requests.post(url, json=connector_payload, headers=headers)
    return response.status_code, response.text

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <connector_file> <address> [auth_token]")
        sys.exit(1)

    connector_file = sys.argv[1]
    address = sys.argv[2]
    auth_token = sys.argv[3] if len(sys.argv) >= 4 else None

    if not address.startswith('http://') and not address.startswith('https://'):
        address = 'http://' + address

    with open(connector_file, 'r') as f:
        connector_payload = json.load(f)

    status_code, text = post_connector(address, connector_payload, auth_token)
    print(f"POST {address}/api/worker/connectors -> Status: {status_code}")
    if status_code >= 400:
        print(f"Error: {text}")

if __name__ == "__main__":
    main()