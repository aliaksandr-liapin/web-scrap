import requests
import lxml

url = 'https://en.wikipedia.org/wiki/List_of_most_visited_websites'
url_txt = 'https://www.samsclub.com/robots.txt'
url_xml = 'https://www.samsclub.com/sitemap.xml'
url_json = 'https://swapi.dev/api/people/1'

"""
    ! prepare POST request data
    # params = {'custname':'Mr. ABC',
    #           'custtel':'',
    #           'custemail':'abc@somedomain.com',
    #           'size':'small',
    #           'topping':['cheese','mushroom'],
    #           'delivery':'13:00',
    #           'comments':'None'}

    #  headers={ 'Accept':'text/html,application/xhtml+xml,
    #            'Content-Type':'application/x-www-form-urlencoded',
    #            'Referer':pageUrl
    #           }
    # response = requests.post(postUrl,data=params,headers=headers).json()
"""

"""
    ! prepare GET request data
    link="http://localhost:8080/~cache"

    # queries= {'id':'123456','display':'yes'}
    # addedheaders={'user-agent':''}
    # response = requests.get(link, params=queries, headers=addedheaders)

    resuls -> 'http://localhst:8080/~cache?id=123456+display=yes'
"""

resp = requests.get(url_json)
print(resp.status_code)
print(resp.encoding)
print(resp.headers['content-type'])
data = resp.json()

# for veh in data['vehicles']:
#     print(veh)

# write data into file as binary "wb"
# file = open("sitemap.xml", "wb")
# file.write(resp.content)
