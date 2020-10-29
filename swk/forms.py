from django import forms
from .models import Tracksheet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
import datetime

            
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
timeslot= [

            ('7:30am - 8:30 am','Morning'),
            ('7:30pm - 8:30 pm','Evening'),
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
    
    date= forms.DateField(required=True,widget=forms.TextInput(attrs={'type': 'date'}),initial=datetime.date.today)
    lane_name = forms.CharField(label = 'Name of the Lane/Galli',widget=forms.Select(choices=demarcated_lane))
    first_attendants_name = forms.CharField(label = 'Name of First Attendant',widget=forms.Select(choices=atten_name))
    second_attendants_name = forms.CharField(label = 'Name of Second Attendant',widget=forms.Select(choices=atten_name))
    time_of_visit = forms.CharField(label = "Morning /Evening Visit",widget=forms.Select(choices=timeslot))
    drywaste_bf = forms.CharField(label = "Dry waste before")
    drywaste_af = forms.CharField(label = "Dry waste after")
    wetwaste_bf = forms.CharField(label = "Wet waste before")
    wetwaste_af = forms.CharField(label = "Wet waste after")
    num_houses_doing_segg = forms.CharField(label = "Number of houses doing segregation")
    num_houses_giving_mixwaste = forms.CharField(label = "Number of houses giving mixwaste")


    
    # date  time_of_visit
    # lane_name
    # num_attendants first_attendants_name second_attendants_name 
    # num_houses_reached  num_houses_doing_segg  num_houses_giving_mixwaste 
    # drywaste_bf drywaste_af 
    # wetwaste_bf wetwaste_af 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('date', css_class='form-group col-md-3 mb-0'),
                Column('time_of_visit', css_class='form-group col-md-3 mb-0'),
                Column('lane_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            # 'address_1',
            # 'address_2',
            Row(
                Column('num_attendants', css_class='form-group col-md-4 mb-0'),
                Column('first_attendants_name', css_class='form-group col-md-4 mb-0'),
                Column('second_attendants_name', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            # 'check_me_out',
            Row(
                Column('num_houses_reached', css_class='form-group col-md-2 mb-0'),
                Column('num_houses_doing_segg', css_class='form-group col-md-5 mb-0'),
                Column('num_houses_giving_mixwaste', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('drywaste_bf', css_class='form-group col-md-3 mb-0'),
                Column('drywaste_af', css_class='form-group col-md-3 mb-0'),
                Column('wetwaste_bf', css_class='form-group col-md-3 mb-0'),
                Column('wetwaste_af', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )
    class Meta:

        model = Tracksheet
        fields = '__all__'
