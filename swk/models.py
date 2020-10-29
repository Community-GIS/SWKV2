from django.db import models
from django import forms
from django.forms import ModelForm
import datetime


from wagtail.core.models import Page


class HomePage(Page):

    template = "HomePage.html"



class TracksheetModel(Page):

    template = "TracksheetForm.html"

class Tracksheet(models.Model):
    track_id = models.AutoField(primary_key=True)
    lane_name = models.CharField(max_length=200, blank = False)
    date = models.DateField(default=datetime.date.today)
    time_of_visit = models.CharField(max_length=100)
    num_attendants = models.IntegerField(default = 2 )
    first_attendants_name = models.CharField(max_length=100)
    second_attendants_name = models.CharField(max_length=100)
    num_houses_reached = models.IntegerField(default= 20)
    num_houses_doing_segg = models.IntegerField()
    num_houses_giving_mixwaste = models.IntegerField()
    drywaste_bf = models.IntegerField()
    drywaste_af = models.IntegerField()
    wetwaste_bf = models.IntegerField()
    wetwaste_af = models.IntegerField()
    def __str__(self):
        return "{}-{}".format(self.date,self.lane_name)
