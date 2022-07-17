import csv
import json

def jsonloader(jsonfile):
    try: 
        f = open(jsonfile, 'r')
        data = json.load(f)
        tweetobj = json.loads(data)
        f.close()
        return tweetobj
    except IOError:
        return None

def covidreader(label, events):
    rumourlist = []
    nonrumourlist = []
    with open(label, newline='') as labelfile:
        with open(events, newline='') as eventsfile:
            labelreader = csv.reader(labelfile)
            eventsreader = csv.reader(eventsfile)
            next(labelreader)
            for (label,events) in zip(labelreader,eventsreader):
                #loading files
                #templist = []
                source = events.pop()
                sourcetweet = jsonloader("covid_data/" + source + ".json")
                # if there is no sourcetweet, continue
                if sourcetweet != None and sourcetweet != []: 
                    rumourlist.append(sourcetweet) if label[1] =="1" else nonrumourlist.append(sourcetweet)
                    #templist.append(sourcetweet) 
                else: continue
                
                #loading the remaining sorcetweet
                #for event in events:
                #    tweet = jsonloader("covid_data/"    + event +".json")
                #    if tweet: templist.append(tweet)
                #rumourlist.append(templist) if label[1] =="1" else nonrumourlist.append(templist)
    
    return rumourlist, nonrumourlist

import os
print(len(os.listdir("covid_data")))