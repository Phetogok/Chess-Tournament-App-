from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Player, Tournament, News, Message, AdminProfile
from .forms import TournamentForm, NewsForm, PlayerForm
import calendar
from datetime import datetime, date
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Add this view to your existing views.py
def register_view(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create admin profile automatically
            AdminProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    """Dashboard view with overview data"""
    players = Player.objects.all()[:5]  # Latest 5 players
    recent_messages = Message.objects.filter(is_read=False)[:5]
    upcoming_tournaments = Tournament.objects.filter(date__gte=datetime.now())[:3]
    latest_news = News.objects.all()[:3]
    
    context = {
        'players': players,
        'recent_messages': recent_messages,
        'upcoming_tournaments': upcoming_tournaments,
        'latest_news': latest_news,
        'total_players': Player.objects.count(),
        'total_tournaments': Tournament.objects.count(),
        'unread_messages': Message.objects.filter(is_read=False).count(),
    }
    return render(request, 'dashboard.html', context)

@login_required
def members(request):
    """Members view showing players and coaches"""
    search_query = request.GET.get('search', '')
    role_filter = request.GET.get('role', '')
    
    players = Player.objects.all()
    
    if search_query:
        players = players.filter(
            Q(name__icontains=search_query) | 
            Q(specialty__icontains=search_query)
        )
    
    if role_filter:
        players = players.filter(role=role_filter)
    
    # Separate players and coaches
    player_list = players.filter(role='player')
    coach_list = players.filter(role='coach')
    
    context = {
        'players': player_list,
        'coaches': coach_list,
        'search_query': search_query,
        'role_filter': role_filter,
    }
    return render(request, 'members.html', context)

@login_required
def tournament_list(request):
    """Tournament list and creation"""
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tournament created successfully!')
            return redirect('tournament_list')
    else:
        form = TournamentForm()
    
    tournaments = Tournament.objects.all()
    paginator = Paginator(tournaments, 10)
    page_number = request.GET.get('page')
    tournaments = paginator.get_page(page_number)
    
    context = {
        'tournaments': tournaments,
        'form': form,
    }
    return render(request, 'tournament_list.html', context)

@login_required
def tournament_detail(request, pk):
    """Tournament detail view"""
    tournament = get_object_or_404(Tournament, pk=pk)
    context = {'tournament': tournament}
    return render(request, 'tournament_detail.html', context)

@login_required
def news_room(request):
    """News room view"""
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'News created successfully!')
            return redirect('news_room')
    else:
        form = NewsForm()
    
    news_list = News.objects.all()
    paginator = Paginator(news_list, 6)
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)
    
    context = {
        'news_list': news_list,
        'form': form,
    }
    return render(request, 'news.html', context)

@login_required
def calendar_view(request):
    """Calendar view with tournament highlights"""
    today = date.today()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))
    
    # Get calendar data
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    # Get tournaments for this month
    tournaments = Tournament.objects.filter(
        date__year=year,
        date__month=month
    )
    
    # Create tournament dict by day
    tournament_days = {}
    for tournament in tournaments:
        day = tournament.date.day
        if day not in tournament_days:
            tournament_days[day] = []
        tournament_days[day].append(tournament)
    
    context = {
        'calendar': cal,
        'year': year,
        'month': month,
        'month_name': month_name,
        'tournament_days': tournament_days,
        'today': today,
    }
    return render(request, 'calendar.html', context)

@login_required
def profile_view(request):
    """User profile view"""
    try:
        admin_profile = request.user.adminprofile
    except AdminProfile.DoesNotExist:
        admin_profile = AdminProfile.objects.create(user=request.user)
    
    context = {
        'admin_profile': admin_profile,
    }
    return render(request, 'profile.html', context)