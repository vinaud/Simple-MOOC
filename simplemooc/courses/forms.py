from django import forms

class ContactCourse(forms.Form):
    
    name = forms.CharField(label='nome', max_lenght=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem/Dúvida', widget = forms.Textarea)
