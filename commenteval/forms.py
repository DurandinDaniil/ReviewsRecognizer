from django import forms
 
class UserForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'pb-cmnt-textarea', 'name' : 'text', 'placeholder': 'Write your review here!'}), label=False)