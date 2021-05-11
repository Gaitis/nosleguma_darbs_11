from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ('<h4> deposits</h4>')
    #return render (request,'main/index.html') - nestrādā.

def deposit_id (request):
    return HttpResponse ('<h4> deposit_id</h4>')

def deposit_new (request):
    return HttpResponse ('<h4> deposit_new</h4>')




def >>> # saliek visas klases un funcijas

deposit= float(input('Input deposit:'))
term= int(input('Term:'))
interest=float(input('Input interest:'))
interest_in_period=0
sum=0

for i in range(1,term+1):
    interest_in_period=deposit*interest
    deposit=deposit+interest_in_period
    sum=sum+interest_in_period
print('Interest:',sum)
