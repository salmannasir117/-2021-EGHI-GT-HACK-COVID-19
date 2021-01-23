from django.shortcuts import render

# Create your views here.
def test_static(request):
     _file = open('static/tracker/wrapper.html').read()
     return render(request, 'tracker/test_static.html', {"HtmlFile": _file})
