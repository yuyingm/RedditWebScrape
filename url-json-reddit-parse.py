import requests

# subreddit = 'python'
# limit = 100
# timeframe = 'month' #hour, day, week, month, year, all
# listing = 'top' # controversial, best, hot, new, random, rising, top


subreddit = input(
          "Enter the subreddit that you'd like to scrape (just the name, no slashes, quotation marks, etc.):  "
      )

limit = input(
          "Enter the max no. of posts that you'd like to scrape as a whole number:  "
      )

timeframe = input(
          "Enter the timeframe for data that you'd like to scrape (i.e. hour, day, week, month, year, all):  "
      )

listing = input(
          "Enter how you'd like the data organised (e.g. controversial, best, hot, new, random, rising, top):  "
      )

def get_reddit(subreddit,listing,limit,timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()

r = get_reddit(subreddit,listing,limit,timeframe)

print(get_reddit(subreddit,listing,limit,timeframe))
