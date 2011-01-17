import urllib.request, urllib.parse, json, pprint

jsonDecoder = json.JSONDecoder()

request = urllib.request.Request('http://www.reddit.com/.json')

f = urllib.request.urlopen(request)

data = jsonDecoder.decode( f.read().decode('utf-8') )

if __name__ == '__main__':
    for x in data['data']['children']:
        print('{title}\n{url}\n{author}\n'.format(title=x['data']['title'], 
                                                  author=x['data']['author'],
                                                  url=x['data']['url'],
                                                  ) )

#pprint.pprint(data)
