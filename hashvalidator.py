import hashlib
import os.path
import urllib.request


class FileHashGenerator:
    """Generates an SHA256 hash from a supplied file"""

    def __init__(self) -> object:
        self.sha256 = hashlib.sha256()

    def generate_hash(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'rb') as file_contents:
                buffer = file_contents.read()
                self.sha256.update(buffer)
        return self.sha256.hexdigest()


class OnlineHashRetriever:
    """Retrieves a HASH from a website URL"""

    def __init__(self):
        self.file_hash = ''

    def generate_hash_from_url(self, hash_url):
        with urllib.request.urlopen(hash_url) as request:
            content = request.read().decode('utf-8')
            self.file_hash = content.split(' ')[0]
            return self.file_hash


class HashValidator:
    def __init__(self, hash_generator: FileHashGenerator, hash_retriever: OnlineHashRetriever):
        """
        Calculates whether a file was manipulated
        :param hash_generator: A class that retrieves a hash from a file
        :param hash_retriever: A class that retrieves a hash from a URL
        """
        self.__file_hash_generator = hash_generator
        self.__online_hash_retriever = hash_retriever

    def validate_hash(self, file, hash_url):
        file_hash = self.__file_hash_generator.generate_hash(file)
        correct_hash = self.__online_hash_retriever.generate_hash_from_url(hash_url)
        return "SHA256 match" if file_hash == correct_hash else "This file has been manipulated"
