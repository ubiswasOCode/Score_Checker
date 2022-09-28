from django.shortcuts import render
import metadata_parser
import requests
from bs4 import BeautifulSoup

def Score_checker(request):
    error={}

    warning={}
    value={}
    context = dict()
    if request.method == "POST":
        url = request.POST.get('url')
    
        if url:

            page=metadata_parser.MetadataParser(url)
            # print(page.metadata)
            #   ------------ MEta Title ----------------------------
            meta_title = {"alert":"", "alert_msg":"", "data": ""}
            title_tag=page.get_metadata('title')
            if title_tag is None:
                meta_title["alert"] =  "danger"
                meta_title["alert_msg"]  = "Titile is Missing" 

                error['title']="titile is Missing"
                context["meta_title_msg"] = "titile is Missing" 
            # print(error)
            elif len(title_tag)>=30  and len(title_tag)<=350:
                meta_title["alert"] =  "warning"
                meta_title["alert_msg"]  = f"Title should be Greater than 60 characters {len(title_tag)} characters" 
                meta_title["data"] = title_tag

                warning['title']=f"Title should be Greater than 60 characters {len(title_tag)} characters"
                context["meta_title_msg"] =f"Title should be Greater than 60 characters {len(title_tag)} characters"
            else:
                meta_title["alert"] =  "success"
                meta_title["alert_msg"]  = f"Congratulations your webpage is using a title tag."
                meta_title["data"] = title_tag

                context["meta_title_msg"] =f"Congratulations your webpage is using a title tag."
            # print(page.get_metadata('title'))
            # print(title_tag)
            context["meta_title"] = meta_title



            #   ------------ MEta Desc. ----------------------------
            meta_desc={"alert":"", "alert_msg":"", "data": ""}
            desc=page.get_metadata("description")

            if desc is None:
                meta_desc["alert"] =  "danger"
                meta_desc["alert_msg"]  = "description is Missing" 

                error['description'] = "description is Missing"
                context["meta_desc_msg"] = "description is Missing" 
            elif len(desc) >= 160 :
                meta_desc["alert"] =  "warning"
                meta_desc["alert_msg"]  = f"description should be Greater than 160 characters {len(desc)}  characters"
                meta_desc["data"] = desc


                # print(f"description should be Greater than 160 characters {len(desc)}  characters")
                warning['description'] =f"description should be Greater than 160 characters {len(desc)}  characters"
                context["meta_desc_msg"] = f"description should be Greater than 160 characters {len(desc)}  characters"
            else:
                meta_desc["alert"] =  "success"
                meta_desc["alert_msg"]  =f"Congratulations your webpage is using a limited description tag."
                meta_desc["data"] = desc
                
                context["meta_desc_msg"] = f"Congratulations your webpage is using a limited description tag."
                
            
            context["meta_desc"] = meta_desc
          



            # ###--------------------Meta Keywords-------------------------------
            meta_key={"alert":"", "alert_msg":"", "data": ""}
            keyword=page.get_metadata("keywords")
            if keyword is None:
                meta_key["alert"] =  "danger"
                meta_key["alert_msg"]  = "keyword is Missing" 

                error['keyword'] = "keyword is Missing"
                context["meta_keyword_msg"]="keyword is Missing"
            elif len(keyword) >= 10:
                meta_key["alert"] =  "warning"
                meta_key["alert_msg"]  =f"Keyword should be Greater than 10 characters {len(desc)}  characters"
                meta_key["data"] = keyword

                warning['Keyword'] =f"Keyword should be Greater than 10 characters {len(desc)}  characters"
                context["meta_keyword_msg"]=f"Keyword should be Greater than 10 characters {len(desc)}  characters"
            else:
                meta_key["alert"] =  "success"
                meta_key["alert_msg"]  =f"Keyword is Less than 10 keywords"
                meta_key["data"] = keyword

                context["meta_keyword_msg"]=f"Keyword is Less than 10 keywords"
          
            context["meta_key"] = meta_key
          

            # ----------------------Heading H1----------------------------
            page_urls = requests.get(url)
            Soup = BeautifulSoup(page_urls.text, 'lxml')
            # creating a list of all common heading tags
            heading_tags = ["h1"]
            heading1_text = []
            meta_h1={"alert":"", "alert_msg":"", "data": ""}
            h1_tags = Soup.find_all(heading_tags)
            for tags in Soup.find_all(heading_tags):
                print(tags.name + ' -> ' + tags.text.strip())
                li=(tags.name)
                li1=li.split()
                heading1_text.append(tags.text.strip())
                # print(li1)
            if len(h1_tags) is None:
                meta_h1["alert"] =  "danger"
                meta_h1["alert_msg"]  = f"h1 is Missing"

                error['h1'] = "h1 is Missing"
                context["meta_h1_msg"]=f"h1 is Missing"
            elif len(h1_tags) >=2:
                meta_h1["alert"] =  "warning"
                meta_h1["alert_msg"]  =f"Your page contains headings two or more heading tag"
                meta_h1["data"] = h1_tags


                warning['h1'] =f"Your page contains headings two or more heading tag"
                context["meta_h1_msg"]=f"Your page contains headings two or more heading tag"
            
            else:
                meta_h1["alert"] =  "success"
                meta_h1["alert_msg"]  =f"Congratulations! Your page contains headings. Their contents are listed below:"
                meta_h1["data"] = h1_tags

               
                context["meta_h1_msg"]=f"Congratulations! Your page contains headings. Their contents are listed below:"

            # context["heading_tags"] = heading_tags
            context["meta_h1"] = meta_h1
            
            # #

            # ##---------------------H2 Tags--------------------------
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
                warning['h2'] = f"Your page contains headings two or more heading tag"
                context["meta_h2_msg"]=f"Your page contains headings two or more heading tag"
            else:
                print(f"Congratulations! Your page contains headings. Their contents are listed below:")
                context["meta_h2_msg"]=f"Congratulations! Your page contains headings. Their contents are listed below:"
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
                warning['h3'] = f"Your page contains headings two or more heading tag"
                context["meta_h3_msg"]=f"Your page contains headings two or more heading tag"
            else:
                print(f"Congratulations! Your page contains headings. Their contents are listed below:")
                context["meta_h3_msg"]=f"Congratulations! Your page contains headings. Their contents are listed below:"
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
                        warning['img'] = f"Your webpage has 200 'img' tags and all of them has the required {len(images)} attribute."
                        context["img_msg"]=f"Your webpage has 200 'img' tags and all of them has the required {len(images)} attribute."
                    else:
                        print(f"your webpage is used limited image ")
                        context["img_msg"]=f"your webpage is used limited image "
            
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
                    warning['style'] = f"Style Tag should be Greater than 100 characters {len(taggg)} characters"
                    context["style_msg"]=f"Style Tag should be Greater than 100 characters {len(taggg)} characters"
                else:
                    print(f"your webpage is used limited style tag")
                    context["style_msg"]=f"your webpage is used limited style tag"
            
            
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
                        warning['a'] = f"anchor Tag should be Greater than 100 characters {len(anc)} characters"
                        context["anc_msg"]=f"anchor Tag should be Greater than 100 characters {len(anc)} characters"
                    else:
                        print(f"Congratulations! Your page contains anchor ")
                        context["anc_msg"]=f"Congratulations! Your page contains anchor "
            
            #Check Robot.Txt File Is availabale or not          
            # print(url)
            robots = requests.get(url+"/robots.txt")
            print(robots,"--------------file")
        
            if robots is None:  
                print(f"Robbot File is Missing")
                error['rob_mess'] =f"Robbot File is Missing"
            else:
                print(f"Robot.txt is Available")
                context["rob"]=f"Robot.txt is Available"


            
            #Check sitemap.xml File Is availabale or not          
            # print(url)
            site_map = requests.get(url+"/sitemap.xml")
            print(robots,"--------------file")
        
            if site_map is None:
                print(f"Sitemap.xml File is Missing")
                error['site_mess'] =f"Sitemap.xml File is Missing"
            else:
                print(f"Sitemap.xml is Available")
                context["site"]=f"Sitemap.xml is Available"
            print(site_map,"_____-abi")
            
            ERR=1
            WARN=0.5

            err=len(error)
            warn=len(warning)
            print(warning)
            print(error)
            
            print(err)
            print(warn)

            case=11
            temp=case
            total_right=err+warn
            total_correct=case-total_right
            print(total_correct,"-------------------Correct")


            for i in range(1,err+1):
                temp=temp-ERR
                # print(temp,"-------error")

            for j in range(1,warn+1):
                temp=temp-WARN
                # print(temp,"---------warn")

            percent=(temp/case)*100
            per=round(percent)
            
            value={ 
                    "error":error,
                    "warning":warning,
                    "err":err,
                    "warn":warn,
                    "total_correct":total_correct,
                    "per":per}


        
    return render(request,"SeoChecknew.html",{"context":context,"value":value})

def Home(request):
    
    return render(request, "Boot_head_foot.html")










