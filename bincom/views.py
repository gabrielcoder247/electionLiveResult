from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from bincom.models import Polling_unit, State, Ward, Lga
from django.db.models import Sum
from django.db.models import Count


from .forms import PollingUnitForm, SignUpForm, LgaForm, WardForm, StateForm


# Create your views here.




def index(request):

    '''
    View home function that returns the home page
    '''
  
    polling_units = Polling_unit.objects.all()

    # duplicates = Polling_unit.objects.values('polling_unit_name').annotate(name_count = Count('polling_unit_name')).filter(name_count__gt=1)

    # records = Polling_unit.objects.filter(polling_unit_name__in=[item['polling_unit_name'] for item in duplicates])
    # result = ([item.party_score for item in records])
    # total = sum(i for i in result)

    # return  total





    states = State.objects.all()
    print(states)

    wards = Ward.objects.all()
    print(wards)

    lgas = Lga.objects.all()
    print(lgas)


    # apartments = Listing.objects.filter(category__contains="apartments").all()
    # print(apartments)

    # mansionattes = Listing.objects.filter(category__contains="mansionattes").all()
    # print(mansionattes)

    # bungalows = Listing.objects.filter(category__contains="bungalows").all()
    # print(bungalows)
    

    
    return render(request, 'home.html', {"p_units": polling_units, "states": states, "wards": wards, "lgas": lgas})


# def total_vote(id):
#        if id == self.id:
#            vote_sum = Polling_unit.objects.aggregate(Sum('party_score'))
#            return vote_sum 


# def GetDoggysWithSameName(self):
#     return Doggy.objects.filter(color=self.name)


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





@login_required(login_url='/accounts/login/')
def p_unit(request):

    '''
    View listing function that returns the listing page and data
    '''
    # form = ListingForm()
    current_user = request.user
    if request.method == 'POST':
        form = PollingUnitForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            poll = form.save(commit=False)
            poll.user = current_user
            poll.save()
        return redirect('index_page') 
    else: 

        form = PollingUnitForm() 

    return render(request, 'pollUnit_form.html', {"form": form})



@login_required(login_url='/accounts/login/')
def lga(request):



    '''
    View listing function that returns the listing page and data
    '''
    # form = ListingForm()
    current_user = request.user
    if request.method == 'POST':
        form = LgaForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            poll = form.save(commit=False)
            poll.user = current_user
            poll.save()
        return redirect('index_page') 
    else: 

        form = LgaForm() 

    return render(request, 'lga_form.html', {"form": form})


@login_required(login_url='/accounts/login/')
def ward(request):



    '''
    View listing function that returns the listing page and data
    '''
    # form = ListingForm()
    current_user = request.user
    if request.method == 'POST':
        form = WardForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            poll = form.save(commit=False)
            poll.user = current_user
            poll.save()
        return redirect('index_page') 
    else: 

        form = WardForm() 

    return render(request, 'ward_form.html', {"form": form})




@login_required(login_url='/accounts/login/')
def state(request):

    '''
    View listing function that returns the listing page and data
    '''
    
    # form = ListingForm()
    current_user = request.user
    if request.method == 'POST':
        form = StateForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            poll = form.save(commit=False)
            poll.user = current_user
            poll.save()
        return redirect('index_page') 
    else: 

        form = StateForm() 

    return render(request, 'state_form.html', {"form": form})




