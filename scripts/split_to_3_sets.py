#!/usr/bin/env python3

import json
import sys
import os
from collections import defaultdict, Counter


def load_sources(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    # If it's a list, extract sources from news_items inside stories
    if isinstance(data, list):
        source_counter = Counter()
        for story in data:
            news_items = story.get("news_items", [])
            for news_item in news_items:
                source_id = news_item.get("osint_source_id")
                if source_id:
                    source_counter[source_id] += 1
        return dict(source_counter)
    elif isinstance(data, dict):
        return data
    else:
        raise ValueError("Unsupported JSON structure")


def save_group(group, path):
    with open(path, "w") as f:
        json.dump(group, f, indent=2)


def split_sources(sources):
    if not sources:
        raise ValueError("No sources to split. Check your input file.")

    # Sort sources by item count descending
    sorted_sources = sorted(sources.items(), key=lambda x: x[1], reverse=True)

    # Pick the most heavy source to be shared across all groups
    shared_source_id, shared_source_count = sorted_sources[0]

    # Remaining sources
    remaining_sources = sorted_sources[1:]

    groups = [{shared_source_id: shared_source_count} for _ in range(3)]
    group_totals = [shared_source_count] * 3

    # Distribute the rest to balance item counts across groups
    for src_id, count in remaining_sources:
        min_index = group_totals.index(min(group_totals))
        groups[min_index][src_id] = count
        group_totals[min_index] += count

    return groups


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <path_to_source_file> <output_directory>")
        sys.exit(1)

    source_file = sys.argv[1]
    output_dir = sys.argv[2]

    sources = load_sources(source_file)

    groups = split_sources(sources)

    os.makedirs(output_dir, exist_ok=True)
    for idx, group in enumerate(groups, start=1):
        save_group(group, os.path.join(output_dir, f"group{idx}.json"))

    print(
        f"Groups created and saved into {output_dir}/group1.json, group2.json, group3.json"
    )


if __name__ == "__main__":
    main()
