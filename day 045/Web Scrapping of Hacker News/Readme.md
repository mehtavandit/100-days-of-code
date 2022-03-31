## Objective
This project's goal is to scrape [Hacker News](https://news.ycombinator.com/) and find the article with the highest points.

## main.py
- The data from [Hacker News](https://news.ycombinator.com/) is imported using the requests module and parsed with the Beautiful soup library.
- Title of all the news articles, along with their link and points are fetched using the find_all function of beautiful soup.
- The name and URL of the news stories with the most points are displayed as output.
