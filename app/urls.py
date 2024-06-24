from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView, home_view
from contato.views import NewContactView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', CarListView.as_view(), name='cars_list'),
    path('contact/', NewContactView.as_view(), name='new_contact'),
    path('new_cars/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

