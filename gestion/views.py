from django.contrib import messages
from django.shortcuts import render, redirect
from gestion.models.contact import Contact

# Create your views here.
from gestion.models.create_contact import ContactForm


def view_index(request):
    return render(request, 'index.html')


def view_list_contact(request):
    getContact = Contact.objects.all()
    valeur = list(getContact.values())
    print(valeur)
    return render(request, 'contact-list.html', {'contacts': getContact})


def view_create_contact(request):
    if request.method == 'POST':
        contact_form: ContactForm = ContactForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Félicitations! Le formulaire a été soumis avec succès.")
            return redirect('list')

    else:
        contact_form = ContactForm()
    return render(request, 'forms/create-contact.html', {"contact_form": contact_form})


def update(request, id):
    update_contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        form: ContactForm = ContactForm(request.POST, instance=update_contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Félicitations! Modification effectué avec succès.")
            return redirect('list')
    else:
        form = ContactForm(instance=update_contact)
    return render(request, 'forms/update.html', {'form': form, 'update': update_contact})


def destroy(request, id):
    deleted = Contact.objects.get(id=id)
    deleted.delete()
    messages.success(request, "Félicitations! supprèssion avec succès.")
    return redirect('list')
