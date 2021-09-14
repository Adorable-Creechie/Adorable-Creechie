"""
ovostreams.com

method:
generic/first_iframe_get_urls
"""

NAME = "ovostreams.com"
KEY = "ovostreamscom"
BASE = "ovostreams.com"

try:
    from generic_m3u8_searcher import first_iframe_get_urls as get_urls
    from router import PLUGIN, path_for_source
    from .common import gen_can_handle, gen_root
except Exception as e:
    print(e)

can_handle = gen_can_handle(BASE)

@PLUGIN.route("%s/<url>" % path_for_source(KEY))
def root(url):
    gen_root(url, get_urls)

if __name__ == "__main__":
    def test(url):
        vid_urls = get_urls(url)
        print(vid_urls)

    def test_can_handle(url):
        print(can_handle(url))

    test("http://www.ovostreams.com/liverpool-vs-burnley.php")
    test_can_handle("http://www.ovostreams.com/liverpool-vs-burnley.php")
