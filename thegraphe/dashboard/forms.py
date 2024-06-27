from django import forms

from frontend.models import main_category


class MainCategoryForm(forms.ModelForm):
    class Meta:
        model = main_category
        fields = ['name', 'slug', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control form_style'}),
        }
