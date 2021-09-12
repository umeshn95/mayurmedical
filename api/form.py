from .models import Product
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['customer_name', 'product_name', 'customer_phone', 'customer_address', 'image']
        # widgets = {
        #     'customer_name':forms.TextInput(),
        #     'product_name':forms.TextInput(),
        #     'product_quantity':forms.NumberInput(),
        #     'product_mg':forms.NumberInput(),
        #     'customer_phone':forms.NumberInput(),
        #     'customer_address':forms.TextInput(),
        #     'image':forms.FileInput()
        # }