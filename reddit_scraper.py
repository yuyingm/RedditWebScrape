import requests
from bs4 import BeautifulSoup

def scrape_subreddit(subreddit, keyword):
    url = f"https://www.reddit.com/r/{subreddit}/search/?q={keyword}"
    headers = {"User-Agent": "Your User Agent"}  # Add a user agent to mimic a web browser request

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information
    posts = soup.find_all('div', class_='scrollerItem')

    for post in posts:
        title = post.find('h3').text
        link = post.find('a')['href']
        print(f"Title: {title}\nLink: {link}\n")

if __name__ == "__main__":
    subreddit_name = "your_subreddit_name"
    search_keyword = "cost of living"
    scrape_subreddit(subreddit_name, search_keyword)
