from django.db import models

STATES_LIST = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
PARTIES = [('Republican','Republican'),('Democrat','Democrat'),('Independent','Independent')]
GENDERS = [('M','Male'),('F','Female')]
EDUCATION_CHOICES = [('N','None'),('HS','High school'),('C','College')]
STATES = {"AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PW": "Palau",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"}



class Candidate(models.Model):
    name = models.CharField(max_length=200)
    party = models.CharField(max_length=50,choices=PARTIES)
    votes = models.IntegerField(default=0)
        
class State(models.Model):
    name = models.CharField(max_length=200)
    votes_rep = models.IntegerField(default=0)
    votes_dem = models.IntegerField(default=0)
    votes_ind = models.IntegerField(default=0)
    electoral_votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Voter(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    password =models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,choices=GENDERS)
    education = models.CharField(max_length=20,choices=EDUCATION_CHOICES)
    party = models.CharField(max_length=200,default='Democrat')
    voted = models.BooleanField(default=False)
    
AUTHORS = [('Politico','Politico'),('New York Times','New York Times'),('Washington Post','Washington Post')]

class Poll(models.Model):
    author = models.CharField(max_length=200,choices=AUTHORS)
    key_state = models.CharField(max_length=200)
    percent_ind = models.IntegerField()
    percent_dem = models.IntegerField()
    percent_rep = models.IntegerField()






