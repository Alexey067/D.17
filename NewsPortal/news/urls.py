from django.urls import path
from .views import (
   PostList, PostDetail, PostCreate, PostSearch,  PostEdit, PostDelete, CategoryListView, subscribe
)
from .views import IndexView
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', cache_page(300)(PostDetail.as_view()), name='post_detail'),
   path('create/', cache_page(60)(PostCreate.as_view()), name='post_create'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/edit/', cache_page(300)(PostEdit.as_view()), name='post_edit'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_news'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('', IndexView.as_view())
]
