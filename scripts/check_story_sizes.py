#!/usr/bin/env python3

import json
import sys
from collections import Counter

def analyze_news_items(file_path):
    # Load data
    with open(file_path, 'r') as f:
        stories = json.load(f)

    # Count news_items per story
    news_items_counts = [len(story.get("news_items", [])) for story in stories]

    # Count how many stories have the same number of news_items
    counts_distribution = Counter(news_items_counts)

    # Print results
    print("News Items per Story Distribution:")
    for num_items, count in sorted(counts_distribution.items()):
        print(f"Stories with {num_items} news_items: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    analyze_news_items(source_file)
