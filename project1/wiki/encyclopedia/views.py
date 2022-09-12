from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "get_entry": util.get_entry()
    })

def create(request):
    return render(request, "encyclopedia/create.html")