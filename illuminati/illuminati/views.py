from django.shortcuts import render, redirect
from .models import Profile, Messages
from .forms import MsgForm

# Create your views here.
def dashboard(request):
    if request.method == "POST":
        form = MsgForm(request.POST or None)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = request.user
            msg.save()
            return redirect('illuminati:dashboard')
    
    followed_messages = Messages.objects.filter(
        user__profile__in = request.user.profile.follows.all()
    ).order_by("-created_at")

    form = MsgForm()
    return render(request, 'illuminati/dashboard.html', {"form": form, "messages": followed_messages})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'illuminati/profile_list.html', {'profiles': profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "illuminati/profile.html", {'profile': profile})

