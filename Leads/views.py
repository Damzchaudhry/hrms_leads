# from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
# from .models import NewApplicants,Lead_Category,Leads,Send_To
# from .forms import LoginForm 
# from django.contrib.auth import login,authenticate,logout
# from django.contrib import messages

# def login_User(request):
#     form = LoginForm(request.POST or None)

#     context = {
#         "form":form
#     }

#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")

#         user = authenticate(username = username,password = password)

#         if user is None:
#             messages.info(request,"No match Found")
#             return render(request,"login.html",context)

#         messages.success(request,"Hello")
#         login(request,user)
#         return render(request,"index.html")
#     return render(request,"login.html",context)
