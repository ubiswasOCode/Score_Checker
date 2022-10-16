
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import metadata_parser
import re


def Density_Check(request):

    url=" "
    context = dict()

    if request.method == "POST":
        url = request.POST.get('url')
        if (url):
       
            context = Density(url)
        else:
            context =WordDensity(wrdsrch)
            
        # context = WordDensity(wrdsrch)

        context['url']=url
       

    return render(request, 'Density.html', context)




def Density(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')


    one=[]
    two = []
    three = []
    four = []


    #Append into One List
    all_list=one+two+three+four
    print(all_list,"---------------------Listssssssss")



    #Get Meta Title
    page=metadata_parser.MetadataParser(url)
    meta_title=page.get_metadata('title')
    print(meta_title,"--------------------meta Title")
    meta_list=list(meta_title)

      #Check it is Title or not
    for x in all_list:
        if x in meta_list:
            print(x,"---------------Yes")
        else:
            print(x,"--------------------------no")

      ### Keywords
    keyword=page.get_metadata("keywords")
    print(keyword,"-------------------------keywordss")


    #Get Description
    meta_desc=page.get_metadata("description")
    print(meta_desc,"---------------Description")
    # desc_list=list(meta_desc)


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
        Total_word1=len(one)
        density=round((int(len(results))/int(Total_word1))*100,2)
        data[kwrd] = {"freq": len(results), "density": density}
        # data[kwrd] = len(results)
        # print(results,"-----------------------results")



    #Two Word Frequency and Density calculate
    data1={}
    Two_Word=list(set(two))
    print(two,"--------------------------Two")
    for Kword1 in Two_Word:
        results1 = soup.body.find_all(string=re.compile('.*{0}.*'.format(Kword1)), recursive=True)
        Total_word2=len(two)
        data1[Kword1] = len(results1)
        density1=round((int(len(results1))/int(Total_word2))*100,2)
        data1[Kword1] = {"freq1": len(results), "density1": density1}



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
        Three_Word1=len(three)
        data2[Kword2] = len(results2)
        density2=round((int(len(results1))/int(Three_Word1))*100,2)
        data2[Kword2] = {"freq2": len(results), "density2": density2}


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
        density4=round((int(val3)/int(Four_word1))*100,2)




    return  {"data":data, "data1": data1, "data2":data2, "data3":data3}


def WordDensity(wrdsrch):

    convert=list(wrdsrch.split(' '))

    frequency={}

    #One OWrd
    for item in convert:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1


        print(frequency)


    two_word=list(map(' '.join, zip(convert[:-1], convert[1:])))
    print(two_word)
    for item in two_word:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    print(frequency)


    # print(convert)
    # three_word=list(map(' '.join, zip(convert[:-2], convert[2:])))
    # print(three_word)


    three=[]
    for i in range(len(convert) - 2):
        three.append(convert[i] + ' ' + convert[i+2])
    print(three)


    return {"frequency":frequency}








