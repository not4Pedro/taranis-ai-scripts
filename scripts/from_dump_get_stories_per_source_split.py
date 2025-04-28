#!/usr/bin/env python3

import json
import sys
import os

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def filter_stories(all_stories, group_sources):
    group_source_ids = set(group_sources.keys())
    filtered_stories = []

    for story in all_stories:
        news_items = story.get('news_items', [])
        for news_item in news_items:
            if news_item.get('osint_source_id') in group_source_ids:
                filtered_stories.append(story)
                break  # include story once, even if multiple matching news_items

    return filtered_stories

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <all_stories_file> <group_sources_file> <output_file>")
        sys.exit(1)

    all_stories_file = sys.argv[1]
    group_sources_file = sys.argv[2]
    output_file = sys.argv[3]

    all_stories = load_json(all_stories_file)
    group_sources = load_json(group_sources_file)

    filtered_stories = filter_stories(all_stories, group_sources)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    save_json(filtered_stories, output_file)

    print(f"Filtered {len(filtered_stories)} stories into {output_file}")

if __name__ == "__main__":
    main()
