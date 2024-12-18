# Tds_project1
### GitHub Users in Boston

This repository contains data about GitHub users in Boston with over 100 followers and their repositories.

### Files

1. `users.csv`: Contains information about 469 GitHub users in Boston with over 100 followers.
2. `repositories.csv`: Contains information about 45005 public repositories from these users.
3. `Data_Collection.py`: Python script that uses request module to collect this data.
4. `Analysis.py`: Python script used to analyze the data.
   

### Data Collection

- Date of collection: 2024-10-23
- Data was scraped from the GitHub API by filtering users in Boston with over 100 followers and fetching their most recent repositories.
- Up to 500 most recently pushed repositories per user



### Interferences
- Developers in Boston should focus on collaboration in JavaScript-based and Python-based projects to leverage the local expertise and community.
- I used a python code to scrape the data using my GitHub token from api.github.com and to clean the data.
- It is interesting that SQL is one of the least popular programming languagues among the users and yet it has the highest average number of stars per repository.
- The regression slope of followers on bio word count is negative, which means that the shorter the bio, the higher the followers, the developer would gain.
- A significant portion of repositories in Boston are written in JavaScript but surprisingly SQL is also seen in many repositories.
- Developers in Boston should focus on collaboration in JavaScript-based and Python-based projects to leverage the local expertise and community.


