from nltk.corpus import stopwords

from Task34.utils.PreprocessTweets import strip_accents
from Task34.utils.get_counter_plot import get_counter_plot
from Task34.utils.get_tweet_counters import get_tweet_counters
from Task34.utils.get_tweet_location import get_tweet_location

file_name = '../Task34/c19.json'

""" Tokanize tweets and keep track of the frequencies """

discarded_terms = stopwords.words('spanish') + stopwords.words('french') + stopwords.words('portuguese')

# Get rid of stop words accents:
stop_without_accents = []
for stop_word in discarded_terms:
    stop_without_accents.append(strip_accents(stop_word))
discarded_terms = stop_without_accents

counters = get_tweet_counters(file_name, all_terms=True, hashtags=True, simple_terms=True,
                              num_most_common=20, print_output=True, discarded_terms=discarded_terms)


""" Show and save plots """

get_counter_plot(counters['Terms without mentions and hashtags'], 'SimpleTermsPlot.png')
get_counter_plot(counters['Hashtags'], 'HashtagsPlot.png')


""" Get tweets location an plot them """

location_counter = get_tweet_location(file_name)
get_counter_plot(location_counter, 'LocationsPlot.png')
