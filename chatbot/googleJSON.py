from lib.google_search_results import GoogleSearchResults
f = open('recognizedtext.txt','r')
queryText = f.read()
f.close()
query = GoogleSearchResults({'q':queryText})
json_results = query.get_json()
json_obj1 = json_results['organic_results']
json_obj2 = json_obj1[1]
snippet = json_obj2['snippet']
print(snippet)
f  =open('snippet.txt','w')
f.write(snippet)
f.close()
