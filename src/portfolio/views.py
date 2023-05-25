from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import PortfolioDoc

# Create your views here.
def portfolio_detail(request, doc_slug):
    # obj = PortfolioDoc.objects.get(id=doc_id)
    obj = get_object_or_404(PortfolioDoc, slug=doc_slug)
    template_name = "portfolio_detail.html"
    context = {"object": obj}
    # return render(request, "/home/saif/Projects/tryDjango/src/templates/portfolio_detail.html", context)
    return FileResponse(obj.document, content_type='application/pdf')
