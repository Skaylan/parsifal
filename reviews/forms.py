from django import forms
from reviews.models import Review

class CreateReviewForm(forms.ModelForm):
    title = forms.CharField(
            widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Systematic literature review\'s title' }), 
            max_length=255)
    description = forms.CharField(
            widget=forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Give a brief description of your systematic literature review' }), 
            max_length=500, 
            help_text='Try to keep it short, max 500 characters :)',
            required=False)

    class Meta:
        model = Review
        fields = ['title', 'description',]


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
            widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
            max_length=255)
    name = forms.SlugField(
            widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
            label='URL',
            help_text='Only letters, numbers, underscores or hyphens are allowed.',
            max_length=255)
    description = forms.CharField(
            widget=forms.Textarea(attrs={ 'class': 'form-control expanding', 'rows': '1' }), 
            max_length=500, 
            required=False)

    class Meta:
        model = Review
        fields = ['title', 'name', 'description',]