from django import forms
from .models import Question,Order

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title','desc')
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields= "__all__"
