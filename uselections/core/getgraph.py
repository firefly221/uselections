import matplotlib.pyplot as plt
import numpy as np
import pandas as pa
from statedata import STATE_DATA
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


for state_abbr in STATES.keys():
    
   

    YEAR = 1992
    arr_rep = []
    arr_dem = []
    for election in STATE_DATA:
        for st in election['votes']:
            if 'popular' in election['votes'][st] and st == state_abbr:
                pop_votes = election['votes'][st]['popular']
                rep = pop_votes['republican']
                dem = pop_votes['democrat']
                arr_rep.append(rep)
                arr_dem.append(dem)
                #print(YEAR,rep,dem)
                YEAR+=4

    if arr_dem == []:
        continue
    plt.plot([year for year in range(1992,2021,4)],arr_rep,label='Republikanie',color='red')
    plt.plot([year for year in range(1992,2021,4)],arr_dem,label='Demokraci',color='blue')
    plt.title('Liczba głosów w poprzednich latach')
    plt.ticklabel_format(style='plain')
    plt.xlabel('Rok')
    plt.ylabel('Liczba osób')
    plt.subplots_adjust(left=0.3)
    plt.legend()
    plt.savefig('graphs/'+STATES[state_abbr]+'.png')
    plt.close()








