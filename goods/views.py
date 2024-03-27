from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_list_or_404, render


from goods.models import Products

# Create your views here.


def catalog(request, category_slug):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", False)
    order_by = request.GET.get("order_by", False)

    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        if not goods:
            raise Http404

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    return render(request, "goods/product.html", {"product": product})
