from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def homepageview(request):
    return render (request,'home.html')

def aboutpageview(request):
    return render (request,'about.html')

def contactpageview(request):
    return render (request,'contact.html')

def shoppage(request):
    return render (request,'shop.html')

def saveSessionData(request):
    request.session['username'] = "Hetvi Patel"
    return HttpResponse ("Session Created")

def getSessionData(request):
   if request.session.has_key('username'):
    msg = request.session['username'] 
    return HttpResponse (msg)
   else:
       return HttpResponse ("Session Variable not Present")

def deleteSessionData(request):
    del request.session['username']
    return HttpResponse ("Session Removed")

def getSessionData2(request):
    msg = request.session['username'] 
    return HttpResponse(msg)
   
def contactprocess(request):
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = int(request.POST['txt3'])
    d = int(request.POST['txt4'])
    e = int(request.POST['txt5'])
    f = a + b + c + d + e
    g = f/5
    msg = "a Value is ",a, "B Value is ",b, "C Value is ",c, "D Value is ",d, "E Value is ",e, "Sum is ",f, "Avg is ",g,
    h=""
    if f == 500:
        h = "Grade A"
    elif f>250:
        h = "Grade B"
    else:
        h = "Grade C"
    return render(request,'ans.html',{'mya':a,'myb':b,'myc':c,'myd':d,'mye':e,'myf':f,'myg':g,'myh':h})

def loginpage(request):
    return render(request,'login.html')

def loginprocess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginpage)
    
def logout(request):
    del request.session['myemail']
    return redirect(loginpage)