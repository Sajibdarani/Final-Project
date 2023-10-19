from django.shortcuts import render

blog_post = [
    {
        'tittle': " sdfdkjlsj",
        'content': " jdhshfsfh",
        'author': "sajib",
        'post_create_date':"45566",

    },
    {
        'tittle': " sdfdkjlsj",
        'content': " jdhshfsfh",
        'author': "sajib",
        'post_create_date': "45566",

    }
]
def homepage(request):
    return render(request, 'home/homepage.html', {"blog_post": blog_post})
def about(request):
    return render(request, 'home/about.html', {"tittle":"about page"})
