import sys
import json

def incrementdico(tweetstring, scores_dict, new_scores_dict):
    words = tweetstring.split(" ")
    score=0
    for word in words:
        if( word in scores_dict):
            score += scores_dict[word]
    
    for word in words:
        if ((not word.startswith("@")) and (not word.startswith("#")) and (not word.startswith("RT")) and (not word.startswith(":")) and (not word.startswith("http")) ):
            #it is a word
            if(not word in scores_dict):
                if( word in new_scores_dict):
                    new_scores_dict[word] += int(score)
                else:
                    new_scores_dict[word] = int(score)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    new_scores={}
    for line in tweet_file:
        tweet_data= json.loads(line)
        if("text" in tweet_data):
            if("lang" in tweet_data):
                if(tweet_data["lang"]=="en"):
                    incrementdico( tweet_data ["text"], scores, new_scores)
            else:
                incrementdico( tweet_data ["text"], scores, new_scores)

    for key, value in new_scores.items():
        print key, value

#    hw()
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
