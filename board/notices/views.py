from django.shortcuts import render

# Create your views here.

def _index(req):
    content = {

    }
    return render(req, 'index.html', context=content)
def _write(req):
    content = {

    }
    return render(req, 'write.html', context=content)

def _list(req):
    content = {

    }
    return render(req, 'list.html', context=content)
def _introduce(req):
    content = {

    }
    return render(req, 'introduce.html', context=content)