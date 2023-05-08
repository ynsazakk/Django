from django.http.response import HttpResponse
from django.shortcuts import render

data = {
    "blogs":[
    {
        "id":1,
        "title":"Zirve Resturaunt Güzel Bir Akşam Yemeği",
        "image":"us.jpg",
        "is_active":True,
        "is_home":True,
        "description":"Pizzası kötüydü, makarnasını beğendik. Fiyatlar pahalı."
    },
    {
        "id":2,
        "title":"Ceren'le Günübirlik Antalya Gezisi",
        "image":"us1.jpg",
        "is_active":True,
        "is_home":True,
        "description":"Antalya'nın Alanya'dan güzel olduğunu anladım.!"
    },
    {
        "id":3,
        "title":"Metro Gezisi Sonrası Starbucks",
        "image":"us2.jpg",
        "is_active":True,
        "is_home":True,
        "description":"1+1 ev hayalimizden vazgeçtiğimiz gezi."
    },
    {
        "id":4,
        "title":"Dut Dibinde Güzel Bir Gece",
        "image":"us4.jpeg",
        "is_active":True,
        "is_home":True,
        "description":"Güzel bir geceydi. Rüzgar ve yağmur vardı Ceren'i evine sarıla sarıla bıraktım."
    },
    {
        "id":5,
        "title":"Çadırda Kamp Sonrası Sabah Kahvesi",
        "image":"us6.jpeg",
        "is_active":True,
        "is_home":True,
        "description":"Çadırda ilk defa birlikte kaldık. Güzel bir deneyimdi."
    }
    ]
}

# Create your views here.

def index(request):
    context ={
        "blogs":data["blogs"]
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context ={
        "blogs":data["blogs"]
    }
    return render(request,"blog/blogs.html", context)

def blog_details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None

    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog

    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0]

    return render(request,"blog/blog-details.html", {
        "blog": selectedBlog
    })