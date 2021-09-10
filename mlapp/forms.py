
from django import forms
from .models import Image

# forms.py
from django import forms


class ImageForm(forms.ModelForm):

	class Meta:
		model = Image
		fields = ['name', 'image']
		widgets = {
                'name':forms.TextInput(attrs={'class':'input1',"type": "text","placeholder": "Enter Your Name "})
		}
