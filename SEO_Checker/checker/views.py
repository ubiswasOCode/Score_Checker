
from django.shortcuts import render
import metadata_parser
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
import re
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager


def Score_checker(request):
    error={}

    warning={}
    value={}
    context = dict()
    url = ''
    if request.method == "POST":
        url = request.POST.get('url')

        if url:

            page=metadata_parser.MetadataParser(url)
            # print(page.metadata)
            #   ------------ MEta Title ----------------------------
            meta_title = {"alert":"", "alert_msg":"", "data": ""}
            title_tag=page.get_metadata('title')
            if len(title_tag) ==0:
                meta_title["alert"] =  "danger"
                meta_title["alert_msg"]  = "Titile is Missing"

                error['title']="titile is Missing"
                # context["meta_title_msg"] = "titile is Missing"
            # print(error)
            elif len(title_tag)>=1  and len(title_tag)<=70:
                meta_title["alert"] =  "success"
                meta_title["alert_msg"]  = f"Congratulations your webpage is using a title tag."
                meta_title["data"] = title_tag

                # context["meta_title_msg"] =f"Congratulations your webpage is using a title tag."
            # print(page.get_metadata('title'))


            else:
                meta_title["alert"] =  "warning"
                meta_title["alert_msg"]  = f"Title should be Greater than 60 characters {len(title_tag)} characters"
                meta_title["data"] = title_tag

                warning['title']=f"Title should be Greater than 60 characters {len(title_tag)} characters"
                context["meta_title_msg"] =f"Title should be Greater than 60 characters {len(title_tag)} characters"

            # print(title_tag,"-------------------title")
            context["meta_title"] = meta_title



            #   ------------ MEta Desc. ----------------------------
            meta_desc={"alert":"", "alert_msg":"", "data": ""}
            desc=page.get_metadata("description")

            if len(desc)==0 :
                meta_desc["alert"] =  "danger"
                meta_desc["alert_msg"]  = "description is Missing"
                meta_desc["alert_msg"]  = "description is Missing"
                meta_desc["data"] =desc

                error['description'] = "description is Missing"
                context["meta_desc_msg"] = "description is Missing"
            elif len(desc) >=1 and len(desc)<= 165 :
                meta_desc["alert"] =  "success"
                meta_desc["alert_msg"]  =f"Congratulations your webpage is using a limited description tag."
                meta_desc["data"] = desc

                context["meta_desc_msg"] = f"Congratulations your webpage is using a limited description tag."

            else:
                meta_desc["alert"] ="warning"
                meta_desc["alert_msg"]  = f"description should be Greater than 160 characters use {len(desc)}  characters"
                meta_desc["data"] = desc


                # print(f"description should be Greater than 160 characters {len(desc)}  characters")
                warning['description'] =f"description should be Greater than 160 characters {len(desc)}  characters"
                context["meta_desc_msg"] = f"description should be Greater than 160 characters {len(desc)}  characters"


            context["meta_desc"] = meta_desc




            # ###--------------------Meta Keywords-------------------------------
            meta_key={"alert":"", "alert_msg":"", "data": ""}
            keyword=page.get_metadata("keywords")
            if keyword is None:
                meta_key["alert"] =  "danger"
                meta_key["alert_msg"]  = "keyword is Missing"
                meta_key["data"] = f" keyword is Missing"

                error['keyword'] = "keyword is Missing"
                context["meta_keyword_msg"]="keyword is Missing"
            elif len(keyword) >= 100 and len(keyword)<=165:
                meta_key["alert"] =  "success"
                meta_key["alert_msg"]  =f"Keyword is Less than 100 keywords"
                meta_key["data"] = keyword

                context["meta_keyword_msg"]=f"Keyword is Less than 100 keywords"


            else:
                meta_key["alert"] =  "warning"
                meta_key["alert_msg"]  =f"Keyword should be Greater than 100 characters use {len(keyword)}  characters"
                meta_key["data"] = keyword

                warning['Keyword'] =f"Keyword should be Greater than 100 characters {len(desc)}  characters"
                context["meta_keyword_msg"]=f"Keyword should be Greater than 100 characters {len(keyword)}  characters"

            context["meta_key"] = meta_key


            #####----------------Repeated Keyword

            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
            text=soup.prettify()
            # remove=re.sub('<[^<]+?>', '', text)
            # print(text)

            frequency={}

            #One OWrd
            for item in text:
                if item in frequency:
                    frequency[item] += 1
                else:
                    frequency[item] = 1


                # print(frequency,"-------------------freqqq")



            # ----------------------Heading H1----------------------------
            page_urls = requests.get(url)
            Soup = BeautifulSoup(page_urls.text, 'lxml')
            # creating a list of all common heading tags
            heading_tags = ["h1"]
            heading1_text = []
            meta_h1={"alert":"", "alert_msg":"", "data": ""}
            # h1_tags = Soup.find_all(heading_tags)
            for tags in Soup.find_all(heading_tags):
                print(tags.name + ' -> ' + tags.text.strip())
                li=(tags.name)
                li1=li.split()
                heading1_text.append(tags.text.strip())

            if len(heading1_text) ==1:
                meta_h1["alert"] =  "success"
                meta_h1["alert_msg"]  =f"Congratulations! Your page contains headings. Their contents are listed below:"
                meta_h1["data"] = heading1_text


                context["meta_h1_msg"]=f"Congratulations! Your page contains headings. Their contents are listed below:"


            elif len(heading1_text) ==2:
                meta_h1["alert"] =  "warning"
                meta_h1["alert_msg"]  =f"Your page contains headings two or more heading tag"
                meta_h1["data"] = heading1_text


                warning['h1'] =f"Your page contains headings two or more heading tag"
                context["meta_h1_msg"]=f"Your page contains headings two or more heading tag"

            else:
                meta_h1["alert"] =  "danger"
                meta_h1["alert_msg"]  = f"h1 is Missing"
                meta_h1["data"] = f"h1 is Missing"

                error['h1'] = "h1 is Missing"
                context["meta_h1_msg"]=f"h1 is Missing"


            # print(len(heading1_text),"---------------h111111")

            context["meta_h1"] = meta_h1

            # #

            # ##---------------------H2 Tags--------------------------
            heading2_tags = ["h2"]
            heading2_text = []
            h2_tags = Soup.find_all(heading_tags)
            meta_h2={"alert":"", "alert_msg":"", "data": ""}
            for tags2 in Soup.find_all(heading2_tags):
                print(tags2.name + ' -> ' + tags2.text.strip())
                # print(tags,"---------------tags")
                convert_lst = (tags2.name)
                convert_split = convert_lst.split()
                heading2_text.append(tags2.text.strip())
            # listToStrh2 = ' '.join(map(str, heading2_text))
            if len(heading2_text) ==2:
                meta_h2["alert"] =  "success"
                meta_h2["alert_msg"]  =f"Congratulations! Your page contains headings. Their contents are listed below:"
                meta_h2["data"] = heading2_text

                context["meta_h2_msg"]=f"Congratulations! Your page contains headings. Their contents are listed below:"

            elif len(heading2_text)>=2 and len(heading2_text) <=4:
                meta_h2["alert"] =  "warning"
                meta_h2["alert_msg"]  =f"Your page contains headings two or more heading tag"
                meta_h2["data"] = heading2_text

                warning['h2'] = f"Your page contains headings two or more heading tag"
                context["meta_h2_msg"]=f"Your page contains headings two or more heading tag"
            else:

                meta_h2["alert"] =  "danger"
                meta_h2["alert_msg"]  = f"h2 is Missing"
                meta_h2["data"] = heading2_text

                error['h2'] = "h2 is Missing"
                context["meta_h2_msg"]=f"h2 is Missing"
            # context["heading2_tags"] = heading2_tags

            context["meta_h2"] = meta_h2



            ##--------------------H3 Tags----------------
            heading3_tags = ["h3"]
            heading3_text = []
            h3_tags = Soup.find_all(heading3_tags)
            meta_h3={"alert":"", "alert_msg":"", "data": ""}
            for tags3 in h3_tags:
                heading3_text.append(tags3.text.strip())

            if len(h3_tags) ==3:
                meta_h3["alert"] =  "success"
                meta_h3["alert_msg"]  =f"Congratulations! Your page contains headings. Their contents are listed below:"
                meta_h3["data"] = heading3_text

                context["meta_h3_msg"]=f"Congratulations! Your page contains headings. Their contents are listed below:"
                # context["heading3_text"] = heading3_text

            elif len(h3_tags)>=3 and len(h3_tags) <= 9:
                meta_h3["alert"] =  "warning"
                meta_h3["alert_msg"]  =f"Your page contains headings two or more heading tag"
                meta_h3["data"] = heading3_text

                warning['h3'] = f"Your page contains headings two or more heading tag"
                context["meta_h3_msg"]=f"Your page contains headings two or more heading tag"
            else:
                meta_h3["alert"] =  "danger"
                meta_h3["alert_msg"]  = f"h3 is Missing"

                error['h3'] = "h3 is Missing"
                context["meta_h3_msg"]=f"h3 is Missing"

            context["meta_h3"] = meta_h3

            # #
            # # ##For Images
            #

            imag={"alert":"", "alert_msg":"", "data": ""}
            # for image in images:
            image = []
            all_img = Soup.findAll('img')
            if len(all_img) == 0:
                imag["alert"] =  "danger"
                imag["alert_msg"]  = f"No Img tag Found, Images can help your user to understand about a topic easily."

                error['img'] = "img is Missing"
                context["img_msg"]=f"img Tag is Missing"

            elif len(all_img) >= 100 :
                imag["alert"] =  "warning"
                imag["alert_msg"]  =f"Your webpage use {len(all_img)} but maximum use 100."
                imag["data"] = all_img

                warning['img'] = f"Your webpage has 200 'img' tags and all of them has the required {len(image)} attribute."
                context["img_msg"]=f"Your webpage has 200 'img' tags and all of them has the required {len(image)} attribute."
            else:
                imag["alert"] =  "success"
                imag["alert_msg"]  =f"your webpage is used limited image "
                imag["data"] = all_img

                context["img_msg"]=f"your webpage is used limited image "
            # print(all_img,"----------------------------imagess")
            context["imag"] = imag


            # #
            # #
            # ##Style Tags

            style_tags =Soup.findAll('div''style')
            meta_style={"alert":"", "alert_msg":"", "data": ""}
            for tags in Soup.find_all(style_tags):
                taggg=tags.name + ' -> ' + tags.text.strip()

                if len(taggg) is None:
                    meta_style["alert"] =  "danger"
                    meta_style["alert_msg"]  = f"Inline CSS is Missing"

                    error['style'] = "style is Missing"
                    context["style_msg"]=f"Inline CSS is Missing"
                elif len(taggg) >= 100:
                    meta_style["alert"] =  "warning"
                    meta_style["alert_msg"]  =f"Your webpage is using{len(taggg)}inline CSS styles"
                    meta_style["data"] = style_tags

                    warning['style'] = f"Style Tag should be Greater than 100 use {len(taggg)} "
                    context["style_msg"]=f"Your webpage is using{len(taggg)}inline CSS styles"
                else:
                    meta_style["alert"] =  "success"
                    meta_style["alert_msg"]  =f"Congratulations! Your webpage is not using any inline CSS styles."
                    meta_style["data"] = style_tags

                    # print(f"your webpage is used limited style tag")
                    context["style_msg"]=f"Congratulations! Your webpage is not using any inline CSS styles."

                # print(len(style_tags),"------------------style,,,,,")
                context["meta_style"] = meta_style


            ####----------------SEO Friendly----------------
            # html = requests.get(url).content
            # soup = BeautifulSoup(html, "html.parser")
            # links = [a["href"] for a in soup.find_all("a", href=True)]

            # print(links,"Total link ----------------")

            # # ##--------------anchor tag----------------------

            meta_anc={"alert":"", "alert_msg":"", "data": ""}
            all_anc = Soup.findAll('a')
            if len(all_anc) == 0:
                meta_anc["alert"] =  "danger"
                meta_anc["alert_msg"]  = f"anchor tag is Missing"
                meta_anc["data"] = all_anc

                error['a'] = "anchor tag is Missing"
                context["anc_msg"]=f"anchor tag is Missing"
            elif len(all_anc) >= 100:
                meta_anc["alert"] =  "warning"
                meta_anc["alert_msg"]  =f"anchor Tag should be Greater than 100 your webpage use {len(all_anc)} "
                meta_anc["data"] = all_anc

                warning['a'] = f"anchor Tag should be Greater than 100 your webpage use {len(all_anc)} "
                context["anc_msg"]=f" anchor Tag should be Greater than 100 your webpage use {len(all_anc)} "

            else:
                meta_anc["alert"] =  "success"
                meta_anc["alert_msg"]  =f"Congratulations! Your page contains limited anchor tag."
                meta_anc["data"] = all_anc

                context["anc_msg"]=f"your webpage is used limited anchor tag"

            # print(len(all_anc),"---------Anchoorrrrrrr")
            context["meta_anc"]=meta_anc


            ####----------------------------ViewPort ----------------------
            meta_view={"alert":"", "alert_msg":"", "data": ""}
            view_port=page.get_metadata("viewport")
            if view_port is None:
                meta_view["alert"] =  "danger"
                meta_view["alert_msg"]  = f"Viewport Not used"

                context["meta_view_msg"] ="No Viewport"

            else:
                meta_view["alert"] =  "success"
                meta_view["alert_msg"]  = f"Viewport is used"
                context["meta_view_msg"] =f"Viewport is used"
            # print(meta_view)
            context["meta_view"] = meta_view


            #Check Robot.Txt File Is availabale or not
            robots = requests.get(url+"/robots.txt")
            meta_robot={"alert":"","data": ""}
            if robots is None:
                meta_robot["alert"] =  "danger"
                meta_robot["alert_msg"]  = f"Robbot File is Missing"

                error['rob_mess'] =f"Robbot File is Missing"
            else:
                # print(f"Robot.txt is Available")
                meta_robot["alert"] =  "success"
                meta_robot["alert_msg"]  =f"Congratulations! Your web page contains Robbot.txt File"
                meta_robot["data"] = robots

                context['rob_mess'] =f"Congratulations! Your web page contains Robbot.txt File"

            context["meta_robot"]=meta_robot


            #Check sitemap.xml File Is availabale or not
            # print(url)
            site_map = requests.get(url+"/sitemap.xml")
            meta_site={"alert":"","data": ""}
            if site_map is None:
                # print(f"Sitemap.xml File is Missing")
                meta_site["alert"] =  "danger"
                meta_site["alert_msg"]  = f"Sitemap.xml File is Missing"

                error['site_mess'] =f"Sitemap.xml File is Missing"
            else:
                # print(f"Sitemap.xml is Available")
                meta_site["alert"] =  "success"
                meta_site["data"] = robots
                meta_site["alert_msg"]  =f"Congratulations! Your web page contains Sitemap.xml File"

                context["site_mess"]=f"Sitemap.xml is Available"

            context['meta_site']=meta_site




            # print(site_map,"_____-abi")

            ERR=1
            WARN=0.5

            err=len(error)
            warn=len(warning)
            # print(warning)
            # print(error)

            # print(err)
            # print(warn)

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




    ######------------------------------------Page Opening Time--------------------
        # driver = webdriver.Chrome(ChromeDriverManager().install())

        # driver.get(url)
        # load_time = driver.execute_script(
        # """
        # var loadTime = ((window.performance.timing.domComplete- window.performance.timing.navigationStart)/1000)+" sec.";
        # return loadTime;
        # """
        # )

        # print(load_time,"---------------------------Time")

        # driver.close()



        ##Calculate Time
        # driver=webdriver.Chrome('/home/ocode-22/chromedriver')
        # driver.get('url')
        # meta_time= {"alert":"","data": ""}
        # load_time = driver.execute_script(
        #         """
        #         var loadTime = ((window.performance.timing.domComplete- window.performance.timing.navigationStart)/1000)+" sec.";
        #         return loadTime;
        #         """
        #         )


        # print(load_time,"---------------------------Time")

        ###Favicon
        favcon_tag ={"alert":"","data": ""}
        fav_icon=Soup.findAll('favicon')
        if fav_icon is None:
            favcon_tag["alert"] =  "danger"
            favcon_tag["alert_msg"]  = f"Your website Not Using favicon..."
            favcon_tag["data"] = fav_icon

            error['favicon_img']="Https is Missing"
            context["meta_favicon_msg"] = f"Your website Not Using favicon..."
        else:

            favcon_tag["alert"] =  "success"
            favcon_tag["alert_msg"]  = f"Congratulations Your website appears to have a favicon. "
            favcon_tag["data"] = fav_icon

            context["meta_favicon_msg"] =f"Congratulations Your website appears to have a favicon.."

        print("httpppppppppppp--------------------------")

        context['favcon_tag']=favcon_tag


        ####-------------------------IFramne Checker--------------------
        meta_iframe={"alert":"","data": ""}
        iframe_tag=page.get_metadata('iframe')
        if iframe_tag is None:
            meta_iframe["alert"] =  "success"
            meta_iframe["alert_msg"]  = "Congratulations! Your webpage does not use frames."

            error['iframe_err']="titile is Missing"
            context["meta_iframe_msg"] = "Congratulations! Your webpage does not use frames."

            print("Iframne None--------------------------")
        else:
            meta_iframe["alert"] =  "danger"
            meta_iframe["alert_msg"]  = f"Congratulations your webpage is using Iframe tag."
            meta_iframe["data"] = iframe_tag

            context["meta_iframe_msg"] =f"Congratulations your webpage is using Iframe tag."
            print(iframe_tag,"IFramne Yes-----------------")

        context['meta_iframe']=meta_iframe



        ####-------------------------IDoctyp Checker--------------------
        meta_doc={"alert":"","data": ""}
        page=metadata_parser.MetadataParser(url)
        if "!DOCTYPE html>" or"<!DocType html>"or "<!Doctype html>"or "<!doctype html" in page:
            meta_doc["alert"] =  "success"
            meta_doc["alert_msg"]  = f"Congratulations! Your website has a doctype declaration."
            meta_doc["data"] = page

            context["meta_doc_msg"] =f"Congratulations! Your website has a doctype declaration."

            print("Doctype Yes--------------------------")

        else:

            meta_doc["alert"] =  "danger"
            meta_doc["alert_msg"]  = "Doctype Not Use"

            error['doc']="titile is Missing"
            context["meta_doc_msg"] = "Doctype Not Use"
            print("Doctype none-----------------")
        print(meta_doc,"--------------------------Doctype")
        context['meta_doc']=meta_doc



        #####-------------Minify CSS-----------
        minify={"alert":"","data":""}
        r = requests.get(url)
        # print(r.content)
        remove=re.sub('\s+',' ','\n'+str(r.content))
        # print(remove,"=========================minify")
        if len(remove)>=1:
            minify["alert"]="success"
            minify["alert_msg"]="Congratulations! Your webpage CSS resources are minified"

        else:

            minify["alert"]="danger"
            minify["alert_msg"]="! Your webpage CSS resources are not minified"

        context['minify']=minify


        ####------------Preloader-------------
        loader={"alert":"","alert_msg":""}
        sibling_soup = Soup.findAll('link')

        if len(sibling_soup)>= 1:
            loader["alert"]="success"
            loader["alert_msg"]="Congratulations! Your webpage is using rel-preload"

        else:

            loader["alert"]="danger"
            loader["alert_msg"]="! Your webpage is not using rel-preload"

        context['loader']=loader

        ####---------------Script


        ####--------Minify or not
        # data = """<script>
        #         window.addEventListener('load', function (e)
        #             {
        #                 i = 4;
        #             });
        #             </script>
        #         """

        # soup = BeautifulSoup(data, 'lxml')
        # script = soup.select_one('script')
        # r = requests.post(url, data={"source":script.text, "type" :"js"})
        # json_data = json.loads(r.text)
        # script.clear()
        # script.append(json_data['minified'])

        # print(script,"-------------------------Minifiedss")



        ###---------------------Check Donmain Name Samne or Not -----------------
        # o = urlparse(url)

        # domain = o.hostname

        # temp = domain.rsplit('.')

        # if(len(temp) == 3):
        #     domain = temp[1] + '.' + temp[2]
        #     print("Great, a redirect is in place to redirect traffic from your non-preferred domain. Your website directs "+url+" and "+domain+" to the same URL.")

        # else:
        #     print("not Same url or Domain Name")


        #####-----------------Check The Website used Http or Https---------------
        meta_host={"alert":"", "alert_msg":""}
        if "https:" in url:
            meta_host["alert"] =  "success"
            meta_host["alert_msg"]  = f"Your website is successfully using https, a secure communication protocol over the Internet. "


            context["meta_host_msg"] =f"Your website is successfully using https, a  over the Internet."

            print("yes https==============")
        elif "http:" in url:
            meta_host["alert"] =  "danger"
            meta_host["alert_msg"]  = f"Your website is not using https, a  over the Internet."

            error['host']="Https is Missing"
            context["meta_host_msg"] = f"Your website is not using https, a  over the Internet."

            print("httpppppppppppp--------------------------")

        context['meta_host']=meta_host


        #####--------------------Secure or Not------------------####
        meta_secure={"alert":"", "alert_msg":""}
        if "https:" in url:
            meta_secure["alert"] =  "success"
            meta_secure["alert_msg"]  = f"This site is not currently listed as suspicious (no malware or phishing activity found). "


            context["meta_host_msg"] =f"This site is not currently listed as suspicious (no malware or phishing activity found)."

            # print("Secure Protocol is used")
        else:
            meta_secure["alert"] =  "danger"
            meta_secure["alert_msg"]  = f"This site is not currently listed as suspicious (no malware or phishing activity found)."

            error['host']="Https is Missing"
            context["meta_host_msg"] = f"This site is not currently listed as suspicious (no malware or phishing activity found)."
            # print("Not Used Sceure--------------------------")
        context['meta_secure']=meta_secure


      ###-------------------Directory Browsing use or not-------------------------
        meta_dir={"alert":"", "alert_msg":""}
        dir_tag = Soup.findAll('dir')
        print(dir_tag,"------dir is use")
        if len(dir_tag) >= 0 :
            meta_dir["alert"] =  "success"
            meta_dir["alert_msg"]  = f"Congratulations! Your server has disabled directory browsing."


            context["meta_dir_msg"] =f"Congratulations! Your server has disabled directory browsing."

        else:
            meta_dir["alert"] =  "danger"
            meta_dir["alert_msg"]  = f" Your server has enabled directory browsing.."

            error['dirtag']="dir is Missing"
            context["meta_dir_msg"] = f"Your server has enabled directory browsing."
            # print("Not Used Sceure--------------------------")
        print(dir_tag,"------dir is use")
        context['meta_dir']=meta_dir




    return render(request,"SeoChecknew.html",{"context":context,"value":value, 'url':url})

def Home(request):

    return render(request, "Boot_head_foot.html")











