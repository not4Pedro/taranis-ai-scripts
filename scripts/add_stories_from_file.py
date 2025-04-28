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

def remove_keys(story, story_keys_to_remove, news_item_keys_to_remove, attribute_keys_to_remove):
    for key in story_keys_to_remove:
        story.pop(key, None)
    if 'news_items' in story:
        for news_item in story['news_items']:
            for key in news_item_keys_to_remove:
                news_item.pop(key, None)
    if 'attributes' in story:
        for attribute in story['attributes']:
            for key in attribute_keys_to_remove:
                attribute.pop(key, None)
    return story

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <stories_file> <address> [auth_token] [story_keys_to_remove] [news_item_keys_to_remove] [attribute_keys_to_remove]")
        sys.exit(1)

    stories_file = sys.argv[1]
    address = sys.argv[2]
    auth_token = sys.argv[3] if len(sys.argv) >= 4 else None
    story_keys_to_remove = sys.argv[4].split(',') if len(sys.argv) >= 5 else []
    news_item_keys_to_remove = sys.argv[5].split(',') if len(sys.argv) >= 6 else []
    attribute_keys_to_remove = sys.argv[6].split(',') if len(sys.argv) >= 7 else []

    if not address.startswith('http://') and not address.startswith('https://'):
        address = 'http://' + address

    stories = load_stories(stories_file)

    for idx, story in enumerate(stories, start=1):
        story = remove_keys(story, story_keys_to_remove, news_item_keys_to_remove, attribute_keys_to_remove)
        status_code, text = post_story(address, story, auth_token)
        print(f"[{idx}/{len(stories)}] POST {address}/api/worker/stories -> Status: {status_code}")
        if status_code >= 400:
            print(f"Error: {text}")

if __name__ == "__main__":
    main()