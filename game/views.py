import random
import json

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EnterName

# Create your views here.
def get_name(request):
    if request.method == "POST":
        form = EnterName(request.POST)
        if form.is_valid():
            name = form.cleaned_data['enter_name']
            with open('names.json', 'r') as fp:
                names = json.load(fp)
                names.append({
                    "name": name.title(),
                    "status": False,
                    "id": len(names)+1
                })
            with open('names.json', 'w') as fp:
                random.shuffle(names)
                for i, name in enumerate(names):
                    name['id'] = i
                json.dump(names, fp)
            return HttpResponseRedirect("/waitroom/")
    else:
        form = EnterName()
    return render(request, "index.html", {"form": form})

def game_play(request):
    with open('names.json', 'r') as fp:
        names = json.load(fp)
        # random.shuffle(names)
    return render(request, "gamePlay.html", {"names": names})

def setup(request):
    with open('names.json', 'r') as fp:
        names = json.load(fp)
    return render(request, "setup.html", {"names": names})

def wait_room(request):
    with open('names.json', 'r') as fp:
        names = json.load(fp)
    number_players = len(names)
    return render(request, "waitRoom.html", {"number_players": number_players})

def reset(request):
    with open('names.json', '+w') as fp:
        fp.write("[]")
    return HttpResponseRedirect("/setup/")

def crossout(request, id):
    with open('names.json', 'r') as fp:
        names = json.load(fp)
    names[id]["status"] = not names[id]["status"] 
    with open('names.json', 'w') as fp:
        json.dump(names, fp)
    return HttpResponseRedirect("/setup/")
    

