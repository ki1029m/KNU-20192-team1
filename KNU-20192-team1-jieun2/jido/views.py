from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.
def jido(request):
    
    return render(request, 'html/jido.html', {'kaldiLat': '35.885895', 'kaldiLng':'128.610023', 'keanuLat':'35.886009', 'keanuLng':'128.610123'})