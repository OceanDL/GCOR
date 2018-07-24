import urllib.request,json
data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=ocean&api_key=qstJPgVMjzbl0Mu1yGibicFiubKUFbBQ&limit=5").read())
print(json.dumps(data, sort_keys=True, indent=4))