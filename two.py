import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from wordcloud import WordCloud

data = {
    'Book_Title': [
        'Python Data Science Handbook', 'Introduction to Machine Learning',
        'Deep Learning with Python', 'Hands-On Machine Learning',
        'Data Science from Scratch', 'Artificial Intelligence Basics',
        'Python Programming Essentials', 'Machine Learning Yearning'
    ],
    'Author': [
        'Jake VanderPlas', 'Andreas Muller', 'Francois Chollet', 'Aurelien Geron',
        'Joel Grus', 'Andrew Ng', 'Jake VanderPlas', 'Andrew Ng'
    ],
    'Publication_Year': [2016, 2016, 2017, 2019, 2015, 2020, 2018, 2018],
    'Average_Rating': [4.7, 4.5, 4.8, 4.9, 4.3, 4.6, 4.4, 4.8],
    'Number_of_Ratings': [3200, 1500, 4100, 5200, 2100, 3100, 1800, 4900]
}

df = pd.DataFrame(data)

period1_authors = set(df[df['Publication_Year'] <= 2016]['Author'])
period2_authors = set(df[df['Publication_Year'] > 2016]['Author'])

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
venn2([period1_authors, period2_authors], set_labels=('Published <= 2016', 'Published > 2016'))
plt.title("Venn Diagram of Authors Across Time Periods")

plt.subplot(1, 2, 2)
all_titles = " ".join(df['Book_Title'])
wc = WordCloud(width=600, height=400, background_color='white').generate(all_titles)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Book Titles")

plt.tight_layout()
plt.show()
