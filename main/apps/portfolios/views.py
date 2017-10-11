from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Portfolio
# Create your views here.
def index(request):
    print "portfolios index page"
    if not 'user_id' in request.session:
		return redirect('home:index')
    # response = "Portfolios"
    # return HttpResponse(response)
    context = { 'portfolios': Portfolio.objects.all().order_by('portfolio__title')}
    return render(request,'portfolios/index.html') # , context
def create(request):
    print "1 - trying to create..."

    if request.method == 'POST':
        print "2 - trying to create..."
        curr_user = User.get(id = int(request.session['user_id']))

        Portfolio.objects.create(title = request.POST['title'], user = curr_user)
    return redirect('home:success')

def show(request,id):
    print 'portfolios show page'
    return redirect('portfolios:index')
def delete(request):
    return redirect('portfolios:index')
