import urllib.request, urllib.parse, json, pprint, colorama

from colorama import Fore, Back, Style

colorama.init()

def get_frontpage_json(subreddit = None):
    jsonDecoder = json.JSONDecoder()

    subreddit = 'r/' + subreddit if subreddit else ''

    url = 'http://www.reddit.com/' + subreddit + '.json'
    request = urllib.request.Request(url)
    
    f = urllib.request.urlopen(request)
    
    return f.read().decode('utf-8')

def render(subreddit = None):
    page = json.JSONDecoder().decode( get_frontpage_json(subreddit) )
    for x in page['data']['children']:
        if type( x ) is dict:
            if x['data']['over_18']:
                x['data']['title'] = Fore.RED + x['data']['title'] + Fore.RESET
            if x['data']['is_self']:
                print('> {title}\n - {selftext}\n| {url}\n| {author}\n'.format(title=Style.BRIGHT + x['data']['title'] + Style.RESET_ALL,
                                                                                author=x['data']['author'],
                                                                                url=x['data']['url'],
                                                                                selftext=x['data']['selftext'],
                                                                                ))

            else:
                print('> {title}\n| {url}\n| {author}\n'.format(title=Style.BRIGHT + x['data']['title'] + Style.RESET_ALL,
                                                                author=x['data']['author'],
                                                                url=x['data']['url'],
                                                                ))

if __name__ == '__main__':
    render()
