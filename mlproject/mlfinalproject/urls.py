from django.urls import path
from . import views  

app_name = 'mlfinalproject'

urlpatterns = [ 
    path('', views.mlfinalproject, name='mlfinalproject'),

    path('class_results/', views.class_results, name='class_results'),

    path('classification/', views.classification, name='classification'),
    path('class_viz/', views.class_viz, name='class_viz'), 
    path('classification_pred/', views.classification_pred, name='classification_pred'),  
    
    path('reg_pred/', views.reg_pred, name='reg_pred'),  

    path('import/', views.import_csv, name='import_csv'),    
]
