import urllib.request
import json
import argparse

def getResponse(url: str) -> list:
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            json_data = json.loads(data)
            print(type(json_data))
    except Exception as e:
        print(f"Following error as occdurred: {e}")

    return json_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog="github-activity",
                        description="This will fetch recent activity of a GitHub user and display it in the terminal.",
                        usage="github-activity <username>")
    parser.add_argument('username')

    args = parser.parse_args()
    print(args)
"""
    url = "https://api.github.com/users/kamranahmedse/events"
    response = getResponse(url)

    for element in response:
        print(element)
        for item in element:
            print(item)
        break
"""





"""

{
  "id": "7411874171",
  "type": "PushEvent",
  "actor": {
    "id": 4921183,
    "login": "kamranahmedse",
    "display_login": "kamranahmedse",
    "gravatar_id": "",
    "url": "https://api.github.com/users/kamranahmedse",
    "avatar_url": "https://avatars.githubusercontent.com/u/4921183?"
  },
  "repo": {
    "id": 1133135515,
    "name": "kamranahmedse/timelang",
    "url": "https://api.github.com/repos/kamranahmedse/timelang"
  },
  "payload": {
    "repository_id": 1133135515,
    "push_id": 29706963806,
    "ref": "refs/heads/main",
    "head": "d1bb34cb2bd8a2bba7c84e658b650fc675b41a3a",
    "before": "bb6757b7ff6e66f7fd268d290942fb04a8c81497"
  },
  "public": true,
  "created_at": "2026-01-13T02:11:22Z"
}
"""