import random

from django.contrib.auth.models import User
from django.db.models import Q, Sum
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from datetime import datetime, timedelta, time
from datetime import date


# Create your views here.

def index(request):
    animal = Animal.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    today = datetime.now().date()
    yesterday = today - timedelta(1)

    todaytotaladult = Ticindian.objects.filter(PostingDate=today).aggregate(Sum('NoAdult'))
    todaytotalchild = Ticindian.objects.filter(PostingDate=today).aggregate(Sum('NoChildren'))
    yesterdaytotaladult = Ticindian.objects.filter(PostingDate=yesterday).aggregate(Sum('NoAdult'))
    yesterdaytotalchild = Ticindian.objects.filter(PostingDate=yesterday).aggregate(Sum('NoChildren'))

    todaytotalforadult = Ticforeigner.objects.filter(PostingDate=today).aggregate(Sum('NoAdult'))
    todaytotalforchild = Ticforeigner.objects.filter(PostingDate=today).aggregate(Sum('NoChildren'))
    yesterdaytotalforadult = Ticforeigner.objects.filter(PostingDate=yesterday).aggregate(Sum('NoAdult'))
    yesterdaytotalforchild = Ticforeigner.objects.filter(PostingDate=yesterday).aggregate(Sum('NoChildren'))

    return render(request, 'admin_home.html', locals())

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def add_Ticket_Type(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        ttype = request.POST['TicketType']
        cost = request.POST['Price']

        try:
            Tickettype.objects.create(TicketType=ttype, Price=cost)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_Ticket_Type.html', locals())


def manage_Ticket_Type(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticket = Tickettype.objects.all()
    return render(request, 'manage_Ticket_Type.html', locals())


def edit_TicketType(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    tickets = Tickettype.objects.get(id=pid)
    if request.method == "POST":
        price = request.POST['Price']

        tickets.Price = price

        try:
            tickets.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_TicketType.html', locals())


def delete_TicketType(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticktes = Tickettype.objects.get(id=pid)
    ticktes.delete()
    return redirect('manage_Ticket_Type')


def add_Animal(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        aname = request.POST['AnimalName']
        cnumber = request.POST['CageNumber']
        fnumber = request.POST['FeedNumber']
        breed = request.POST['Breed']
        aniimg = request.FILES['AnimalImage']
        des = request.POST['Description']

        try:
            Animal.objects.create(AnimalName=aname, CageNumber=cnumber, FeedNumber=fnumber, Breed=breed,
                                  AnimalImage=aniimg, Description=des)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_Animal.html', locals())


def manage_Animal(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    animal = Animal.objects.all()
    return render(request, 'manage_Animal.html', locals())


def edit_Animal(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    animal = Animal.objects.get(id=pid)
    if request.method == "POST":
        aname = request.POST['AnimalName']
        cnumber = request.POST['CageNumber']
        fnumber = request.POST['FeedNumber']
        breed = request.POST['Breed']
        des = request.POST['Description']

        animal.AnimalName = aname
        animal.CageNumber = cnumber
        animal.FeedNumber = fnumber
        animal.Breed = breed
        animal.Description = des

        try:
            animal.save()
            error = "no"
        except:
            error = "yes"

        try:
            aniimg = request.FILES['AnimalImage']
            animal.AnimalImage = aniimg
            animal.save()
        except:
            pass
    return render(request, 'edit_Animal.html', locals())


def delete_Animal(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    animal = Animal.objects.get(id=pid)
    animal.delete()
    return redirect('manage_Animal')


def add_NormalTicket(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        tid = str(random.randint(10000000, 99999999))
        noadult = request.POST['NoAdult']
        nochild = request.POST['NoChildren']

        try:
            Ticindian.objects.create(TicketID=tid, NoAdult=noadult, NoChildren=nochild, PostingDate=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_NormalTicket.html', locals())


def manage_NormalTicket(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticketind = Ticindian.objects.all()
    return render(request, 'manage_NormalTicket.html', locals())


def view_NormalTicket(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticketind = Ticindian.objects.get(id=pid)
    nchild = Tickettype.objects.get(TicketType="Native Child")
    nadult = Tickettype.objects.get(TicketType="Native Adult")
    nchildprice = nchild.Price
    nadultprice = nadult.Price

    Adultprice = int(ticketind.NoAdult) * int(nadultprice)
    Childprice = int(ticketind.NoChildren) * int(nchildprice)
    total = int(Adultprice) + int(Childprice)

    return render(request, 'view_NormalTicket.html', locals())


def delete_NormalTicket(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticketind = Ticindian.objects.get(id=pid)
    ticketind.delete()

    return redirect('manage_NormalTicket')


def add_ForTicket(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        tid = str(random.randint(10000000, 99999999))
        noadult = request.POST['NoAdult']
        nochild = request.POST['NoChildren']

        try:
            Ticforeigner.objects.create(TicketID=tid, NoAdult=noadult, NoChildren=nochild, PostingDate=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_ForTicket.html', locals())


def manage_ForTicket(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticketforeig = Ticforeigner.objects.all()
    return render(request, 'manage_ForTicket.html', locals())


def view_ForeTicket(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticketforeig = Ticforeigner.objects.get(id=pid)
    nadult = Tickettype.objects.get(TicketType="Foreigner Adult")
    nchild = Tickettype.objects.get(TicketType="Foreigner Child")
    nchildprice = nchild.Price
    nadultprice = nadult.Price

    Adultprice = int(ticketforeig.NoAdult) * int(nadultprice)
    Childprice = int(ticketforeig.NoChildren) * int(nchildprice)
    total = int(Adultprice) + int(Childprice)

    return render(request, 'view_ForeTicket.html', locals())


def delete_ForeTicket(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ticketforeig = Ticforeigner.objects.get(id=pid)
    ticketforeig.delete()
    return redirect('manage_ForTicket')


def btnDates_normalreports(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['FromDate']
        td = request.POST['ToDate']
        ticketind = Ticindian.objects.filter(Q(PostingDate__gte=fd) & Q(PostingDate__lte=td))
        return render(request, 'indianreportbtwdates.html', locals())
    return render(request, 'btnDates_normalreports.html')


def btnDates_foregnreports(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['FromDate']
        td = request.POST['ToDate']
        ticketfore = Ticforeigner.objects.filter(Q(PostingDate__gte=fd) & Q(PostingDate__lte=td))
        return render(request, 'foreportbtwdates.html', locals())
    return render(request, 'btnDates_foregnreports.html')


def normal_Ticket_Search(request):
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
    try:
        ticketind = Ticindian.objects.filter(TicketID=sd)
    except:
        ticketind = ""
    return render(request, 'normal_Ticket_Search.html', locals())


def foreigner_Ticket_Search(request):
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
    try:
        ticketfore = Ticforeigner.objects.filter(TicketID=sd)
    except:
        ticketfore = ""
    return render(request, 'foreigner_Ticket_Search.html', locals())


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())

def contact(request):
    if request.method == 'POST':
        n = request.POST['fullname']
        cont = request.POST['contact']
        e = request.POST['emailid']
        msg = request.POST['message']
        try:
            Contact.objects.create(fullname=n, contact=cont, emailid=e, message=msg, mdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(isread="no")
    return render(request, 'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(isread="yes")
    return render(request, 'read_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request, 'view_queries.html',locals())

def delete_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.get(id=pid)
    contact.delete()
    return redirect('read_queries')


def Logout(request):
    logout(request)
    return redirect('index')
