import requests
import time

def get_starred_by_user(username):
    starred_repos = []
    page = 1
    while True:
        response = requests.get(
            f'https://api.github.com/users/{username}/starred?page={page}&per_page=1000', 
            headers={'Accept': 'application/vnd.github.v3+json'}
        )
        data = response.json()
        if response.status_code != 200:
            raise Exception(f'Error{page}: {data}')
        if not data:
            break
        starred_repos += data
        page += 1
        time.sleep(1)
    return [(repo['html_url'], repo['stargazers_count']) for repo in starred_repos]

username = input("type user id: ")
starred_repos = get_starred_by_user(username)
for repo in starred_repos:
    print(f'{repo[0]}')
