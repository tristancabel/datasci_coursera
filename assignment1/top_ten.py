import sys
import json
import operator

def lines(fp):
    return str(len(fp.readlines()))

def incrementdico(tweetstring, scores_dict):
    tags = tweetstring["hashtags"]
    nb_terms=0
    for w in tags:
        word = w["text"]
        if( word in scores_dict):
            scores_dict[word] += 1.0
        else:
            scores_dict[word] = 1.0

def main():
    tweet_file = open(sys.argv[1])
    occurences = {}
    nb_terms = 0.0

    for line in tweet_file:
        tweet_data= json.loads(line)
        if("text" in tweet_data):
            if("lang" in tweet_data):
                if(tweet_data["lang"]=="en"):
                    #it is a real tweet in english
                    incrementdico( tweet_data ["entities"], occurences)
            else:
                incrementdico( tweet_data ["entities"], occurences)

    #sort the tags
    i=0
    for tag in sorted(occurences.items(), key=operator.itemgetter(1), reverse=True):
        i=i+1
        if(i>10):
            break
        print tag[0] , tag[1]


if __name__ == '__main__':
    main()
