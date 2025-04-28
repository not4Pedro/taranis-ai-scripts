#!/usr/bin/env python
import json
import argparse
from collections import Counter

def main():
    parser = argparse.ArgumentParser(
        description="Count news items per source from a JSON file."
    )
    parser.add_argument("jsonfile", help="Path to the JSON file containing stories")
    parser.add_argument(
        "-o", "--output", default=None,
        help="Path to the output JSON file (default: prints to stdout)"
    )
    args = parser.parse_args()

    try:
        with open(args.jsonfile, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(json.dumps({"error": f"Error reading file: {e}"}))
        return

    source_counter = Counter()

    for story in data:
        news_items = story.get("news_items", [])
        for item in news_items:
            source = item.get("osint_source_id")
            if source:
                source_counter[source] += 1

    result = dict(source_counter)
    output_json = json.dumps(result, indent=2)

    if args.output:
        try:
            with open(args.output, "w") as out_file:
                out_file.write(output_json)
            print(f"Results written to {args.output}")
        except Exception as e:
            print(json.dumps({"error": f"Error writing output file: {e}"}))
    else:
        print(output_json)

if __name__ == "__main__":
    main()
