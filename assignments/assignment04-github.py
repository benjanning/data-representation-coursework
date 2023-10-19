from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)
repo = g.get_repo("benjanning/assignment04privaterepo")
print(repo.clone_url)
      
fileInfo = repo.get_contents("names.txt", ref="main")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

# Replace "Andrew" with "Ben" in the content
newContents = contentOfFile.replace("Andrew", "Ben")
print (newContents)

# Update the file with the new content
result = repo.update_file(fileInfo.path, "replaced Andrew with Ben", newContents, fileInfo.sha, branch="main")

print(result)

# Reference: https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python
