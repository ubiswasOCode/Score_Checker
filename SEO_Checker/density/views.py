
from operator import le
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import metadata_parser
import re


def Density_Check(request):
    data = {}
    if request.method == "POST":
    
        url = request.POST.get('url')
        data = Density(url)
        print(data)
        
        
    return render(request, 'Density.html',{'data': data })

# def Density_cal():
#     total_words=len(one)
    
#     msg=[]
    
#     msg.append('\n' + str(round(exist_keys,3)) + '%' + ' keyword density')
#     msg.append('\nThe keyword appears ' + str(density) + ' times in the page.')

        

def Density(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    
    one=[]
    two = []
    three = []
    four = []

    for para in soup.find_all("p"):
        text = para.get_text()
        # print(text)

        # convert into List
        li = list(text.split())
        if len(li) == 1:
            one.append(" ".join(li))
        elif len(li) == 2:
            two.append(" ".join(li))
        elif len(li) == 3:
            three.append(" ".join(li))
        elif len(li) == 4:
            four.append(" ".join(li))

    for para in soup.find_all("a"):
        text = para.get_text()
        li = list(text.split())
        if len(li) == 1:
            one.append(" ".join(li))
        elif len(li) == 2:
            two.append(" ".join(li))
        elif len(li) == 3:
            three.append(" ".join(li))
        elif len(li) == 4:
            four.append(" ".join(li))
        else:
            pass

    #
    for Head1 in soup.find_all("h1"):
        text1 = Head1.get_text()
        li2 = list(text1.split())
        if len(li2) == 1:
            one.append(" ".join(li2))
        elif len(li2) == 2:
            two.append(" ".join(li2))
        elif len(li2) == 3:
            three.append(" ".join(li2))
        elif len(li2) == 4:
            four.append(" ".join(li2))
        else:
            pass

    for Head2 in soup.find_all("h2"):
        text2 = Head2.get_text()
        li3 = list(text2.split())
        if len(li3) == 1:
            one.append(" ".join(li3))
        elif len(li3) == 2:
            two.append(" ".join(li3))
        elif len(li3) == 3:
            three.append(" ".join(li3))
        elif len(li3) == 4:
            four.append(" ".join(li3))
        else:
            pass
    #
    for Head3 in soup.find_all("h3"):
        text3 = Head3.get_text()
        li4 = list(text3.split())
        if len(li4) == 1:
            one.append(" ".join(li4))
        elif len(li4) == 2:
            two.append(" ".join(li4))
        elif len(li4) == 3:
            three.append(" ".join(li4))
        elif len(li4) == 4:
            four.append(" ".join(li4))
        else:
            pass

    for Head4 in soup.find_all("h4"):
        text4 = Head4.get_text()
        li5 = list(text4.split())
        if len(li5) == 1:
            one.append(" ".join(li5))
        elif len(li5) == 2:
            two.append(" ".join(li5))
        elif len(li5) == 3:
            three.append(" ".join(li5))
        elif len(li5) == 4:
            four.append(" ".join(li5))
        else:
            pass
        

    #After Removing
    One_Word = list(set(one))
    print(one,"---------------------one")
    if "C++" in One_Word:
        One_Word.remove("C++")
    
    data = {}
    for kwrd in One_Word:
        results = soup.body.find_all(string=re.compile('.*{0}.*'.format(kwrd)), recursive=True)
        data[kwrd] = len(results)
        # print(results,"-----------------------results")
    
    
        
    # Two_Word=list(set(two))
    # for Kword1 in Two_Word:
    #     results = soup.body.find_all(string=re.compile('.*{0}.*'.format(Kword1)), recursive=True)
    #     data[Kword1] = f"{len(results)} times"
    
    
    Total_word=len(one)
    for key,val in data.items():
        # print(key,"and",val)
        # print(val)
       
        print("Density=",(int(val)/int(Total_word))*100,key)
        
    
    return data








