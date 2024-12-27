from django import forms
from .models import Newsletter, Contact, Comment, Booking

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = "__all__"

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"