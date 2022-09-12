from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
import metadata_parser
import requests

from bs4 import BeautifulSoup

def Score_checker(request):
    
    url=request.GET.get('url')
    context = dict()

    error={}

    warning={}
    value={}
    
    if url:

        page=metadata_parser.MetadataParser(url)
        # print(page.metadata)

        title_tag=page.get_metadata('title')
        print("Congratulations your webpage is using a title tag.")

        if title_tag is None:
            error['title']="titile is Missing"
            context["meta_title_msg"] = "titile is Missing" 
        # print(error)
        elif len(title_tag)>=30  and len(title_tag)<=350:
            warning['title']="titile is big"
            context["meta_title_msg"] =f"Title should be Greater than 60 characters {len(title_tag)} characters"
        else:
            print(f"title is best")
            context["meta_title_msg"] =f"title is best"
        # print(page.get_metadata('title'))
        # print(title_tag)
        context["title_tag"] = title_tag
        print()


        desc=page.get_metadata("description")
        if desc is None:
            error['description'] = "description is Missing"
            context["meta_desc_msg"] = "description is Missing" 
        elif len(desc) >= 160 :
            # print(f"description should be Greater than 160 characters {len(desc)}  characters")
            warning['description'] = "description is Big"
            context["meta_desc_msg"] = f"description should be Greater than 160 characters {len(desc)}  characters"
        else:
            print(f"description is best")
            context["meta_desc_msg"] = f"description is best"
            
        print(page.get_metadata('description'))
        context["desc"] = desc
        print()
        print()


        keyword=page.get_metadata("keywords")
        if keyword is None:
            error['keyword'] = "keyword is Missing"
            context["meta_keyword_msg"]="keyword is Missing"
        elif len(keyword) >= 10:
            warning['Keyword'] = "Keyword is huge"
            context["meta_keyword_msg"]="Keyword is huge"
        else:
            print(f"Keyword is Less than 10 keywords")
            context["meta_keyword_msg"]=f"Keyword is Less than 10 keywords"
        print(page.get_metadata("keywords"))
        context["keyword"] = keyword
        print()
        print()
        

        page_urls = requests.get(url)
        Soup = BeautifulSoup(page_urls.text, 'lxml')
        # creating a list of all common heading tags
        heading_tags = ["h1"]
        heading1_text = []
        h1_tags = Soup.find_all(heading_tags)
        for tags in Soup.find_all(heading_tags):
            print(tags.name + ' -> ' + tags.text.strip())
            li=(tags.name)
            li1=li.split()
            heading1_text.append(tags.text.strip())
            # print(li1)
        if len(h1_tags) is None:
            error['h1'] = "h1 is Missing"
            context["meta_h1_msg"]=f"h1 is Missing"
        elif len(h1_tags) >=2:
            warning['h1'] = "h1 is huge"
            context["meta_h1_msg"]=f"h1 is huge"
        else:
            print(f"it h1 is Best")
            context["meta_h1_msg"]=f"it h1 is Best"

        # context["heading_tags"] = heading_tags
        context["heading1_text"] = heading1_text
        
        # #
        # ##H2 Tags
        heading2_tags = ["h2"]
        heading2_text = []
        h2_tags = Soup.find_all(heading_tags)
        for tags2 in Soup.find_all(heading2_tags):
            print(tags2.name + ' -> ' + tags2.text.strip())
            # print(tags,"---------------tags")
            convert_lst = (tags2.name)
            convert_split = convert_lst.split()
            heading2_text.append(tags2.text.strip())
        if len(h2_tags) is None:
            error['h2'] = "h2 is Missing"
            context["meta_h2_msg"]=f"h2 is Missing"
        elif len(h2_tags) >=2:
            warning['h2'] = f"h2 is huge"
            context["meta_h2_msg"]=f"h2 is huge"
        else:
            print("h2 is Best")
            context["meta_h2_msg"]=f"it h2 is Best"
        # context["heading2_tags"] = heading2_tags
        context["heading2_text"] = heading2_text
            

        ##H3 Tags
        heading3_tags = ["h3"]
        heading3_text = []
        h3_tags = Soup.find_all(heading3_tags)
        for tags3 in h3_tags:
            heading3_text.append(tags3.text.strip())
        if len(h3_tags) is None:
            error['h3'] = "h3 is Missing"
            context["meta_h3_msg"]=f"h3 is Missing"
        elif len(h3_tags) >= 3:
            warning['h3'] = "h3 is huge"
            context["meta_h3_msg"]=f"h3 is huge"
        else:
            print("h3 is Best")
            context["meta_h3_msg"]=f"h3 is Best"
        context["heading3_text"] = heading3_text
        
                
        # #
        # # ##For Images
        #
        images = Soup.findAll('img')
        for image in images:
            image = []
            for img in Soup.findAll('img'):
                image.append(img.get('src'))
                if len(images) is None:
                    error['img'] = "img is Missing"
                    context["img_msg"]=f"img is Missing"
                elif len(images) >= 200 :
                    warning['img'] = "img is huge"
                    context["img_msg"]=f"img is huge"
                else:
                    print("image is Best")
                    context["img_msg"]=f"img is best"
        
        # #
        # #
        # ##Style Tags
        style_tags = ["style"]
        for tags in Soup.find_all(style_tags):
            taggg=tags.name + ' -> ' + tags.text.strip()

            if len(taggg) is None:
                error['style'] = "style is Missing"
                context["style_msg"]=f"style is Missing"
            elif len(taggg) >= 100:
                warning['style'] = "style is huge"
                context["style_msg"]=f"style is huge"
            else:
                print("style is Best")
                context["style_msg"]=f"Style tag is best"
        
        
        # # ##Underscore
        anc=[]
        for link in Soup.find_all('a'):
            under=link.get('href')
            if "_" in under:
                anc.append(under)
                if len(anc) is None:
                    error['a'] = "anchor tag is Missing"
                    context["anc_msg"]=f"anchor tag is Missing"
                elif len(anc) >= 100:
                    warning['a'] = "anchor tag is huge"
                    context["anc_msg"]=f"anchor tag is huge"
                else:
                    print("anchor tag is Best")
                    context["anc_msg"]=f"anchor tag is Best"
          
          
        #Check Robot.Txt File Is availabale or not          
        # print(url)
        robots = requests.get(url+"/robots.txt")
        print(robots,"--------------file")
       
        if robots is None:
            error['rob_mess'] = "Robbot File is Missing"
        else:
            context["rob"]=f"Robot.txt is Available"


        
        #Check sitemap.xml File Is availabale or not          
        # print(url)
        site_map = requests.get(url+"/sitemap.xml")
        print(robots,"--------------file")
       
        if site_map is None:
            error['site_mess'] = "Sitemap.xml File is Missing"
        else:
            context["site"]=f"Sitemap.xml is Available"
        print(site_map,"_____-abi")
        
        ERR=1
        WARN=0.5

        err=len(error)
        warn=len(warning)
        print(err)
        print(warn)

        case=11
        temp=case


        for i in range(1,err+1):
            temp=temp-ERR
            # print(temp,"-------error")

        for j in range(1,warn+1):
            temp=temp-WARN
            # print(temp,"---------warn")

        percent=(temp/case)*100
        print(percent)
        
           
        value={"err":err,
                "warn":warn,
                "percent":percent}

     
    return render(request,"SeoTool.html",{"context":context,"value":value})












