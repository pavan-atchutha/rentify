from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, HouseForm, HouseFilterForm, CommentForm
from .models import House, Like, Comment,User
from django.contrib.auth import logout


def home(request):
    return redirect('house_list')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('house_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('house_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def house_list(request):
    form = HouseFilterForm(request.GET)
    houses = House.objects.all()

    if form.is_valid():
        if form.cleaned_data['name']:
            houses = houses.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['city']:
            houses = houses.filter(city__icontains=form.cleaned_data['city'])
        if form.cleaned_data['state']:
            houses = houses.filter(state__icontains=form.cleaned_data['state'])
        if form.cleaned_data['min_price']:
            houses = houses.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price']:
            houses = houses.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data['min_bedrooms']:
            houses = houses.filter(number_of_bedrooms__gte=form.cleaned_data['min_bedrooms'])
        if form.cleaned_data['max_bedrooms']:
            houses = houses.filter(number_of_bedrooms__lte=form.cleaned_data['max_bedrooms'])

    return render(request, 'house_list.html', {'form': form, 'houses': houses})

@login_required
def house_create(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.save()
            return redirect('house_list')
    else:
        form = HouseForm()
    return render(request, 'house_form.html', {'form': form})

@login_required
def house_detail(request, house_id):
    house = House.objects.get(house_id=house_id)
    comments = Comment.objects.filter(house=house)
    is_liked = Like.objects.filter(user=request.user, house=house).exists()

    if request.method == 'POST':
        if 'like' in request.POST:
            if is_liked:
                Like.objects.filter(user=request.user, house=house).delete()
            else:
                Like.objects.create(user=request.user, house=house)
            return redirect('house_detail', house_id=house_id)
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.house = house
            comment.save()
            return redirect('house_detail', house_id=house_id)
    else:
        form = CommentForm()
    # if len(comments)==0:
    #     comments={}#, 'comments': comments, 'form': form, 'is_liked': is_liked
    # if len(is_liked)==0:
    #     is_liked={}
    print(house.mobile)
    return render(request, 'house_detail.html', {'house': house, 'comments': comments, 'form': form, 'is_liked': is_liked})

@login_required
def buy_houses(request):
    houses = House.objects.all()
    return render(request, 'buy_houses.html', {'houses': houses})
@login_required
def buy_house1(request, house_id):
    house = House.objects.get(pk=house_id)
    return render(request, 'buy_houses.html', {'houses': [house]})
@login_required
def sell_house1(request, house_id):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.save()
            return redirect('buy_houses')
    house = House.objects.get(pk=house_id)
    form = HouseForm(instance=house)
    return render(request, 'sell_house.html', {'houses': [house],'form':form})

@login_required
def myhousetosell(request):
    house = House.objects.all()
    h=[]
    for i in house:
        if request.user==i.owner:
            h.append(i)
    return render(request, 'sell_houses.html', {'houses': h})


@login_required
def sell_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.save()
            return redirect('buy_houses')
    else:
        form = HouseForm()
    return render(request, 'sell_house.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('house_list') 
