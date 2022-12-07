from django.urls import path, include
from .views import CategoryListView, TagListView, BlogListCreateView, BlogRetrieveUpdateDestroyView

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
    path('tag-list/', TagListView.as_view()),
    path('blog-list-create/', BlogListCreateView.as_view()),
    path('blog-rud/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view()),

]
