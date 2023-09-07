from django import forms

from catalog.models import Product, Version, Feedback

words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_current_version':
                continue
            field.widget.attrs['class'] = 'form-control'


class FeedbackForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'
