
import time
import pickle
import random
import requests

token = "EAACEdEose0cBAHfkkgIzET7ptSlf0wZBSzZCixjyRV1lVqSBZATbj27SzxOUGigNCwB6QEzMWMdZCTsc9ZAXDCKgDZAT4JLju027X3GDmO2WZCkC1eluZBEycWzlvrOuPOxz6IEG4WCets2oz64T9zIAaozlrCK5qN9BKpCYZBmyzZCFBCZCuS98BZCqpISCdw7TChEZD"


def req_fb(req):
    r = requests.get("https://graph.facebook.com/v2.9/"+ req, {'access_token':token})
    
    return r
    
req = "67919847338/posts?fields=comments,likes.limit(10)"    
obj = req_fb(req).json()        

data = []

#obj = obj['/posts']
i=0
while True:
    
    try:
        time.sleep(random.randint(2,5))
        data.extend(obj['data'])
        r = request.get(obj['paging']['next'])
        obj = r.json()
        i+=1
        
        if i>4:
            break
    
    except:
        print "done"
        break

pickle.dump(data,open('stream_data.pkl','wb'))
load_data = pickle.load(file=open("stream_data.pkl"))