import sys
import json

def lines(fp):
    return str(len(fp.readlines()))

def isword(word):
    for character in word:
        if(not character.isalpha()):
            return False
    return True

def incrementdico(tweetstring, scores_dict):
    words = tweetstring.split(" ")
    nb_terms=0
    for word in words:
        if( word in scores_dict):
            scores_dict[word] += 1.0
            nb_terms += 1.0
        else:
#            if ((not word.startswith("@")) and (not word.startswith("#")) and (not word.startswith("RT")) and (not word.startswith(":")) and (not word.startswith("http")) ):
            if(word.strip() and isword(word.strip())):
            #it is a word
                scores_dict[word.strip()] = 1.0
                nb_terms += 1.0
    return nb_terms

def main():
    tweet_file = open(sys.argv[1])
    occurences = {}
    nb_terms = 0.0

    for line in tweet_file:
        tweet_data= json.loads(line)
        if("text" in tweet_data and tweet_data["lang"]=="en"):
            #it is a real tweet in english
            nb_terms += incrementdico( tweet_data ["text"], occurences)

    for key, value in occurences.items():
        print key, float(value/nb_terms)

#    hw()
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
