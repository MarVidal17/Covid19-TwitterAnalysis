import json
from collections import Counter


def get_tweet_location(file_name):
    with open(file_name, 'r') as f:

        location_counter = Counter()

        for line in f:
            tweet = json.loads(line)
            location = [tweet['place']['country_code']] if tweet['place'] else ['Location not set']
            location_counter.update(location)

        num_countries = len(location_counter.items())
        i = 0
        print('\n Tweets locations:')
        for word, index in location_counter.most_common(num_countries):
            i += 1
            print('\t{}. {}: {}'.format(i, word, index))

        location_counter.pop('Location not set')

        return location_counter
