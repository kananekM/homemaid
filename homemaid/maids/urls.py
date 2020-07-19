from django.urls import path

from .views import MaidListView, MaidAddView, maid_another_list_view

urlpatterns = [
    path('', MaidListView.as_view(), name='maid-list'),
    path('v2/', maid_another_list_view, name='maid-another-list'),
    path('add/', MaidAddView.as_view(), name='maid-add'),
]
