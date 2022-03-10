from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginUserForm, NewPostForm, UpdatePostForm, AdminProfileForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import User

# Create home page.
def home_page(request):
    posts = Post.objects.all()
    return render(request, 'user/home.html',{'posts':posts})

# Create sign up page.
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Thank you. Now, you can log in the website.')
            fm.save()
    else:
        fm =SignUpForm()
    return render(request,'user/sign_up.html',{'form':fm})

# Create login page.
def login_page(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginUserForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user =authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged successfully.')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=LoginUserForm()
        return render(request,'user/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

# Create profile page.
def dashboard_page(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name =user.get_full_name()
        return render(request,'user/dashboard.html',{'posts':posts,'full_name':full_name,})
    else:
        return HttpResponseRedirect('/login/')

# Create a new post.
def create_post(request):
  if request.user.is_authenticated:
    if request.method=='POST':
      fm = NewPostForm(request.POST or None)
      if fm.is_valid():
        usr =request.user
        t =fm.cleaned_data['text']
        cr =fm.cleaned_data['created_at']
        pst =Post(user=usr,text=t,created_at=cr)
        pst.save()
        fm = NewPostForm()
        messages.success(request,'Now, your post created.')
    else:
      fm = NewPostForm()
    uname =request.user.username
    print(uname)
    return render(request,'user/add_post.html',{'form':fm,'username':uname})
  else:
    return HttpResponseRedirect('/login/')

# update post.
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi =Post.objects.get(pk=id)
            fm = UpdatePostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Now, Your post updated.')
        else:
            pi =Post.objects.get(pk=id)
            fm = UpdatePostForm(instance=pi)
        return render(request,'user/update.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# Create logout page.
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Profile Page for user and Admin
def profile_page(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser==True:
                fm =AdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
                posts =Post.objects.all()
        else:
            fm =UserProfileForm(request.POST,instance=request.user)
        if fm.is_valid():
            messages.success(request,'profile updated...!!')
            fm.save()
        else:
            if request.user.is_superuser==True:
                fm =AdminProfileForm(instance=request.user)
                users = User.objects.all()
                posts =Post.objects.all()
                pst = 0
                for p in posts:
                    pst =pst+1
            else:
                fm = UserProfileForm(instance=request.user)
                users = None
                pst = None
            return render(request,'user/profile.html',{'form':fm,'users':users,'post':pst})
    else:
        return HttpResponseRedirect('/login/')
