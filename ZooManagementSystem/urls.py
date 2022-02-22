"""ZooManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from zoo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('admin_home', admin_home, name='admin_home'),
    path('admin_login', admin_login, name='admin_login'),
    path('add_Animal', add_Animal, name='add_Animal'),
    path('manage_Animal', manage_Animal, name='manage_Animal'),
    path('edit_Animal/<int:pid>', edit_Animal, name='edit_Animal'),
    path('delete_Animal/<int:pid>', delete_Animal, name='delete_Animal'),
    path('manage_Ticket_Type', manage_Ticket_Type, name='manage_Ticket_Type'),
    path('edit_TicketType/<int:pid>', edit_TicketType, name='edit_TicketType'),
    path('delete_TicketType/<int:pid>', delete_TicketType, name='delete_TicketType'),
    path('add_NormalTicket', add_NormalTicket, name='add_NormalTicket'),
    path('manage_NormalTicket', manage_NormalTicket, name='manage_NormalTicket'),
    path('view_NormalTicket/<int:pid>', view_NormalTicket, name='view_NormalTicket'),
    path('delete_NormalTicket/<int:pid>', delete_NormalTicket, name='delete_NormalTicket'),
    path('add_ForTicket', add_ForTicket, name='add_ForTicket'),
    path('manage_ForTicket', manage_ForTicket, name='manage_ForTicket'),
    path('view_ForeTicket/<int:pid>', view_ForeTicket, name='view_ForeTicket'),
    path('delete_ForeTicket/<int:pid>', delete_ForeTicket, name='delete_ForeTicket'),
    path('btnDates_normalreports', btnDates_normalreports, name='btnDates_normalreports'),
    path('btnDates_foregnreports', btnDates_foregnreports, name='btnDates_foregnreports'),
    path('normal_Ticket_Search', normal_Ticket_Search, name='normal_Ticket_Search'),
    path('foreigner_Ticket_Search', foreigner_Ticket_Search, name='foreigner_Ticket_Search'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout',Logout,name='logout'),
    path('read_queries',read_queries, name='read_queries'),
    path('unread_queries',unread_queries, name='unread_queries'),
    path('view_queries/<int:pid>',view_queries, name='view_queries'),
    path('delete_queries/<int:pid>', delete_queries, name='delete_queries'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
