from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Business , Investors , Promoters , Business
from django.contrib.auth.models import User,auth
from .forms import CustomerForm

def index(request):
    buss = Business.objects.all()
    return render(request,'index.html',{'nameofuser': 'Shubham','buss': buss})
def investor(request):
    return render(request,'investor.html')
def promoter(request):
     return render(request,'promoter.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            print("username taken")

        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('/')

    else :
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            message.info(request,'invalid credentials')
            return redirect('login')


    else:

        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


def bussquery(request):
   
    print("in bussquery")
    
    owner = request.GET.get('owner')
    users = User.objects.all()
    ownerobj = User.objects.get(first_name = owner)
    owneremail = ownerobj.email 
    print(owneremail)
    
    name = request.GET.get('name')
    location = request.GET.get('location')
    description = request.GET.get('description')
    shortdescription = description[:20]
    img_one = request.GET.get('img_one')
    img_two = request.GET.get('img_two')
    img_three = request.GET.get('img_three')
    print(img_one,img_two,img_three)
    
    id = request.GET.get('id')
    opencount = request.GET.get('opencount')
    queryobj = Business.objects.get(id=id)
    


    
    
    #for bus in Business.objects.all():
        
    if (Business.objects.filter(id = id)):
        
        queryobj = Business.objects.get(id=id)
        busin = Business( id = id,name = name,loction = location,description = description ,shortdescription = shortdescription, img_one = img_one, img_two = img_two, img_three = img_three, owner = owner,opencount = queryobj.opencount + 1,likes = queryobj.likes)
        busin.save()
        #make a pge to display the enlarged idea of bussiness
    return render(request,'bussquery.html',{'queryobj' : queryobj,'email' : owneremail })

def like(request):
    id = request.GET.get('id')
    
    likeobj = Business.objects.get(id = id)
    busin = Business( id = id,name = likeobj.name,loction = likeobj.loction,description = likeobj.description ,shortdescription = likeobj.shortdescription,  img_one = likeobj.img_one, img_two = likeobj.img_two, img_three = likeobj.img_three,owner = likeobj.owner,opencount = likeobj.opencount,likes = likeobj.likes + 1)
    busin.save()
    queryobj = likeobj
    return render(request,'bussquery.html',{'queryobj' : queryobj})

def search(request):
    searchresult = []
    searchkey = request.GET.get('searchkey')
    listofallbussiness = Business.objects.all()
    for liss in listofallbussiness:
        print(liss.name)
        if searchkey.lower() in liss.name.lower():
            searchresult.append(liss)
    return render(request,'searchresult.html',{'nameofuser': 'Shubham','searchresult': searchresult})
def poststartup(request):
    user = request.user
    form = CustomerForm(instance = user)
    context = {'form': form}
    print("posst startup is called")
    
    
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        name = request.POST['name']
        owner = request.POST['owner']
        
        ownerid = request.user.id
        obj = Business.objects.get(id = ownerid)
        

        description = request.POST['description']
        shortdescription = description[0:20]
        loction = request.POST['loction']
        img_one = request.FILES.get('img_one')
        img_two = request.FILES.get('img_two')
        img_three = request.FILES.get('img_three')
        address = request.POST['address']
        
        busin = Business(name = name,loction = loction,description = description ,shortdescription = shortdescription, img_one = img_one, img_two = img_two, img_three = img_three,address = address,owner = owner,opencount = 0,likes = 0, startup = True )
        busin.save()
        return redirect('/')

        pass
    else:
        return render(request,'poststartup.html')
        






def postbus(request):

    user = request.user
    if str(user) == "AnonymousUser":
        print("nahi chalega")
        return render(request,'login.html')
    print(type(user),str(user))
    form = CustomerForm(instance = user)
    context = {'form': form}
    
    
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        name = request.POST['name']
        owner = request.POST['owner']
        
        
        ownerid = request.user.id
        obj = Business.objects.get(id = ownerid)
        startup = obj.startup

        description = request.POST['description']
        shortdescription = description[:20]
        loction = request.POST['loction']
        img_one = request.FILES.get('img_one')
        img_two = request.FILES.get('img_two')
        img_three = request.FILES.get('img_three')
        address = request.POST['address']
        
        
        busin = Business(name = name,loction = loction,description = description , img_one = img_one, img_two = img_two, img_three = img_three,address = address,owner = owner,opencount = 0,likes = 0, startup = startup )
        busin.save()
        return redirect('/')

        pass
    else:
        return render(request,'postbus.html')
        





    
def myads(request):
    
    myadslist = []
    print(request.user.first_name)
    allbuss = Business.objects.all()
    for x in allbuss:
        if str(request.user.first_name == x.owner):
            print(x.owner,"of",x.name)
            myadslist.append(x)
    


    return render(request,'myads.html',{'buss': myadslist})

def startup(request):

    user = request.user
    if str(user) == "AnonymousUser":
        print("nahi chalega")
        return render(request,'login.html')
    
    form = CustomerForm(instance = user)
    context = {'form': form}
    
    
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        name = request.POST['name']
        owner = request.POST['owner']
        print(owner)
        print(request.FILES)
        ownerid = request.user.id
        
        obj = Business.objects.get(id = ownerid)
        
        startup = obj.startup
        description = request.POST['description']
        shortdescription = description[:20]
        loction = request.POST['loction']
        img_one = request.FILES.get('img_one')
        img_two = request.FILES.get('img_two')
        img_three = request.FILES.get('img_three')
        address = request.POST['address']
        print(img_three,"is third image")
        print(img_two,"is two")
        
        busin = Business(name = name,loction = loction,description = description ,shortdescription = shortdescription,  img_one = img_one, img_two = img_two, img_three = img_three,address = address,owner = owner,opencount = 0,likes = 0)
        busin.save()
        return redirect('/')

        pass
    else:
        startuplist = []
        listofallbussiness = Business.objects.all()
        print(len(listofallbussiness))
        for liss in listofallbussiness:
            print(liss.name)
            print(liss.startup)
            if liss.startup == True :
                startuplist.append(liss)
        return render(request,'startup.html',{'startuplist': startuplist})

        
        





