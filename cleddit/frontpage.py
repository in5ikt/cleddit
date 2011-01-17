import urllib.request, urllib.parse, json, pprint
from bcolors import bcolors

def get_frontpage_json():
    jsonDecoder = json.JSONDecoder()
    
    request = urllib.request.Request('http://www.reddit.com/.json')
    
    f = urllib.request.urlopen(request)
    
    return f.read().decode('utf-8')

if __name__ == '__main__':
    page = json.JSONDecoder().decode( get_frontpage_json() )
    for x in page['data']['children']:
        if type( x ) is dict:
            if x['data']['over_18']:
                x['data']['title'] = bcolors.ERROR + x['data']['title']
            if x['data']['is_self']:
                print('> {title}\n - {selftext}\n| {url}\n| {author}\n)'.format(title=x['data']['title'],
                                                                                author=x['data']['author'],
                                                                                url=x['data']['url'],
                                                                                selftext=x['data']['selftext'],
                                                                                ))

            else:
                print('> {title}\n| {url}\n| {author}\n'.format(title=x['data']['title'], 
                                                                author=x['data']['author'],
                                                                url=x['data']['url'],
                                                                ))

