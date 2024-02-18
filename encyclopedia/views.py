from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": util.get_entry(title)
        })

def search(request):
    query = request.GET.get('q')
    filtered_byquery = list(filter(lambda entry: query in entry, util.list_entries()))
    if len(filtered_byquery) > 0:
        return render(request, 'encyclopedia/search.html', {
            "query": query,
            "entries": filtered_byquery
        })
    else:
        return render(request, "encyclopedia/error.html", {
        "query": query
    })