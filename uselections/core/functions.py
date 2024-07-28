from core.models import Candidate
from core.models import State,Poll,AUTHORS
import random
import requests
from bs4 import BeautifulSoup


STATES = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]


def update_electoral_votes():
    Trump = Candidate.objects.get(name='Donald Trump')
    Harris = Candidate.objects.get(name='Kamala Harris')
    Kennedy = Candidate.objects.get(name='Robert Kennedy')

    states = State.objects.all()
    Trump.votes = 0
    Kennedy.votes =0
    Harris.votes =0
    for state in states:
        MAX = max(state.votes_dem,state.votes_ind,state.votes_rep)
        if MAX > 0:
            if MAX == state.votes_dem:
                Harris.votes+=state.electoral_votes
            elif MAX == state.votes_rep:
                Trump.votes+=state.electoral_votes
            elif MAX == state.votes_ind:
                Kennedy.votes+=state.electoral_votes
        print(state.electoral_votes,state.name,state.votes_rep)
    Harris.save()
    Trump.save()
    Kennedy.save()



def generate_poll():
    
    
    author = random.choice(AUTHORS)
    key_state = random.choice(STATES)
    percent_dem = random.randint(0,70)
    percent_rep = random.randint(0,100-percent_dem)
    percent_ind = (100-percent_dem-percent_rep)
    
    while Poll.objects.count() > 2:
        item = Poll.objects.all()[0]
        item.delete()
    p = Poll(author=author[0],key_state=key_state,percent_dem=percent_dem,percent_ind=percent_ind,percent_rep=percent_rep)
    p.save()


def scrape_state_info():
    pass








