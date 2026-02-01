from django.contrib import admin
from .models import (
    Lead,
    Product,
    ProductImage,
    ProductSection,
    ProductSectionImage,
    ProductSectionSpec,
    Certification,
)


# =======================
# Lead Admin
# =======================
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "phone", "email")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


# =======================
# Product Inlines
# =======================
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "order")
    ordering = ("order",)


class ProductSectionInline(admin.StackedInline):
    model = ProductSection
    extra = 1
    fields = ("title", "content", "order")
    ordering = ("order",)
    show_change_link = True


# =======================
# Product Admin
# =======================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    inlines = (
        ProductImageInline,
        ProductSectionInline,
    )


# =======================
# Product Section Inlines
# =======================
class ProductSectionImageInline(admin.TabularInline):
    model = ProductSectionImage
    extra = 1
    fields = ("image", "order")
    ordering = ("order",)


class ProductSectionSpecInline(admin.TabularInline):
    model = ProductSectionSpec
    extra = 1
    fields = ("name", "value")


# =======================
# Product Section Admin
# =======================
@admin.register(ProductSection)
class ProductSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "product", "order")
    list_filter = ("product",)
    search_fields = ("title", "content")
    ordering = ("product", "order")
    inlines = (
        ProductSectionImageInline,
        ProductSectionSpecInline,
    )

# =======================
# Certificat Admin
# =======================
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "order")
    list_editable = ("order",)
    search_fields = ("title", "issuer", "description")

