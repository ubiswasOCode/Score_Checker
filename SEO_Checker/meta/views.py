from bs4 import BeautifulSoup
from django.shortcuts import render
# Create your views here.
from multiprocessing import context
from re import template
import requests
from django.http import HttpResponse
from django.shortcuts import render
import metadata_parser
# Create your views here.
def Meta(request):

    url=""
    context = dict()
    if request.method == "POST":
        url = request.POST.get('url')


        page=metadata_parser.MetadataParser(url)

        meta_title = {"alert":"", "alert_msg":"", "data": ""}
        meta_tag=page.get_metadata('title')
        if len(meta_tag)==0:
            context["meta_title_msg"] = "Title Not Found"
            meta_title["alert"] =  "danger"
            meta_title["alert_msg"]  = "Titile is Missing"
            meta_title["data"]="Titile is Missing"

            # error['title']="titile is Missing"

        elif len(meta_tag)>=1  and len(meta_tag)<=70:
            meta_title["alert"] =  "success"
            meta_title["alert_msg"]  = f"Congratulations your webpage is using a title tag."
            meta_title["data"] = meta_tag
            context["meta_title_msg"] =f"Title should be Greater than 60 characters {len(meta_tag)} characters"
        else:
            meta_title["alert"] =  "warning"
            meta_title["alert_msg"]  = f"Title should be Greater than 60 characters {len(meta_tag)} characters"
            meta_title["data"] = meta_tag
            context["meta_title_msg"] = f"title is smaller than 60 characters {len(meta_tag)} characters"

        context["meta_title"] = meta_title

        desc={"alert":"", "alert_msg":"", "data": ""}
        meta_desc=page.get_metadata("description")
        if len(meta_desc)==0:
            desc["alert"] =  "danger"
            desc["alert_msg"]  = "description is Missing"
            desc["data"] = "description is Missing"
            context["meta_desc_msg"] = "Description not Found"
        elif len(desc) >=1 and len(desc)<= 165 :
            desc["alert"] =  "success"
            desc["alert_msg"]  =f"Congratulations your webpage is using a limited description ."
            desc["data"] = meta_desc
            context["meta_desc_msg"] =f"Description should be Greater than 60 characters {len(meta_desc)}  characters"
        else:
            desc["alert"] ="warning"
            desc["alert_msg"]  = f"description should be Greater than 160 characters use {len(meta_desc)}  characters"
            desc["data"] = meta_desc
            context["meta_desc_msg"] =f"Description is smaller than 60 characters {len(meta_desc)}characters"

        context["desc"] = desc


        keyword={"alert":"", "alert_msg":"", "data": ""}
        meta_key=page.get_metadata("keywords")
        if meta_key is None:
            keyword["alert"] =  "danger"
            keyword["alert_msg"]  = "keyword is Missing"
            keyword["data"] = f" keyword is Missing"
            context["meta_key_msg"] = "No keywords found"
        elif len(meta_key) >= 100 and len(meta_key)<=165:
            keyword["alert"] =  "success"
            keyword["alert_msg"]  =f"Keyword is Less than 100 keywords"
            keyword["data"] = meta_key
            context["meta_keyword_msg"]=f"Keyword is Less than 100 keywords"
        else:
            keyword["alert"] =  "warning"
            keyword["alert_msg"]  =f"Keyword should be Greater than 100 characters use {len(meta_key)} characters"
            keyword["data"] = meta_key

        context["keyword"] = keyword


        page_urls = requests.get(url)
        Soup = BeautifulSoup(page_urls.text, 'lxml')
        meta_anc={"alert":"", "alert_msg":"", "data": ""}
        all_anc = Soup.findAll('a')
        if len(all_anc) == 0:
            meta_anc["alert"] =  "danger"
            meta_anc["alert_msg"]  = f"anchor tag is Missing"
            meta_anc["data"] = all_anc
            context["anc_msg"]=f"anchor tag is Missing"

        elif len(all_anc) >= 100:
            meta_anc["alert"] =  "warning"
            meta_anc["alert_msg"]  =f"anchor Tag  Greater than 100 your webpage contains {len(all_anc)} "
            meta_anc["data"] = all_anc
            context["anc_msg"]=f" anchor Tag  Greater than 100 your webpage contains {len(all_anc)} "

        else:
            meta_anc["alert"] =  "success"
            meta_anc["alert_msg"]  =f"Congratulations! Your page contains limited anchor tag."
            meta_anc["data"] = all_anc
            context["anc_msg"]=f"your webpage is used limited anchor tag"

        context["meta_anc"]=meta_anc


        view_port={"alert":"", "alert_msg":"", "data": ""}
        meta_view=page.get_metadata("viewport")
        if meta_view is None:
            view_port["alert"] =  "danger"
            view_port["alert_msg"]  = f"Viewport Not used"
            view_port["data"] = meta_view
            context["meta_view_msg"] ="No Viewport"
        else:
            view_port["alert"] =  "success"
            view_port["alert_msg"]  = f"Viewport is used"
            view_port["data"] = meta_view
            context["meta_view_msg"] =f"Viewport is used"

        context["view_port"] = view_port


        meta_robot={"alert":"","data": ""}
        robots = requests.get(url+"/robots.txt")
        if robots is None:
            meta_robot["alert"] =  "danger"
            meta_robot["alert_msg"]  = f"Robbot File is Missing"
        else:
            meta_robot["alert"] =  "success"
            meta_robot["alert_msg"]  =f"Congratulations! Your web page contains Robbot.txt File"
            meta_robot["data"] = robots
            context['rob_mess'] =f"Congratulations! Your web page contains Robbot.txt File"

        context["meta_robot"]=meta_robot


        meta_graph={"alert":"","data": ""}
        graph=page.get_metadata("open-graph")
        if graph is None:
            meta_graph["alert"] =  "danger"
            meta_graph["alert_msg"]  = f"Open graph is Missing"
        else:
            meta_graph["alert"] =  "success"
            meta_graph["alert_msg"]  =f"Congratulations! Your web page contains Open graph"
            meta_graph["data"] = graph

        context["meta_graph"] = meta_graph



    return render(request,"NewMeta.html",{"context":context,"url":url})