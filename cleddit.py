#!/usr/bin/env python3.1
from optparse import OptionParser
import lib.frontpage

usage = '%prog [-l LIMIT ] [-s SUBREDDIT ]'
parser = OptionParser(usage=usage)

parser.add_option('-s', '--subreddit', dest = 'subreddit', help = 'Subreddit, e.g. programming')
parser.add_option('-l', '--limit', dest = 'limit', help = 'The number of posts you want to be displayed')

(options, args) = parser.parse_args()

lib.frontpage.render(
    subreddit = options.subreddit if options.subreddit else None, 
    limit = options.limit if options.limit else None,
    )
