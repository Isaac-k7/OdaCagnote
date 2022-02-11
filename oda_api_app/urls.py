from django.urls import path
from . import views

urlpatterns = [
    path("", views.ApiOverview),
    path('payements/create', views.add_payments, name='add-payment'),
    path('payements/', views.ListPayementAPIView.as_view(), name='all-payments'),
    path('payements/update/<int:id>', views.update_payments, name='update-payments'),
    path('payements/<int:id>/delete/', views.delete_payments, name='delete-payments'),

]
