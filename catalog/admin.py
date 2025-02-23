from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "product_price", "category",)
# продуктов выведите в список id, название, цену и категорию.
    list_filter = ("category",)
# результат отображения фильтровать по категории
    search_fields = ("product_name", "product_info",)
# осуществлять поиск по названию и полю описания.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name",)
# Для категорий выведите id и наименование в список отображения


# admin.site.register(Product)
# Register your models here.
