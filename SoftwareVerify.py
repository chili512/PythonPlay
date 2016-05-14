from hashvalidator import FileHashGenerator, OnlineHashRetriever, HashValidator

file_hash_generator = FileHashGenerator()
online_hash_retriever = OnlineHashRetriever()
hashValidator = HashValidator(file_hash_generator, online_hash_retriever)
filename = '/Users/jonathan/Downloads/datagrip-2016.1.dmg'
url = 'https://download.jetbrains.com/datagrip/datagrip-2016.1.dmg.sha256'
message = hashValidator.validate_hash(filename, url)

print(message)
