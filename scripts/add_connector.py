#!/usr/bin/env python3

import argparse
import requests
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Send MISP connector payload to server"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Base URL of the server (e.g., https://example.com)",
    )
    parser.add_argument(
        "--auth_header", required=True, help="Authorization header (e.g., Bearer token)"
    )
    parser.add_argument("--api_key", required=True, help="MISP API Key")
    parser.add_argument("--con_url", required=True, help="Connector URL")
    parser.add_argument("--organisation_id", required=True, help="Organisation ID")
    parser.add_argument("--sharing_group_id", required=True, help="Sharing Group ID")

    args = parser.parse_args()

    payload = {
        "name": "misp",
        "description": "",
        "icon": "",
        "type": "misp_connector",
        "parameters": {
            "URL": args.con_url,
            "API_KEY": args.api_key,
            "ORGANISATION_ID": args.organisation_id,
            "SHARING_GROUP_ID": args.sharing_group_id,
        },
    }

    headers = {"Content-Type": "application/json", "Authorization": args.auth_header}

    endpoint = f"{args.url.rstrip('/')}/api/worker/connectors"

    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Success: {response.status_code}")
        print(response.json())
    except requests.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
