from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)
repo = g.get_repo("benjanning/aprivateone")
print(repo.clone_url)
      
fileInfo = repo.get_contents("test.txt", ref="main")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)

repo.update_file(fileInfo.path, "update file", newContents, fileInfo.sha, branch="main")

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)
