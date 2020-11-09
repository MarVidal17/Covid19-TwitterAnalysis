import json
import string
from collections import Counter
from nltk.corpus import stopwords

from Task34.utils.PreprocessTweets import preprocess


def get_tweet_counters(file_name, all_terms=True, hashtags=False, simple_terms=False,
                       num_most_common=10, print_output=False, discarded_terms=[]):

    punctuation = list(string.punctuation)
    other_punctuation = ['…', '’', '¿']
    twitter_common_words = ['rt', 'via', 'RT']
    stop = stopwords.words('english') + punctuation + twitter_common_words + other_punctuation + discarded_terms

    with open(file_name, 'r') as f:

        # Create a dictionaries
        counters = {
            'Tokens': Counter() if all_terms else None,
            'Hashtags': Counter() if hashtags else None,
            'Terms without mentions and hashtags': Counter() if simple_terms else None
        }
        terms = {}
        num_of_tweets = 0

        for line in f:
            num_of_tweets += 1
            tweet = json.loads(line)
            tokens = preprocess(tweet['text'])

            # Create a list with all the terms
            if all_terms:
                terms['Tokens'] = [term for term in tokens if term not in stop]
            if hashtags:
                terms['Hashtags'] = [term for term in tokens if term.startswith('#') and term != '#']
            if simple_terms:
                terms['Terms without mentions and hashtags'] = \
                    [term for term in tokens if term not in stop and not term.startswith(('#', '@'))]

            for title, counter in counters.items():
                counter.update(terms[title])

        if print_output:
            print('\n{} total number of tweets'.format(num_of_tweets))
            for title, counter in counters.items():
                print('\n{} most common {}'.format(num_most_common, title))
                i = 0
                for word, index in counter.most_common(num_most_common):
                    i += 1
                    print('\t{}. {}: {}'.format(i, word, index))

        return counters
