from django.urls import path
from .views import (
    PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, CategoryList, subscribe
)
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60*1)(PostsList.as_view()), name='post_list'),
    path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]