import imagehash

from PIL import Image



hash = imagehash.average_hash(Image.open('/Users/billyzhaoyh/Desktop/cat1.jpeg'))


otherhash = imagehash.average_hash(Image.open('/Users/billyzhaoyh/Desktop/cat2.jpg'))

hash2 = imagehash.average_hash(Image.open('/Users/billyzhaoyh/Desktop/monalisa1.jpg'))
hash3 = imagehash.average_hash(Image.open('/Users/billyzhaoyh/Desktop/monalisa2.jpg'))

print(hash2 == hash3)
