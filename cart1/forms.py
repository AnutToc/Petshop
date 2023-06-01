from django import forms
from .models import Order

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, label='Quantity')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
    
    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        if data > 10:
            raise forms.ValidationError('Maximum quantity is 10')
        return data

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'zip_code', 'phone_number']
        
class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    zip_code = forms.CharField(max_length=10, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
