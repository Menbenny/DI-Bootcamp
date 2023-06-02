from django.shortcuts import render
from datetime import date
# from django.http import HttpResponse 

# http response - Generally GUI - what a client sees

# Create your views here.

# def posts(request):
    
#     # posts is a view (what kind of data, where to send)
#     # Request can be seen as a object that gives details 
#     # return HttpResponse(some_text)
    
#     today = date.today()
#     # return render(request, 'posts.html', {'time': today})

#     title = 'This is Django Number One'
#     content = 'Python Framework'
#     author = 'Developers Institute'

#     # best practice 

#     subscribers = ['Yossi', 'Michael', 'Evgeni', 'Ilona']

#     context = {'time': today,
#                'title': title,
#                'content' : content,
#                'author': author,
#                'subcribers_list': subscribers}

#     return render(request, 'posts.html', context)

# url is what calls the view
    
# Add a new view called "profile", Add a new route called "profile_user"
# profile_user is the url
# Inside the view create a dictionary with the information of a specific user. One of the key should be a list
# Add a new template called "profile_user" that renders all the information about the user
# Depending on the gender of the user , welcome him with "Mr" or "Mrs". Use template inheritance to welcome the user in all of the templates you have already created

def profile(request):
    name = 'Shwang'
    age = '26'
    gender = 'female'
    context = {'name': name,
               'middle_names': ['Victor', 'Benjamin'],
               'age': age,
               'gender': gender}
    
    return render(request, 'profile_user.html', context)