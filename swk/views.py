from django.shortcuts import render,redirect
from django.template import loader
from .forms import TracksheetForm, DutyEntryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.form

def user_login(request):
    # context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to index page.
                    # messages.info(request,"login sucessfully")
                    return render(request,"HomePage.html")
                else:
                    # Return a 'disabled account' error message
                    messages.info(request,"You're account is disabled")
                    return HttpResponseRedirect("You're account is disabled.")
        else:
                # Return an 'invalid login' error message.
                print ("invalid login details for " + username)
                # messages.info(request,"Invalid login details"+ username )
                messages.error(request, "Invalid username or password.")
                return render(request,'adminlogin.html')
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'adminlogin.html')

def formLayout(request):
    return render(request,"formlayout.html")

def HomePage(request):
        return render(request,"HomePage.html")

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,"HomePage.html")

def DutyEntryPage(request):
    if request.method == "POST":
            
        # num_houses = request.POST.get("")
        form = DutyEntryForm(request.POST or None)       
        if form.is_valid():

            form.save()
        
            messages.success(request, 'Your form is  saved') 
        return render(request,'HomePage.html')
    else:
        form = DutyEntryForm(request.POST or None)
        context= {
            'form': form,
            'test': 'test',
        }

    return render(request,'DutyEntryForm.html',context)


def TracksheetPage(request):
    if request.method == "POST":

                   
        form = TracksheetForm(request.POST or None)
        print(form)
        
        if form.is_valid():

            form.save()
        
            messages.success(request, 'Your form is  saved') 
        return render(request,'HomePage.html')
    else:
        selected_region = request.POST.get("lane_name")
        dutyentry = DutyEntry.filter(lane_name=selected_region)
        num_houses = dutyentry.num_houses_lane

        form = TracksheetForm(request.POST or None)
        context= {
            'form': form,
            'num_houses':num_houses,
            'test': 'test',
        }

    return render(request,'TracksheetForm.html',context)


def MapPage(request):
    return render(request,"map_fromFGIS.html")

# def TracksheetPage(request):
#     form = TracksheetForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context= {
#         'form': form,
#         'test': 'test',
#     }

#     return render(request,'TracksheetForm.html',context)

def AboutUs(request):
    return render(request,"aboutus.html")

        