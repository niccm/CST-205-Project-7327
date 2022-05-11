import requests, json
from pprint import pprint

# payload = {
#     # 'region' : 'Marina, CA'
# }

# location = input("Where would you like to check the weather for? ")

location = 'marina'
url = f'https://weatherdbi.herokuapp.com/data/weather/{location}'
endpoint = url

try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    region = data['region']
    weatherNow = data['currentConditions']

    # pprint(data)
    print(list(data.values())[0])
    
    for key, value in weatherNow.items():
        if(key != 'iconURL'):
            if(key == 'temp'):
                print(key, "= ", 'c:', value['c'], 'f:', value['f'])
            elif(key == 'wind'):
                print(key, "= ", 'km:', value['km'], 'mile:', value['mile'])
            else:
                print(key, " : ", value)            

except:
    print('please try again')