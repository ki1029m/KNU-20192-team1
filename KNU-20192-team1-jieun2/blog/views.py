from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from market.models import Market, Like
# Create your views here.
def home(request):
    user=request.user

    if user.is_active:
        liked=Like.objects.select_related()
        if user.profile.market_id == -1:
            return render(request, 'html/home.html', {'user':user, 'like':liked})
        else:
            market=get_object_or_404(Market, pk=user.profile.market_id)
            return render(request, 'html/home.html', {'user':user, 'market': market, 'like':liked})
    else:
        return render(request, 'html/home.html', {'user':user})