from django.core.exceptions import ValidationError
from django.db import models


class Contact(models.Model):
    pseudo = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')])
    contact = models.CharField(max_length=16)
    matricule = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def clean(self):
        super().clean()  # Appeler la méthode clean() du modèle parent

        errors = {}

        if len(self.pseudo) < 3:
            errors['pseudo'] = ValidationError("Le pseudo doit comporter au moins 3 caractères.")

        if len(self.city) < 2:
            errors['city'] = ValidationError("La ville doit comporter au moins 3 caractères.")

        if len(self.contact) < 10:
            errors['contact'] = ValidationError("Le contact doit avoir au moins 10 caractères")

        if errors:
            raise ValidationError(errors)
