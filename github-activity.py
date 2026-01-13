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

def generateOutput(filteredContent: dict) -> str:
  for item in filteredContent:
    print(filteredContent[item])


  return ""

def parseTypesAndOccurrences(ApiResponse:list) -> dict:
  filteredContent = {}
  for event in ApiResponse:
    if event["type"] not in filteredContent:
      filteredContent[event["type"]] = 1
    else:
      filteredContent.update({event["type"]: filteredContent[event["type"]]+1})
  
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