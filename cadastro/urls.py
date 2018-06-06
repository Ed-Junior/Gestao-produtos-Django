from django.urls import path
from .views import prod_list, new_prod, delete_prod, prod_up

urlpatterns = [

    path('lista-de-produtos', prod_list, name='prod_list'),
    path('novo-produto', new_prod, name='new_prod'),
    path('atualizaproduto/<int:id>/', prod_up, name='prod_up'),
    path('deletarprod/<int:id>/', delete_prod, name='delete_prod'),


]
