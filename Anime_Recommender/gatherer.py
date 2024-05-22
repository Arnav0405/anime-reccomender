import requests
import pandas as pd
# Here we define our query as a multi-line string
query = '''
{
  Page(page: 1, perPage: 200) {
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

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
json_data = response.json()
df = pd.DataFrame(json_data['data']['Page']['media']) # Convert the json data to a pandas dataframe
df.to_csv('anime_data.csv', index=False) # Save the dataframe to a csv file
print(df.info()) 