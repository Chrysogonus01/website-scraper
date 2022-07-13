import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news") # for next page add... ?p= number of page
soup = BeautifulSoup(res.text,"html.parser")
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'],reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            
            points = int(vote[0].getText().replace('points', ' '))
            #print(points)
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes':points})
        
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))