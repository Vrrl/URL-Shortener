import random
import string


class Link():
    """Link Object"""

    url: str = None
    key: str = None

    def __init__(self, url: str, key: str = None):
        if '.' not in url:
            raise Exception("invalid url")
        
        self.url = url
        self.key = key

    def generate_key(self) -> None:
        if not self.key:
            self.key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))