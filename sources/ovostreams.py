"""
ovostreams.com

method:
first iframe
search for m3u8
"""

NAME = "ovostreams.com"
KEY = "ovostreamscom"
BASE = "www.ovostreams.com"

if __name__ == "__main__":
    import sys
    import os
    import json
    # ugly hack, but oh well
    sys.path.append("%s/.kodi/addons/plugin.video.tide" % os.getenv("HOME"))

try:
    import generic_m3u8_searcher
    from router import PLUGIN, path_for_source
    from helpers import http_get, log
    from common import add_headers, add_items, parse_url
except Exception as e:
    print(e)

import urllib
import re
from bs4 import BeautifulSoup 

def can_handle(url):
    p_url = parse_url(url)
    return p_url.netloc == BASE

@PLUGIN.route("%s/<url>" % path_for_source(KEY))
def root(url):
    ref_url = urllib.unquote(url).decode('utf8')
    urls = get_urls(ref_url)
    add_items(urls, ref_url, PLUGIN)

def get_urls(url):
    p_url = parse_url(url)
    html = http_get(url)
    soup = BeautifulSoup(html.text, 'html5lib')
    iframe = soup.find("iframe")
    iframe_url = "%s://%s/%s" % (p_url.scheme, p_url.netloc, iframe.get("src"))
    return generic_m3u8_searcher.get_urls(iframe_url)

if __name__ == "__main__":
    def test(url):
        vid_urls = get_urls(url)
        print(vid_urls)

    def test_can_handle(url):
        print(can_handle(url))

    test("http://www.ovostreams.com/tottenham-vs-southampton.php")
    test_can_handle("http://www.ovostreams.com/tottenham-vs-southampton.php")