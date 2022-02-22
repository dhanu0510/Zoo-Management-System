from django.db import models

# Create your models here.

class Animal(models.Model):
    AnimalName = models.CharField(max_length=200, null=True)
    CageNumber = models.CharField(max_length=15, null=True)
    FeedNumber = models.CharField(max_length=150, null=True)
    Breed = models.CharField(max_length=200, null=True)
    AnimalImage = models.FileField(max_length=200, null=True)
    Description = models.CharField(max_length=300, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.AnimalName

class Ticforeigner(models.Model):
    TicketID = models.CharField(max_length=100, null=True)
    NoAdult = models.CharField(max_length=50, null=True)
    NoChildren = models.CharField(max_length=50, null=True)
    AdultUnitprice = models.CharField(max_length=100, null=True)
    ChildUnitprice = models.CharField(max_length=100, null=True)
    PostingDate = models.DateTimeField(null=True)

    def __str__(self):
        return self.TicketID

class Ticindian(models.Model):
    TicketID = models.CharField(max_length=100, null=True)
    NoAdult = models.CharField(max_length=50, null=True)
    NoChildren = models.CharField(max_length=50, null=True)
    AdultUnitprice = models.CharField(max_length=100, null=True)
    ChildUnitprice = models.CharField(max_length=100, null=True)
    PostingDate = models.DateTimeField(null=True)

    def __str__(self):
        return self.TicketID

class Tickettype(models.Model):
    TicketType = models.CharField(max_length=200, null=True)
    Price = models.CharField(max_length=150, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TicketType

class Contact(models.Model):
    fullname = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=15,null=True)
    emailid = models.CharField(max_length=100,null=True)
    message = models.CharField(max_length=300,null=True)
    isread = models.CharField(max_length=10)
    mdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

