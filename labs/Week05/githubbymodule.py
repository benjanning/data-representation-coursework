from github import Github
from config import config as cfg
from config import apikey
# use your own key
g = Github(apikey)
repo = g.get_repo("https://api.github.com/benjanning/aprivateone/")
print(repo.clone_url)
      
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)
