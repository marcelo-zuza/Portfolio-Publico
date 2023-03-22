from django.urls import path
from .views import IndexView, TesteView, ProdutosView, VisitasView, VisitasFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste', TesteView.as_view(), name='teste'),
    path('produtos', ProdutosView.as_view(), name='produtos'),
    path('visitas', VisitasView.as_view(), name='visitas'),
    path('visitasform', VisitasFormView.as_view(), name='visitasform')
]
