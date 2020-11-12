
# Create your models here.


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class AgentDetail(models.Model):

    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=70,blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True, related_name='user_booking')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    # @classmethod  
    # def find_bookings(cls,name):
    #     bookings = Bookings.objects.filter_by_name(name__icontains=name).all()

    #     return profile

    # @classmethod   
    # def get_all_booking(cls,id):
    #     booking=Booking.objects.filter(id=id).all()

    def save_user(self):
        self.save()

    # def delete_bookings(self):
    #     self.delete()     

    def __str__(self):
        return self.firstname





class Announced_lga_result(models.Model):


    lga_name = models.CharField(max_length=50,null=True)
    party_abbreviation = models.CharField(max_length=4,null=True)
    party_score = models.IntegerField()
    # entered_by_user = models.CharField(max_length=50,null=True)
    date_entered = models.DateField(auto_now_add=True,blank=True, null=True)
    user_ip_address = models.CharField(max_length=50,null=True)
    entered_by_user = models.ForeignKey('AgentDetail', on_delete=models.CASCADE)
   
    # class meta:
    #     ordering = ['-date'] 


    # def save_timeslot(self):
    #     self.save()

    # @classmethod
    # def get_all_timeslots(cls,id):
    #     timeslots = cls.objects.filter(id=id).order_by('-date')
    #     return timeslots

    def __str__(self):
        return self.lga_name

class Announced_pu_result(models.Model):

  
    lga_name = models.CharField(max_length=50,null=True)
    party_abbreviation = models.CharField(max_length=4,null=True)
    party_score = models.IntegerField()
    # entered_by_user = models.CharField(max_length=50,null=True)
    date_entered = models.DateField(auto_now_add=True,blank=True, null=True)
    user_ip_address = models.CharField(max_length=50,null=True)
    entered_by_user = models.ForeignKey('AgentDetail', on_delete=models.CASCADE)
    polling_unit_id = models.ForeignKey('Polling_unit', on_delete=models.CASCADE, related_name='polling_unit_result')

    def __str__(self):
        return self.entered_by_user


class Announced_state_result(models.Model):

  
    state_name = models.CharField(max_length=50,null=True)
    party_abbreviation = models.CharField(max_length=4,null=True)
    party_score = models.IntegerField(11)
    # entered_by_user = models.CharField(max_length=50,null=True)
    entered_by_user = models.ForeignKey('AgentDetail', on_delete=models.CASCADE, related_name='state_result')
    date_entered = models.DateField(auto_now_add=True,blank=True, null=True)
    user_ip_address = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.state_name


class Announced_ward_result(models.Model):

  
   
    ward_name = models.CharField(max_length=50,null=True)
    party_abbreviation = models.CharField(max_length=4,null=True)
    party_score = models.IntegerField()
    entered_by_user = models.ForeignKey('AgentDetail', on_delete=models.CASCADE, related_name='ward_result')
    date_entered = models.DateField(auto_now_add=True,blank=True, null=True)
    user_ip_address = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.ward_name
   


class Lga(models.Model):

    lga_name = models.CharField(max_length=50,null=True)
    lga_description = models.TextField()
    state_id = models.ForeignKey('State', on_delete=models.CASCADE)
    entered_by_user = models.ForeignKey('AgentDetail', on_delete=models.CASCADE)
    date_entered = models.DateField(auto_now_add=True,blank=True, null=True)
    user_ip_address = models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.lga_name


class Party(models.Model):

    PDP = "PDP"
    DPP = "DPP"
    ACN = "ACN"
    PPA = "PPA"
    CDC = "CDC"
    JP = "JP"
    ANPP = "ANPP"
    LABOUR = "LABOUR"
    CPP = "CPP"

    PROPERTY_CHOICES = [
    (PDP, "PDP"),
    (DPP, "DPP"),
    (ACN, "ACN"),
    (PPA, "PPA"),
    (CDC, "CDC"),
    (JP, "JP"),
    (ANPP, "ANPP"),
    (LABOUR, "LABOUR"),
    (CPP, "CPP")
    ]

    # date = models.DateField(auto_now_add=True,blank=True, null=True)
    party_name = models.CharField(max_length=50, choices=PROPERTY_CHOICES, default=PDP)

    def __str__(self):
        return self.party_name



class Polling_unit(models.Model):

   
    polling_unit_name = models.CharField(max_length=50,null=True)
    party_score = models.IntegerField()
    polling_unit_description = models.TextField(max_length=255,null=True)
    date_entered = models.DateField(auto_now_add=True,blank=True, null=True)
    lat = models.CharField(max_length=255,null=True)
    lng = models.CharField(max_length=255,null=True)
    entered_by_user = models.ForeignKey('AgentDetail', on_delete=models.CASCADE, related_name='polling_unit_agents')
    user_ip_address = models.CharField(max_length=50,null=True)
    ward_id = models.ForeignKey('Ward', on_delete=models.CASCADE, related_name='polling_units_wards')
    party_id = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='party')

    def __str__(self):
        return self.polling_unit_name

        

   
   



class State(models.Model):

    state_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.state_name

   
    



class Ward(models.Model):

    ward_name = models.CharField(max_length=50,null=True)
    polling_unit_name = models.CharField(max_length=50,null=True)
    party_score = models.IntegerField()
    ward_description = models.CharField(max_length=255,null=True)
    date_entered = models.DateField(auto_now_add=True,blank=True, null=True)
    # entered_by_user = models.CharField(max_length=50,null=True)
    user_ip_address = models.CharField(max_length=50,null=True)
    lga_id = models.ForeignKey('Lga', on_delete=models.CASCADE, related_name='ward_lga_id')
    # entered_by_user = models.ForeignKey('AgentDetail', on_delete=models.CASCADE, related_name='ward_agent_details')

   
    def __str__(self):
        return self.ward_name

   

# class Image(models.Model):
   
#     title = models.CharField(max_length=50)
#     pub_date = models.DateField(auto_now_add=True)
#     image_path = models.ImageField(upload_to = 'images/')
   



    class meta:
        ordering = ['-date_entered'] 


    @classmethod
    def get_all(cls, id):
        wards = cls.objects.filter(id=id).all()
        return wards


    def save_ward(self):
        self.save()



    @classmethod
    def update_(cls, id, update):
        updated =cls.objects.filter(id=id).update(ward = update)

        return updated
      
        
    @classmethod
    def search_users(cls, search_term):
        names = cls.objects.filter(ward_name__icontains=search_term)
        return name
                
        

#     class meta:
#         ordering = ['-pub_date'] 



#     def __str__(self):
#         return self.title


# class Listing(models.Model):
#     apartments = "apartments"
#     Bungalows = "bungalows"
#     Mansionattes = "mansionattes"

#     PROPERTY_CHOICES = [
#     (apartments, "apartments"),
#     (Bungalows, "bungalows"),
#     (Mansionattes, "mansionattes")
#     ]



#     title = models.CharField(max_length=50,)
#     location = models.CharField(max_length=100,null=True)
#     date = models.DateField(auto_now_add=True,blank=True, null=True)
#     category = models.CharField(max_length=255,null=True, choices=PROPERTY_CHOICES, default=apartments)
#     description = models.CharField(max_length=255,null=True)
#     bedrooms = models.CharField(max_length=255,null=True)
#     pricing = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     featured_pic_path = models.ImageField(upload_to = 'list/')
#     user = models.ForeignKey(User,related_name='listings', null=True, on_delete=models.CASCADE, blank=True,)
#     timeslot = models.ForeignKey(Timeslot,null=True, on_delete=models.CASCADE, related_name='timeslots')
#     booking = models.ForeignKey(Booking,null=True, on_delete=models.CASCADE, related_name='bookings')


#     @classmethod
#     def get_all(cls):
#         listing = cls.objects.all()
#         return listing

#     def get_listing(self,id):
#         listing = Listing.objects.filter(listing_id=id).all()
#         return listing
            

#     @classmethod
#     def search_by_name(cls,search_term):
#         listing = cls.objects.filter(title__icontains=search_term)
#         return listing

#     @classmethod
#     def show_by_category(cls, category):
#         listing = cls.objects.filter(category=category).all()
#         return listing
    

#     def save_listing(self):
#         self.save()  

#     def delete_listing(self):
#         self.delete()      


#     def __str__(self):
#         return self.category
