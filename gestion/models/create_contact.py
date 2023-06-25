from django import forms


from gestion.models.contact import Contact


class ContactForm(forms.ModelForm):
    class Meta:

        model = Contact
        fields = "__all__"
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'pseudo': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control default-select'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),


        }

