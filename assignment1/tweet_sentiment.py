import sys
import json

def tweetscore(tweetstring, scores_dict):
    words = tweetstring.split(" ")
    score=0
    for word in words:
        if( word in scores_dict):
       # if ((not word.startswith("@")) and (not word.startswith("#")) and (not word.startswith("RT")) and (not word.startswith(":")) and (not word.startswith("http")) ):
            score += scores_dict[word]
    print score
    
#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #create dictionary for sentiments
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        tweet_data= json.loads(line)
        if("text" in tweet_data):
            if("lang" in tweet_data):
                if(tweet_data["lang"]=="en"):
                    tweetscore( tweet_data ["text"], scores)

            else:
                tweetscore( tweet_data ["text"], scores)


if __name__ == '__main__':
    main()
