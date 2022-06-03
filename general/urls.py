from django.urls import path
from . import views

urlpatterns = [
  
    path('Update_spe', views.Updates, name='Updates'),
    path('Update_mat', views.Updatem, name='Updatem'),
    path('Add_spe', views.Adds, name='Adds'),
    path('Add_mat', views.Addm, name='Addm'),
    path('Remove_spe', views.Removes, name='Removes'),
    path('Remove_mat', views.Removem, name='Removem'),
    path('spe', views.spe, name='spe'),
    path('mat', views.mat, name='mat'),
    path('', views.general, name='general'),

    

]
