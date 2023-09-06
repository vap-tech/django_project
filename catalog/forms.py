from django import forms

from catalog.models import Product, Version


words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        """Валидация поля name"""
        cleaned_data = self.cleaned_data['name']
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещено использовать слово {cleaned_data}')
        return cleaned_data

    def clean_description(self):
        """Валидация поля description"""
        cleaned_data = self.cleaned_data['description']
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещено использовать слово {cleaned_data}')
        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
