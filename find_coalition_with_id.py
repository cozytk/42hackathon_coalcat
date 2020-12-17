import requests

access_token = "test"

def get_access_token():
    tokens = {
        'client_id': '81b49a0e9f9492908d09922c08fd6eaa9a7ee6e000eab7f3b622fbe157ad9a85',
        'client_secret': 'ebc94d8b60baa56eb11f2cac16a4cc32b583a1dd5f5b93cc57563d479fd8f68f',
        'grant_type' : 'client_credentials'
    }

    url = 'https://api.intra.42.fr/oauth/token'
    response = requests.post(url, params=tokens)
    global access_token
    access_token = response.json()['access_token']
    print("updated access_token: " + access_token)


def find_coalition_with_id(intra_name):
    global access_token
    headers = { 'Authorization': 'Bearer ' + access_token }
    response = requests.get('https://api.intra.42.fr/v2/users/' + intra_name + '/coalitions', headers=headers)
    if (response.status_code != 200):
        return 'invalid'

    coalition_name = response.json()[0]['slug']
    return coalition_name
