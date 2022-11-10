
# def get_links_from_url(url,visited):
#     page = requests.get(url)

#     # Get the response code of given URL
#     response_code = str(page.status_code)

#     soup = BeautifulSoup(page.text, 'html.parser')

#     urls = []
#     # Iterate over all links on the given URL with the response code next to it
#     for link in soup.find_all('a'):
#         print(link.get('href'))
#         if "http" in link.get('href'):
#             urls.append(link.get('href'))
#     unique_urls = list(set(urls))

#     non_visited_urls = []
#     for i in unique_urls:
#         if i not in visited:
#             non_visited_urls.append(i)

#     return non_visited_urls

# url = input("Enter your url: ")
# page_urls = [url]
# visited = []
# broken_url = []
# external_links = []
# page = 1
# while True:
#     page+=1
#     if len(page_urls) >0:
#         print(page_urls, "----page_urls---")
#         page_url = page_urls[0]
#         print(page_url, "--------------page_url")
#         if page_url not in visited:
#             visited.append(page_url)
#             page_urls.remove(page_url)
#             if url  not in page_url:
#                 external_links.append(page_url)

#             else:
#                 try:
#                     #Function retuens List of Urls
#                     pageUrls = get_links_from_url(page_url,visited)
#                     if page_url in pageUrls:
#                         pageUrls.remove(page_url)
#                     data = page_urls+pageUrls
#                     page_urls = list(set(data))
#                 except:
#                     broken_url.append(page_url)
#         else:
#             page_urls.remove(page_url)
#     else:
#         break
import requests
from bs4 import BeautifulSoup
page_urls = requests.get("https://stackoverflow.com/")
normal_txt = BeautifulSoup(page_urls.content, 'html.parser')
# print(normal_txt)
ch=normal_txt.meta.contents[0]
print(ch)