from django.contrib import admin
from django.urls import path
from gestion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("index/", views.view_index, name="index"),
                  path("contact-list/", views.view_list_contact, name="list"),
                  path("create-contact/", views.view_create_contact, name="create-contact"),
                  path("delete/<int:id>", views.destroy, name="delete"),
                  path("update/<int:id>", views.update, name="update")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
