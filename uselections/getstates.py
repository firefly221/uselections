import json,pprint

file = open('statedata.py','w')


file.write('STATE_DATA = [')
for year in range(1960,2024,4):
    year = str(year)
    with open('uselections/json/' + year + '.json') as json_file:
        json_data = json.load(json_file)
       
        
        file.write(',' + str(pprint.pformat(json_data)))
        
file.write(']')








