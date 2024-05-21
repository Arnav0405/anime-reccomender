import requests
# Here we define our query as a multi-line string
query = '''
query($id: Int){
  Media(id: $id){
    id
    title {
      romaji
      english
    }
    popularity
    relations {
      edges {
        id
      }
    }
    genres
    averageScore
    staff(page: 1){
      edges {
        node {
          id
          name {
            full
          }
          languageV2
        }
        role 
      }
    }
    characters(page: 1){
      edges {
        node {
          id 
          name {
          full
          }
        } 
      }
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': 158927
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.json())