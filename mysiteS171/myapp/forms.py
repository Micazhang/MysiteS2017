from django import forms
from myapp.models import Topic, Student
from django.contrib.auth.forms import UserCreationForm
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['subject','intro_course','time','avg_age']
        widget={'time':forms.RadioSelect()}
        label={'time':('Preferred Time'),'avg_age':('What is your age?'),'intro_course':('This should be an introductory level course')}


class InterestForm(forms.Form):
    interested = forms.ChoiceField(widget=forms.RadioSelect(), choices=((1, 'Yes'), (0, 'No')))
    age = forms.IntegerField(initial='20')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Additional Comments')

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = ['first_name','last_name','address','city','province','age']
        PROVINCE_CHOICES = (
            ('AB', 'Alberta'),
            ('MB', 'Manitoba'),
            ('ON', 'Ontario'),
            ('QC', 'Quebec'),
        )
        province = forms.ChoiceField(widget=forms.RadioSelect(),choices=PROVINCE_CHOICES)

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=Student
        fields=['username','first_name','last_name','email','address','city','province','age']