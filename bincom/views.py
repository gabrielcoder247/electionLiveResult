from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from bincom.models import Polling_unit, State, Ward, Lga
# from .forms import NewImageForm,ListingForm,BookingForm,SignUpForm,TimeForm

# Create your views here.




def index(request):

    '''
    View home function that returns the home page
    '''
  
    polling_unit = Polling_unit.objects.all()
    print(polling_unit)


    state = State.objects.all()
    print(state)

    ward = Ward.objects.all()
    print(ward)

    lga = Lga.objects.all()
    print(lga)


    # apartments = Listing.objects.filter(category__contains="apartments").all()
    # print(apartments)

    # mansionattes = Listing.objects.filter(category__contains="mansionattes").all()
    # print(mansionattes)

    # bungalows = Listing.objects.filter(category__contains="bungalows").all()
    # print(bungalows)
    

    
    return render(request, 'home.html', {"p_unit": polling_unit, "state": state,})


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})