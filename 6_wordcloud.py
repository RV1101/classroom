
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'Aesop’s Fables.txt')).read()
###########################################################################
# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "anne.png")))
###########################################################################
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)
# generate word cloud
wc.generate(text)
###########################################################################
# store to file
wc.to_file(path.join(d, "anne_color.png"))
###########################################################################
wc_1 = WordCloud(background_color="gray", max_words=20000, mask=alice_mask,
               stopwords=stopwords)
# generate word cloud
wc_1.generate(text)
###########################################################################
# show 1
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
# show 2
plt.figure()
plt.imshow(wc_1, interpolation='bilinear')
plt.axis("off")
# show 3
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
#open 123
plt.show()
