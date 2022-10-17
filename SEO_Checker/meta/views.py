from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from re import template
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

        meta_title=page.get_metadata('title')
        if meta_title is None:
            context["meta_title_msg"] = "Title Not Found"

        elif len(meta_title) >= 60:

            context["meta_title_msg"] =f"Title should be Greater than 60 characters {len(meta_title)} characters"

        else:

            context["meta_title_msg"] = f"title is smaller than 60 characters {len(meta_title)} characters"

        context["meta_title"] = meta_title
        print()
        print()


        meta_desc=page.get_metadata("description")
        if meta_desc is None:
            context["meta_desc_msg"] = "Description not Found"

        elif len(meta_desc) >= 60:

            context["meta_desc_msg"] =f"Description should be Greater than 60 characters {len(meta_desc)}  characters"
        else:

            context["meta_desc_msg"] =f"Description is smaller than 60 characters {len(meta_desc)}characters"
        print(meta_desc)
        context["meta_desc"] = meta_desc
        print()
        print()


        meta_key=page.get_metadata("keywords")
        if meta_key is None:
            context["meta_key_msg"] = "No keywords found"
            # print("No Keywords")
        elif len(meta_key) >= 60:

            context["meta_key_msg"] = f"Keywords should be Greater than 60 characters {len(meta_key)}  characters"
        else:

            context["meta_key_msg"] =  f"Keywords is smaller than 60 characters {len(meta_key)}characters"

        context["meta_key"] = meta_key
        print()
        print()


        meta_view=page.get_metadata("viewport")
        if meta_view is None:
            context["meta_view_msg"] ="No Viewport"
            # print("No Keywords")
        # elif len(meta_view) >= 60:

        #     context["meta_view_msg"] =f"Viewport should be Greater than 60 characters {len(meta_view)}  characters"
        else:

            context["meta_view_msg"] =f"Viewport is used"
        print(meta_view)
        context["meta_view"] = meta_view
        print()
        print()


        meta_rob=page.get_metadata("robots")
        if meta_rob is None:
            context["meta_robots_msg"] ="No Robot.txt file is used"
            # print("No Keywords")

        else:

            context["meta_robots_msg"] =f"Robot.txt file is available"
        print(meta_rob)
        context["meta_rob"] = ""
        print()
        print()


        meta_graph=page.get_metadata("open-graph")
        if meta_graph is None:
            context["meta_graph_msg"] ="Open Graph is used"

        else:

            context["meta_graph_msg"] = f"Open graph is not uses "



        context["meta_graph"] = ""



    return render(request,"NewMeta.html",{"context":context,"url":url})