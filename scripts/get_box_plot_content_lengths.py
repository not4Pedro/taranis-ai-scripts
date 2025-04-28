#!/usr/bin/env python

import json
import matplotlib.pyplot as plt
import sys
import os

def main(file_path, n_outliers):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    content_lengths = []
    for item in data:
        for news_item in item.get("news_items", []):
            content_length = len(news_item.get("content", ""))
            content_lengths.append(content_length)

    if not content_lengths:
        print("No content found in the provided file.")
        sys.exit(1)

    content_lengths.sort()
    if n_outliers > 0:
        if 2 * n_outliers >= len(content_lengths):
            print("Not enough data points after removing outliers.")
            sys.exit(1)
        trimmed_lengths = content_lengths[n_outliers: -n_outliers]
    else:
        trimmed_lengths = content_lengths

    item_count = len(trimmed_lengths)

    # Create subplots: 1 row, 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Boxplot on the first subplot
    axes[0].boxplot(trimmed_lengths, vert=True, patch_artist=True)
    axes[0].set_title(f'Boxplot of Content Lengths\n({item_count} items (trimmed), trimmed {n_outliers} min/max)')
    axes[0].set_ylabel('Content Length (characters)')
    axes[0].set_xticks([1])
    axes[0].set_xticklabels(['News Items content'])
    axes[0].grid(True)

    # Histogram on the second subplot
    axes[1].hist(trimmed_lengths, bins=20, edgecolor='black')
    axes[1].set_title(f'Histogram of Content Lengths\n({item_count} items (trimmed), trimmed {n_outliers} min/max)')
    axes[1].set_xlabel('Content Length (characters)')
    axes[1].set_ylabel('Frequency')
    axes[1].grid(True)

    # Adjust layout
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Usage: {sys.argv[0]} <path_to_json_file> [n_outliers]")
        sys.exit(1)

    json_file_path = sys.argv[1]
    n_outliers = int(sys.argv[2]) if len(sys.argv) == 3 else 0  # Default to 0

    main(json_file_path, n_outliers)
