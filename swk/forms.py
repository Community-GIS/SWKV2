from django import forms
from .models import Tracksheet,DutyEntry

            
demarcated_lane = [
        ('Waras lane to Hira Seth chawl','Waras lane - Hira Seth chawl'),
        ('Navneet Lane to Tare Galli','Navneet Lane - Tare Galli'),
        ('BhandarWada to Amar Prem Chowk','BhandarWada - Amar Prem Chowk'),
        ('Shankar Mandir to Bhagat Galli ','Shankar Mandir - Bhagat Galli '),
        ('Gonta Galli to Kranti Galli','Gonta Galli - Kranti Galli'),
        ('Kranti Galli to Navjeevan Chauk','Kranti Galli - Navjeevan Chauk'),
        ('Pakhari Galli ','Pakhari Galli '),
        ('Vada pav Galli to Fish market','Vada pav Galli - Fish market'),
        ('Payari','Payari'),
        ('Sonapur to Dukkur Galli','Sonapur - Dukkur Galli'),
        ('Dukkur to Taak Galli','Dukkur - Taak Galli'),
        ('Nagobacha Ghumat to Achanak','Nagobacha Ghumat - Achanak'),
        ('Golfadevi','Golfadevi'),
    ]
atten_name = [
        ('Amrapali','Amrapali'),
        ('Jana pote','Jana pote'),
        ('Kaushalya', 'Kaushalya'),
        ('Parvati','Parvati'),
        ('Sakuntala','Sakuntala'),
        ('Asha','Asha'),

    ]
class TracksheetForm(forms.ModelForm):
   
    timeslot= [

                ('7:30am - 8:30 am','Morning'),
                ('7:30pm - 8:30 pm','Evening'),

    ]

    
    date= forms.DateField(required=False,widget=forms.TextInput(attrs={'type': 'date'}))
    lane_name = forms.CharField(label = 'Name of the Lane/Galli',widget=forms.Select(choices=demarcated_lane))
    first_attendants_name = forms.CharField(label = 'Name of First Attendant',widget=forms.Select(choices=atten_name))
    second_attendants_name = forms.CharField(label = 'Name of Second Attendant',widget=forms.Select(choices=atten_name))
    time_of_visit = forms.CharField(label = "Morning /Evening Visit",widget=forms.Select(choices=timeslot))

    class Meta:

        model = Tracksheet
        fields = ['date','lane_name','num_attendants','first_attendants_name','second_attendants_name',
            'time_of_visit','num_houses_reached','num_houses_doing_segg','num_houses_giving_mixwaste','drywaste_bf',
            'drywaste_af','wetwaste_bf','wetwaste_af']
        widgets = {
            'date':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


class DutyEntryForm(forms.ModelForm):
    lane_name = forms.CharField(label = 'Name of the Lane/Galli',widget=forms.Select(choices=demarcated_lane))
    first_attendants_name = forms.CharField(label = 'Name of First Attendant',widget=forms.Select(choices=atten_name))
    second_attendants_name = forms.CharField(label = 'Name of Second Attendant',widget=forms.Select(choices=atten_name))
    num_houses_lane = forms.CharField(label = 'Number of houses in Lane')

    class Meta:
        model = DutyEntry
        fields = '__all__'