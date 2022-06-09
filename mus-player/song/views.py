from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Song

@login_required
def index(request, pk=None):
  context = {}
  songs = Song.objects.all()
  song = Song.objects.get(id=pk)
  
  context['songs'] = songs
  context['song'] = song

  return render(request, 'song/index.html', context)
