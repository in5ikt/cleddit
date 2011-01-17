#!/usr/bin/env python3.1
from optparse import OptionParser
import cleddit.frontpage
parser = OptionParser()

parser.add_option('-s', '--subreddit', dest='subreddit', help='subreddit')

(options, args) = parser.parse_args()

cleddit.frontpage.render(options.subreddit if options.subreddit else None)
