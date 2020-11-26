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

    '''
    Here i use sql Group by in django annotes to filter out same polling unit and sum them
    '''

    duplicates = Polling_unit.objects.values('polling_unit_name').annotate(name_count = Count('polling_unit_name')).filter(name_count__gt=1)

    records = Polling_unit.objects.filter(polling_unit_name__in=[item['polling_unit_name'] for item in duplicates])
    pdp = ([item.pdp for item in records])
    total_pdp = sum(i for i in pdp)
    dpp = ([item.dpp for item in records])
    total_dpp = sum(i for i in dpp)
    acn = ([item.acn for item in records])
    total_acn = sum(i for i in acn)
    cdc = ([item.cdc for item in records])
    total_cdc = sum(i for i in cdc)
    anpp = ([item.anpp for item in records])
    total_anpp = sum(i for i in anpp)
    labour = ([item.labour for item in records])
    total_labour = sum(i for i in labour)
    cpp = ([item.cpp for item in records])
    total_cpp = sum(i for i in cpp)
    jp = ([item.jp for item in records])
    total_jp = sum(i for i in jp)
    result = ([item.polling_unit_name for item in records])
   


    polling_units_lga = polling_units.all()
    print(polling_units_lga)
    
    states = State.objects.all()
    print(states)

    wards = Ward.objects.all()
    print(wards)

    lgas = Lga.objects.all()
    print(lgas)

    # polling_unit_name = request.GET.get('polling_unit_name')
    # new_lga = Polling_unit.objects.filter(polling_unit_name=polling_unit_name).all()
    # print(new_lga)
    new_poll = Polling_unit.objects.all()

    if request.GET.get('polling_unit_name'):
        new_poll = Lga.filter_by_poll(request.GET.get('polling_unit_name'))
        print(new_poll)

    else:
        new_poll = Polling_unit.objects.all()

    # LOCAL GOVERNMENT QUERIES

    new_lga = Lga.objects.all()

    if request.GET.get('lga_name'):
        new_lga = Lga.filter_by_lga(request.GET.get('lga_name'))
        print(new_lga)

    else:
        new_lga = Lga.objects.all()

    
    return render(request, 'home.html', {"p_units": polling_units, "states": states, "wards": wards, "lgas": lgas, 
    "polling_units_lga": polling_units_lga, "new_lga": new_lga,"new_poll": new_poll,"total_pdp":total_pdp, "total_dpp":total_dpp ,
    "total_acn":total_acn, "total_jp":total_jp, "total_cdc":total_cdc, "total_anpp":total_anpp, "total_labour":total_labour,"total_cpp":total_cpp, "records":records,"result":result })




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


def lga_filter(request,lga_name):
    lgas = Lga.filter_by_lga(lga_name)
    print(lgas)
    title = 'local gov'
    breadcrumb = "local gov"

    context = {
        "lgas":lgas ,
        "title":title , 
        "breadcrumb": breadcrumb,
    }
    return render(request,'lga_gov.html', context )



def polls(request,polling_units_name):
    poll = Polling_unit.filter_by_poll(polling_units_name)
    print(poll)
    title = 'local gov'
    breadcrumb = "local gov"

    context = {
        "poll":poll ,
        "title":title , 
        "breadcrumb": breadcrumb,
    }
    return render(request,'lga_gov.html', context )





