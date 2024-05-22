import requests
import pandas as pd
import time

def to_csv(data):
    json_data = data
    df = pd.DataFrame(json_data['data']['Page']['media']) # Convert the json data to a pandas dataframe
    df.to_csv('anime_data.csv', index=False, mode='a') # Save the dataframe to a csv file
    return 1

# Here we define our query as a multi-line string
query = '''
{
  Page(page: 29, perPage: 50) {
    pageInfo {
      total
      lastPage
      hasNextPage
    }
    media(type: ANIME, popularity_greater: 10000, sort: POPULARITY_DESC) {
      id
      title {
        romaji
        english
      }
      startDate {
        year
      }
      popularity
      favourites
      tags {
        name
      }
      genres
      averageScore
      description
      studios(isMain: true) {
        nodes{
          name
        }
      } 
    }
  }
}

'''

# Define our query variables and values that will be used in the query request
variables = {
}

url = 'https://graphql.anilist.co'
'''response = requests.post(url, json={'query': query, 'variables': variables})  
data = response.json()
print(data)'''
# Make the HTTP Api request
for i in range(0, 100):
    print(f'Page {i} done')
    query = query.replace(f'Page(page: {i}, perPage: 50)', f'Page(page: {i+1}, perPage: 50)')
    response = requests.post(url, json={'query': query, 'variables': variables})
    time.sleep(2)
    data = response.json()
    to_csv(data)