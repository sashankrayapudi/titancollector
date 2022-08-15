from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('titans/', views.titans_index, name='index'),
  path('titans/<int:titan_id>/', views.titans_detail, name='detail'),
  path('titans/create/', views.TitanCreate.as_view(), name='titans_create'),
  path('titans/<int:pk>/update/', views.TitanUpdate.as_view(), name='titans_update'),
  path('titans/<int:pk>/delete/', views.TitanDelete.as_view(), name='titans_delete'),
  path('titans/<int:titan_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('titans/<int:titan_id>/assoc_eldian/<int:eldian_id>/', views.assoc_eldian, name='assoc_eldian'),
  path('titans/<int:titan_id>/unassoc_eldian/<int:eldian_id>/', views.unassoc_eldian, name='unassoc_eldian'),
  path('eldians/', views.EldianList.as_view(), name='eldians_index'),
  path('eldians/<int:pk>/', views.EldianDetail.as_view(), name='eldians_detail'),
  path('eldians/create/', views.EldianCreate.as_view(), name='eldians_create'),
  path('eldians/<int:pk>/update/', views.EldianUpdate.as_view(), name='eldians_update'),
  path('eldians/<int:pk>/delete/', views.EldianDelete.as_view(), name='eldians_delete'),
]
