import urllib.request
import json
import argparse

def getResponse(username: str) -> list:
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            rawOutput = json.loads(data)
          
    except Exception as e:
        print(f"Following error as occdurred: {e}")

    return rawOutput

def generateOutput(filteredContent: dict):
  for repo, events in filteredContent.items():
    for event in events:
      match event:
        case "PushEvent":
          print(f"Pushed {events[event]} commits to {repo}")
        case "CreateEvent":
          print(f"Created something for {repo}")
        case "PullRequestEvent":
          print(f"opened, closed, merged, reopened, assigned, unassigned, labeled, or unlabeled {events[event]} times for {repo}")



def parseTypesAndOccurrences(ApiResponse:list) -> dict:
  filteredContent = {}
  for event in ApiResponse:
    if event["repo"]["name"] not in filteredContent:
      filteredContent[event["repo"]["name"]] = {}
    if event["type"] not in filteredContent[event["repo"]["name"]]:
      filteredContent[event["repo"]["name"]][event["type"]] = 1
    else:
      filteredContent[event["repo"]["name"]].update({event["type"]: filteredContent[event["repo"]["name"]][event["type"]]+1})

  return filteredContent


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog="github-activity",
                        description="This will fetch recent activity of a GitHub user and display it in the terminal.",
                        usage="github-activity <username>")
    parser.add_argument('username')
    args = parser.parse_args()
    username = args.username
    data = getResponse(username)

    content = parseTypesAndOccurrences(data)
    generateOutput(content)