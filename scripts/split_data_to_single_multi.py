#!/usr/bin/env python3

import json
import sys
import os

def split_stories(file_path):
    # Load data
    with open(file_path, 'r') as f:
        stories = json.load(f)

    # Separate stories
    single_item_stories = [story for story in stories if len(story.get("news_items", [])) == 1]
    multi_item_stories = [story for story in stories if len(story.get("news_items", [])) > 1]

    # Ensure output directory exists
    os.makedirs("../data", exist_ok=True)

    # Write to files
    with open("../data/single_item_stories.json", 'w') as f:
        json.dump(single_item_stories, f, indent=2)

    with open("../data/multi_item_stories.json", 'w') as f:
        json.dump(multi_item_stories, f, indent=2)

    print(f"Wrote {len(single_item_stories)} single-item stories to ../data/single_item_stories.json")
    print(f"Wrote {len(multi_item_stories)} multi-item stories to ../data/multi_item_stories.json")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    split_stories(source_file)
