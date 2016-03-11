import sys
import json
import operator

def tweetlocation(tweet):
    states= { 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California',  'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi','MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',  'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands',  'VT': 'Vermont',  'WA': 'Washington', 'WI': 'Wisconsin',  'WV': 'West Virginia', 'WY': 'Wyoming'}

    location = tweet["location"]
    if(not location is None):
        for key,value in states.iteritems():
            if( key in location or value in location):
                return key

    return "None"

def tweetscore(tweetstring, scores_dict):
    words = tweetstring.split(" ")
    score=0.0
    for word in words:
        if( word in scores_dict):
            score += scores_dict[word]
    return score
    
#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #create dictionary for sentiments
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = float(score)  # Convert the score to an integer.

    tweets_per_state = {'AK': 0.0, 'AL': 0.0, 'AR': 0.0, 'AS': 0.0, 'AZ': 0.0, 'CA': 0.0, 'CO': 0.0, 'CT': 0.0, 'DC': 0.0, 'DE': 0.0, 'FL': 0.0, 'GA': 0.0, 'GU': 0.0, 'HI': 0.0, 'IA': 0.0, 'ID': 0.0, 'IL': 0.0, 'IN': 0.0, 'KS': 0.0, 'KY': 0.0, 'LA': 0.0, 'MA': 0.0, 'MD': 0.0, 'ME': 0.0, 'MI': 0.0, 'MN': 0.0, 'MO': 0.0, 'MP': 0.0, 'MS': 0.0, 'MT': 0.0, 'NA': 0.0, 'NC': 0.0, 'ND': 0.0, 'NE': 0.0, 'NH': 0.0, 'NJ': 0.0, 'NM': 0.0, 'NV': 0.0, 'NY': 0.0, 'OH': 0.0, 'OK': 0.0, 'OR': 0.0, 'PA': 0.0, 'PR': 0.0, 'RI': 0.0, 'SC': 0.0, 'SD': 0.0, 'TN': 0.0, 'TX': 0.0, 'UT': 0.0, 'VA': 0.0, 'VI': 0.0, 'VT': 0.0, 'WA': 0.0, 'WI': 0.0, 'WV': 0.0, 'WY': 0.0}
    score_per_state = {'AK': 0.0, 'AL': 0.0, 'AR': 0.0, 'AS': 0.0, 'AZ': 0.0, 'CA': 0.0, 'CO': 0.0, 'CT': 0.0, 'DC': 0.0, 'DE': 0.0, 'FL': 0.0, 'GA': 0.0, 'GU': 0.0, 'HI': 0.0, 'IA': 0.0, 'ID': 0.0, 'IL': 0.0, 'IN': 0.0, 'KS': 0.0, 'KY': 0.0, 'LA': 0.0, 'MA': 0.0, 'MD': 0.0, 'ME': 0.0, 'MI': 0.0, 'MN': 0.0, 'MO': 0.0, 'MP': 0.0, 'MS': 0.0, 'MT': 0.0, 'NA': 0.0, 'NC': 0.0, 'ND': 0.0, 'NE': 0.0, 'NH': 0.0, 'NJ': 0.0, 'NM': 0.0, 'NV': 0.0, 'NY': 0.0, 'OH': 0.0, 'OK': 0.0, 'OR': 0.0, 'PA': 0.0, 'PR': 0.0, 'RI': 0.0, 'SC': 0.0, 'SD': 0.0, 'TN': 0.0, 'TX': 0.0, 'UT': 0.0, 'VA': 0.0, 'VI': 0.0, 'VT': 0.0, 'WA': 0.0, 'WI': 0.0, 'WV': 0.0, 'WY': 0.0}

    for line in tweet_file:
        tweet_data= json.loads(line)
        if("text" in tweet_data):
            location = tweetlocation(tweet_data["user"])
            if(location != "None") :
         #       print location,
                score_per_state[location] += tweetscore( tweet_data["text"], scores)
                tweets_per_state[location] += 1

    #normalize results
    for location,score in score_per_state.iteritems():
        score_per_state[location] = score/max(1.0,tweets_per_state[location])

    # print the happiest
    print max(score_per_state.iteritems(), key=operator.itemgetter(1))[0]
    
if __name__ == '__main__':
    main()
