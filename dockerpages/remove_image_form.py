from django import forms
from .listimages import ListImages
from .Connection import remote_Machine
#from .views import remote_Machine
class RemoveImageForm(forms.Form):

  #Images=[]
  Images=ListImages(remote_Machine)
  data = []
  for value in Images:
    data.append(value[0])
  print('this is in removeimages')
  
  print('this is in removeimageform class')
  Text = forms.ChoiceField(label="",
                          widget=forms.Select(attrs={
                                                      'class':'form-control'
                                                    }),
                                                    )
  
  Text.widget = forms.Select(choices=[(value[0], value[0]) for value in Images])
  