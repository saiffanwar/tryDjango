from django.shortcuts import render

# Create your views here.
from .models import PortfolioDoc


def document_detail_page(request):
    obj = PortfolioDoc.objects.get(id=3)
    context = {"object": obj}
    return render(request, "portfolio/document_deatail_page.html", context)