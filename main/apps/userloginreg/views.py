from django.shortcuts import render, redirect
from . import models
from django.core.urlresolvers import reverse
# Create your views here.
# home route
def index(request):

    errors=[]
    context = {}

    if 'errors' in request.session:
        errors = request.session['errors']
        context['error'] = True
        context['errors'] = errors
        context['formdata'] = request.session['formdata']
        del request.session['errors']
        del request.session['formdata']

    elif 'new' in request.session:
        context['formdata'] = request.session['formdata']
        context['new'] = True
        del request.session['new']
        del request.session['formdata']

    return render(request,'userloginreg/index.html',context)

def login(request):
    if request.method == 'POST':
        ( flag, data ) = models.User.objects.login(request.POST)
        if flag == True:
            request.session['user_id'] = data.id
            request.session['login'] = True
            return redirect('home:success')
        else:
            request.session['login'] = False
            request.session['formdata'] = {'email': request.POST['user']}
            request.session['errors'] = data
            return redirect('home:index')
    else:
        return redirect('home:index')
def logout(request):
        request.session.clear()
        return redirect('home:index')
def register(request):

    print "register():"
    if request.method == 'POST':

        if 'login' in request.session:
            del request.session['login']

        ( flag , data ) = models.User.objects.register(request.POST)

        if flag == True:
            # fill formdata with the scrubbed successful data
            formdata = {'first_name': data['first_name'],'last_name': data['last_name'],'email': data['email']}
            request.session['formdata'] = formdata
            request.session['new'] = True
        else:
            request.session['errors'] = data
            # fill formdata with the same stuff the user entered into the form
            formdata = {'first_name': request.POST['first_name'],'last_name': request.POST['last_name'],'email': request.POST['email']}
            request.session['formdata'] = formdata

        return redirect('home:index')
    else:
        return redirect('home:index')

def landingpage(request):

    if request.session['user_id']:
        context = {}
        z = models.User.objects.get(id=request.session['user_id'])
        context['user'] = { 'first_name': z.first_name, 'last_name': z.last_name, 'email': z.email }
        return render(request,'userloginreg/landingpage.html', context)
    else:
        return redirect('home:index')
