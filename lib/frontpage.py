import urllib.request, urllib.parse, json, pprint, colorama
from colorama import Fore, Back, Style

colorama.init()

def get_frontpage_json(subreddit = None):
    '''
    Retrieves JSON fron the reddit servers and returns it

    The subreddit parameter states which, if any, subreddit it should fetch.
    Default is *all*
    '''

    jsonDecoder = json.JSONDecoder()

    subreddit = 'r/' + subreddit if subreddit else ''

    url = 'http://www.reddit.com/' + subreddit + '.json'
    request = urllib.request.Request(url)
    
    f = urllib.request.urlopen(request)
    
    return f.read().decode('utf-8')

def render(subreddit = None, limit = 0):
    '''
    Renders the list containing title, (selftext)?, url and author
    '''

    page = json.JSONDecoder().decode( get_frontpage_json(subreddit) )
    rendered_posts = 0
    for x in page['data']['children']:
        if type(x) is dict:
            if x['data']['over_18']:
                x['data']['title'] = Fore.RED + x['data']['title'] + Fore.RESET
            
            print('> {title}\n{selftext}| {url}\n| {author}\n'.format(
                        title=Style.BRIGHT + x['data']['title'].strip() + Style.RESET_ALL,
                        author=Style.DIM + x['data']['author'] + Style.RESET_ALL,
                        selftext=' - ' + x['data']['selftext'].rstrip() + '\n' if x['data']['is_self'] else '',
                        url=x['data']['url'],
                        ))
            rendered_posts += 1
            if limit and rendered_posts >= int(limit):
                break

if __name__ == '__main__':
    render()
