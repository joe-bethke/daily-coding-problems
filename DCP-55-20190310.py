"""
This problem was asked by Microsoft.
Implement a URL shortener with the following methods:
shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""
import requests
from random import choice


class URLShortener(dict):

    shortened_url_characters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890"
    max_urls = 10000000  # Some max, should be based on length of shortened_url_characters

    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix

    def __call__(self, url):
        return self.shorten(url)

    def shorten(self, url):
        if len(self) >= self.max_urls:
            raise ValueError("This URLShortener is full! no more URLs can be shortened based on the allowed characters.")
        if url in self.values():
            return next(short for short, previous_url in self.items() if previous_url == url)
        shortened_url = ""
        while not shortened_url or shortened_url in self:
            shortened_url = "".join(choice(self.shortened_url_characters) for _ in range(6))
        self[shortened_url] = url
        return shortened_url

    def restore(self, short):
        return self.get(short)

    def deactivate(self, short):
        return self.pop(short)

    def full_shortened_url(self, short):
        return "{prefix}/{short}".format(prefix=self.prefix, short=short)

    def redirect(self, short):
        try:
            return requests.get(self.full_shortened_url(short))
        except requests.exceptions.ConnectionError:
            pass


url_shortener = URLShortener("https://goo.gl.com")
short = url_shortener("https://www.facebook.com/")
print(short)
short = url_shortener("https://www.facebook.com/")
print(short)
print(url_shortener.full_shortened_url(short))
full = url_shortener.restore(short)
print(full)
facebook = url_shortener.redirect(full)
print(facebook)
url_shortener.deactivate(short)
print(short in url_shortener)
