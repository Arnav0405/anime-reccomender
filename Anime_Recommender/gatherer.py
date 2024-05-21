import requests

# Here we define our query as a multi-line string
query = '''
query ($id: Int, $page: Int, $perPage: Int, $search: String) { # Define which variables will be used in the query (id)
  Page (page: $page, perPage: $perPage) { # Utilising the Page query type
  pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
  media (id: $id,  type: MANGA, search: $search) { 
    id
    title {
      romaji
      english
       }
    startDate {
      year
      month
    }
    status
    chapters
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'search': 'Domestic',
    'page': 1,
    'perPage': 5
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.json())