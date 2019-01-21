from django import forms

class ImageForm(forms.Form):
    print("image forms ")
    image=forms.CharField(label="",required=True)
    image.widget=forms.TextInput(attrs={
        'placeholder': 'Image',
        'id': 'inputGroup-sizing-default',
        'class': 'form-control'
    })
    #image.initial="nginx"
    tag=forms.CharField(label="",required=False)
    tag.widget=forms.TextInput(attrs={
        'placeholder': 'Tag(latest)',
        'style' : 'width=120',
        'id': 'inputGroup-sizing-default',
        'class': 'form-control'

    })
