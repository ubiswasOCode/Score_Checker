from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
import metadata_parser 
# Create your views here.
def Meta(request):

    url= request.GET.get('url', None)
    context = dict()
    if url:
        

        page=metadata_parser.MetadataParser(url)

        meta_title=page.get_metadata('title')
        if meta_title is None:
            context["meta_title_msg"] = "No Desc" 
            
        elif len(meta_title) >= 60:
            print(f"Title should be Greater than 60 characters {len(meta_title)} characters")
            context["meta_title_msg"] =f"Title should be Greater than 60 characters {len(meta_title)} characters"
        
        else:
            print(f"title is smaller than 60 characters {len(meta_title)} characters")
            context["meta_title_msg"] = f"title is smaller than 60 characters {len(meta_title)} characters"
        print(meta_title)
        context["meta_title"] = meta_title
        print()
        print()
        

        meta_desc=page.get_metadata("description")
        if meta_desc is None:
            context["meta_desc_msg"] = "No Desc" 
        
        elif len(meta_desc) >= 60:
            print(f"Description should be Greater than 60 characters {len(meta_desc)}  characters")
            context["meta_desc_msg"] =f"Description should be Greater than 60 characters {len(meta_desc)}  characters"
        else:
            print(f"Description is smaller than 60 characters {len(meta_desc)}characters")
            context["meta_desc_msg"] =f"Description is smaller than 60 characters {len(meta_desc)}characters"
        print(meta_desc)
        context["meta_desc"] = meta_desc
        print()
        print()


        meta_key=page.get_metadata("keywords")
        if meta_key is None:
            context["meta_key_msg"] = "No Keywords" 
            # print("No Keywords")
        elif len(meta_key) >= 60:
            print(f"Keywords should be Greater than 60 characters {len(meta_key)}  characters")
            context["meta_key_msg"] = f"Keywords should be Greater than 60 characters {len(meta_key)}  characters"
        else:
            print(f"Keywords is smaller than 60 characters {len(meta_key)}characters")
            context["meta_key_msg"] =  f"Keywords is smaller than 60 characters {len(meta_key)}characters"
        print(meta_key)
        context["meta_key"] = meta_key
        print()
        print()


        meta_view=page.get_metadata("viewport")
        if meta_view is None:
            context["meta_view_msg"] ="No Viewport" 
            # print("No Keywords")
        elif len(meta_view) >= 60:
            print(f"Viewport should be Greater than 60 characters {len(meta_view)}  characters")
            context["meta_view_msg"] =f"Viewport should be Greater than 60 characters {len(meta_view)}  characters"
        else:
            print(f"Viewport is smaller than 60 characters {len(meta_view)}characters")
            context["meta_view_msg"] =f"Viewport is smaller than 60 characters {len(meta_view)}characters"
        print(meta_view)
        context["meta_view"] = meta_view
        print()
        print()
        

        meta_rob=page.get_metadata("robots")
        if meta_rob is None:
            context["meta_robots_msg"] ="No Robot used" 
            # print("No Keywords")
        elif len(meta_rob) >= 60:
            print(f"Robots should be Greater than 60 characters {len(meta_rob)}  characters")
            context["meta_robots_msg"] =f"Robots should be Greater than 60 characters {len(meta_rob)}  characters"
        else:
            print(f"Robots is smaller than 60 characters {len(meta_rob)}characters")
            context["meta_robots_msg"] =f"Robots should be Greater than 60 characters {len(meta_rob)}  characters"
        print(meta_rob)
        context["meta_rob"] = ""
        print()
        print()


        meta_graph=page.get_metadata("open-graph")
        if meta_graph is None:
            context["meta_graph_msg"] ="Open Graph is used" 
            print("Open Graph is used")
        elif len(meta_graph) >= 60:
            print(f"Open Graph should be Greater than 60 characters {len(meta_graph)}  characters")
            context["meta_graph_msg"] =f"Open Graph should be Greater than 60 characters {len(meta_graph)}  characters"
        else:
            print(f"Open Graph  is smaller than 60 characters {len(meta_graph)}characters")
            context["meta_graph_msg"] = f"Open Graph  is smaller than 60 characters {len(meta_graph)}characters"
            


        context["meta_graph"] = ""


   
    return render(request,"metad.html",context)