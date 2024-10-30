#user.csv

import requests
import csv

token = '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'
headers = {'Authorization': f'token {token}'}

with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 'public_repos', 'followers', 'following', 'created_at']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    page = 1
    while True:
        
        url = f'https://api.github.com/search/users?q=location:Boston+followers:>100&per_page=30&page={page}'
        response = requests.get(url, headers=headers)
        users_data = response.json()

        if 'items' not in users_data or not users_data['items']:
            break
        
        for user in users_data['items']:
            user_url = f"https://api.github.com/users/{user['login']}"
            user_info = requests.get(user_url, headers=headers).json()

            
            company = user_info.get('company', '')
            if company:
                company = company.strip().lstrip('@').upper()

            writer.writerow({
                'login': user_info.get('login'),
                'name': user_info.get('name'),
                'company': company,
                'location': user_info.get('location'),
                'email': user_info.get('email'),
                'hireable': user_info.get('hireable'),
                'bio': user_info.get('bio'),
                'public_repos': user_info.get('public_repos'),
                'followers': user_info.get('followers'),
                'following': user_info.get('following'),
                'created_at': user_info.get('created_at')
            })
        page += 1
print("Data saved to users.csv")

#repositories.csv

import requests
import csv
import time

# GitHub API token (replace with your own token)
token = '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'
headers = {'Authorization': f'token {token}'}

# Function to fetch repositories for a user
def fetch_repositories(user_login):
    repos_url = f"https://api.github.com/users/{user_login}/repos"
    repos_data = []
    page = 1

    while True:
        response = requests.get(repos_url, headers=headers, params={'per_page': 100, 'page': page})
        repos = response.json()

        if not repos or 'message' in repos:
            break

        repos_data.extend(repos)

        # If we have fewer than 100 results, stop paginating
        if len(repos) < 100:
            break
        page += 1

        time.sleep(1)  # Delay to avoid rate limiting

    return repos_data

# Read users from users.csv
with open('users.csv', 'r', encoding='utf-8') as userfile:
    users = csv.DictReader(userfile)

    # Store users in a list for processing
    user_list = [user for user in users]

    total_users = len(user_list)  # Count total users

    # Open a CSV file to write the repository data
    with open('repositories.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Start the timer
        start_time = time.time()

        # Loop through users
        for index, user in enumerate(user_list, start=1):
            # Debugging: Print the current user dictionary
            print(f"Processing user: {user}")

            # Check if 'login' key exists
            if 'login' not in user:
                print(f"Warning: 'login' key not found in user data: {user}")
                continue  # Skip to the next user if 'login' is missing

            user_login = user['login']
            repositories = fetch_repositories(user_login)

            # Loop through repositories and write them to CSV
            for repo in repositories:
                # Safely handle the license field
                license_info = repo.get('license')
                license_name = license_info['key'] if license_info else None

                writer.writerow({
                    'login': user_login,
                    'full_name': repo.get('full_name'),
                    'created_at': repo.get('created_at'),
                    'stargazers_count': repo.get('stargazers_count'),
                    'watchers_count': repo.get('watchers_count'),
                    'language': repo.get('language'),
                    'has_projects': repo.get('has_projects'),
                    'has_wiki': repo.get('has_wiki'),
                    'license_name': license_name
                })

            # Calculate elapsed time and estimate remaining time
            elapsed_time = time.time() - start_time
            estimated_total_time = (elapsed_time / index) * total_users
            remaining_time = estimated_total_time - elapsed_time

            print(f"Processed {index}/{total_users} users. Estimated remaining time: {remaining_time:.2f} seconds.")

print("Repository data saved to repositories.csv")


