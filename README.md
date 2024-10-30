# Tds_project1
### GitHub Users in Boston

This repository contains data about GitHub users in Boston with over 100 followers and their repositories.

### Files

1. `users.csv`: Contains information about 469 GitHub users in Boston with over 100 followers
2. `repositories.csv`: Contains information about 45005 public repositories from these users
3. `Data_Collection moudule`: Python script that uses request module to collect this data

### Data Collection

- Data collected using GitHub API
- Date of collection: 2024-10-23
- Only included users with 100+ followers
- Up to 500 most recently pushed repositories per user

- Data was scraped from the GitHub API by filtering users in Boston with over 100 followers and fetching their most recent repositories.
- A significant portion of repositories in Boston are written in JavaScript but surprisingly SQL is also seen in many repositories.
- Developers in Boston should focus on collaboration in JavaScript-based and Python-based projects to leverage the local expertise and community.
