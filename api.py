import json
import hashlib
import requests
import pandas as pd



USER_ENDPOINT = 'https://randomuser.me/api/'


def random_user() -> dict:

    """
    Get Random User from an API

    Return_type:
        Dict
    """

    response = requests.get(USER_ENDPOINT)
    return response.json()


def get_users_data() -> list:

    """
    send 1000 requests to endpoint and create a dictionary from needed data
    
    Return_type:
        List[Dict]
    """

    list_of_data = list()
    for _ in range(1000):
        user = random_user()
        data = dict()
        for info in user['results']:
            data = {
                'username' : info.get('login').get('username'),
                'password': info.get('login').get('password'),
                'age': info.get('dob').get('age'),
                'city': info.get('location').get('city'),
                'country': info.get('location').get('country'),
                'gender': info.get('gender'),
                }
            hashed_password = hash_password(data.get('password'))
            data['password'] = hashed_password
        list_of_data.append(data)

    return list_of_data
        


def hash_password(password:str) -> str:

    """
    take a plain-text password and add salt to that
    hashing it and return hashed_password

    Return_type:
        str
    """

    salt = 'g5z'
    password = password + salt
    hashed = hashlib.md5(password.encode())
    return hashed.hexdigest()


def dump_data() -> None:

    """
    Get Data from get_users_data function
    open a file named user_info.json 
    dumps data to that file

    Return_type:
        None
    """

    data = get_users_data()
    with open('user_info.json', 'w') as file:
        json.dump(data, file)


def load_data() -> dict:

    """
    Load Data from user_info.json file that previously dumps with dump_data function above
    and return data as dictionary

    Return_type:
        dict
    """

    with open('user_info.json') as file:
        data = json.load(file)
    return data


def filtered_user() -> pd.DataFrame:

    """
    Create a pandas DataFrame with loaded_data function above
    and return filtered pandas DataFrame aswell.

    Return_type:
        pandas.DataFrame
    """

    df = pd.DataFrame(load_data())
    return df.loc[(df['age'] > 30) & (df['gender'] == 'male')]

# uncomment code below for dumping data in a json file
# dump_data()