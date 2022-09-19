
from operator import le
from unittest.util import three_way_cmp
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import metadata_parser
import re


def Density_Check(request):
    
    context = dict()
    data={}
    data1={}
    data2={}
    data3={}
    if request.method == "POST":
    
        url = request.POST.get('url')
        data = Density(url)
        # print(data,"------------------------alll Dictinory ")
        
    context={  "data":data,
                "data1":data1,
                "data2":data2,
                "data3":data3}
        
    return render(request, 'Density.html', context )

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
    
    Total_word1=len(one)
    for key,val in data.items():
        # print(key,"and",val)
        # print(val)
        print("Density=",(int(val)/int(Total_word1))*100,key)
      
        
    #Two Word Frequency and Density calculate
    data1={}
    Two_Word=list(set(two))
    print(two,"--------------------------Two")
    for Kword1 in Two_Word:
        results1 = soup.body.find_all(string=re.compile('.*{0}.*'.format(Kword1)), recursive=True)
        data1[Kword1] = len(results1)
        
    
    Total_word2=len(two)
    for key1,val1 in data1.items():
        # print(key,"and",val)
        # print(val)
        print("Density Two WOrd=",(int(val1)/int(Total_word2))*100,key1)
    
    
    # #Three Word Frequency and Density calculate
    if "100+ Latest Updates" in three:
        three.remove("100+ Latest Updates")
    if "Learn C++ Tutorial" in three:
        three.remove("Learn C++ Tutorial")
    print(three,"-----------Three List")
    Convert_set=set(three)
    Three_word=list(set(Convert_set))
    print(Three_word,"===============Three Word")
    
    data2={}
    for Kword2 in Three_word:
        results2 = soup.body.find_all(string=re.compile('.*{0}.*'.format(Kword2)), recursive=True)
        data2[Kword2] = len(results2)
        
        # print(results2,"------------------ Three Word")
    Three_Word1=len(Three_word)
    for key2,val2 in data2.items():
        # print(key,"and",val)
        # print(val)
        print("Density Three WOrd=",(int(val2)/int(Three_Word1))*100,key2)
        
    
    #Four Word Frequency and Density calculate
    Four_word=list(set(four))
    print(four,"--------------------------Four")
    data3={}
    for Kword3 in Four_word:
        results3 = soup.body.find_all(string=re.compile('.*{0}.*'.format(Kword3)), recursive=True)
        data3[Kword3] = len(results3)
    
    Four_word1=len(Four_word)
    for key3,val3 in data3.items():
        # print(key,"and",val)
        # print(val)
        print("Density Four WOrd=",(int(val3)/int(Four_word1))*100,key3)
    
    
    return data 








