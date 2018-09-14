import urllib.request,json
search_term = "ocean"
data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=" + search_term + "&api_key=qstJPgVMjzbl0Mu1yGibicFiubKUFbBQ&limit=1").read())
print(json.dumps(data, sort_keys=True, indent=4))
gif_url = data['data'][0]['images']['fixed_height']['url']
urllib.request.urlretrieve(gif_url, "gifs/" + search_term + ".mp4")