from django.contrib import admin
import jdatetime
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import (
    Lead,
    Product,
    ProductImage,
    Certification,
)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "jalali_created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "phone", "email")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

    def jalali_created_at(self, obj):
        return jdatetime.datetime.fromgregorian(
            datetime=obj.created_at
        ).strftime('%Y/%m/%d - %H:%M')

    jalali_created_at.short_description = "تاریخ ثبت"



# =======================
# Product Inlines
# =======================
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "order")
    ordering = ("order",)

# ======== Form با CKEditor ========
class ProductAdminForm(forms.ModelForm):
    specs_table = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Product
        fields = "__all__"


# =======================
# Product Admin
# =======================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    inlines = (
        ProductImageInline,
    )

# =======================
# Certificat Admin
# =======================
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "order")
    list_editable = ("order",)
    search_fields = ("title", "issuer", "description")

