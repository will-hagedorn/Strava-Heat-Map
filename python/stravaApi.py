import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#def main():
#    request()

def request():
    auth_url = "https://www.strava.com/oauth/token"
    activites_url = "https://www.strava.com/api/v3/athlete/activities"

    payload = {
        'client_id': "126690",
        'client_secret': '2f81b0e1740748f05efd95919e806c51e33ada3b',
        'refresh_token': '422123aa4680f809f951f9ab7387964dac6472cf',
        'grant_type': "refresh_token",
        'f': 'json'
    }

    print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']

    print("Access Token = {}\n".format(access_token))
    header = {'Authorization': 'Bearer ' + access_token}

    request_page_num = 1
    all_activities = []

    while True:
        param = {'per_page': 200, 'page': request_page_num}
        
        my_dataset = requests.get(activites_url, headers=header, params=param).json()

        if len(my_dataset) == 0:
            print("breaking out of while loop because the response is zero, which means there must be no more activities")
            break

        if all_activities:
            print("all_activities is populated")
            all_activities.extend(my_dataset)

        else:
            print("all_activities is NOT populated")
            all_activities = my_dataset

        request_page_num += 1

    #return all_activities
    #print(all_activities[0])
    #for count, activity in enumerate(all_activities):
    #    print(activity["name"])
    #    print(count)

    return all_activities

#main()