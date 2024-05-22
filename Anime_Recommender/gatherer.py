import requests
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
      Description
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
print(response.json())