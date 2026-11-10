from django import forms
from django.core.exceptions import ValidationError
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Create a strong password'}),
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'})
    )
    
    class Meta:
        model = User
        fields = [
            'full_name', 'age', 'gender', 'photo',
            'primary_category', 'eligible_categories',
            'occupation', 'phone', 'email', 'notify'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'age': forms.NumberInput(attrs={'min': 18, 'max': 120}),
            'phone': forms.TextInput(attrs={'placeholder': '9876543210'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com'}),
            'occupation': forms.TextInput(attrs={'placeholder': 'e.g., Farmer, Student, Business Owner'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False
        self.fields['email'].required = False
        self.fields['notify'].initial = True
        
        # Customize eligible_categories field
        self.fields['eligible_categories'].widget = forms.CheckboxSelectMultiple(
            choices=User.CATEGORY_CHOICES[:-1]  # Exclude 'neutral'
        )
        self.fields['eligible_categories'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match")
        
        # Check if phone already exists
        phone = cleaned_data.get('phone')
        if phone and User.objects.filter(phone=phone).exists():
            raise ValidationError("This phone number is already registered")
        
        # Validate neutral category
        primary_category = cleaned_data.get('primary_category')
        eligible_categories = cleaned_data.get('eligible_categories', [])
        
        if primary_category == 'neutral' and not eligible_categories:
            raise ValidationError("Please select at least one category for multiple eligibility")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
            # Save many-to-many fields
            self.save_m2m()
        
        return user

class LoginForm(forms.Form):
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )