from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

# Prompt user to enter the URL
def get_links_from_url(request):
    url = ''

    context = dict()
    if request.method == "POST":
        url = request.POST.get('url')

        if url:

            #  Get the response code of given URL
            # response_code = str(url.status_code)
            page_urls = requests.get(url)

            # #####For Anchoe
            soup = BeautifulSoup(page_urls.text, 'lxml')

            urls = []
            # # Iterate over all links on the given URL with the response code next to it
            for link in soup.find_all('a'):
                # print(link.get('href'))
                if "http"or "https" in link.get('href'):
                    urls.append(link.get('href'))
            unique_urls = list(set(urls))
            total_urls=len(unique_urls)
            # print(total_urls,"----------total")
            context["total_urls"]=total_urls



            # ####Page Content
            normal_txt = BeautifulSoup(page_urls.content, 'html.parser')
            anchor=normal_txt.find_all("a")
            no_follow=[]
            if "nofollow" in str(anchor):
                print("yes")
            else:
                print("no")


            visited = []
            non_visited_urls = []
            for i in unique_urls:
                if i not in visited:
                    non_visited_urls.append(i)
            return non_visited_urls

    return HttpResponse (visited)

def all_links(request):
    context = dict()
    url = request.POST.get('url')

    if url:
        visited = []
        page_urls = [url]
        broken_url = []
        external_links = []
        page = 1
        while True:
            page+=1
            if len(page_urls) >0:
                print(page_urls, "----page_urls---")
                page_url = page_urls[0]
                print(page_url, "--------------page_url")
                if page_url not in visited:
                    visited.append(page_url)
                    page_urls.remove(page_url)
                    if url  not in page_url:
                        external_links.append(page_url)
                    else:
                        try:
                            #Function retuens List of Urls
                            pageUrls = get_links_from_url(page_url,visited)
                            if page_url in pageUrls:
                                pageUrls.remove(page_url)
                            data = page_urls+pageUrls
                            page_urls = list(set(data))
                        except:
                            broken_url.append(page_url)
                else:
                    page_urls.remove(page_url)
            else:
                break
            print(len(broken_url),"------------------Broken Url")
            print(len(external_links),"------------------------External")


    return render(request,"Broken.html",{"context":context,"url":url})



