from django.db import models

class Certification(models.Model):
    title = models.CharField("عنوان مجوز / گواهی", max_length=150)
    issuer = models.CharField("مرجع صادرکننده", max_length=150, blank=True)
    description = models.TextField("توضیحات", blank=True)
    image = models.ImageField("تصویر مدرک", upload_to="certifications/")
    order = models.PositiveIntegerField("ترتیب نمایش", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "مجوز و گواهی"
        verbose_name_plural = "مجوزها و گواهی‌ها"

    def __str__(self):
        return self.title


class Lead(models.Model):
    name = models.CharField("نام", max_length=100)
    phone = models.CharField("شماره تماس", max_length=20)
    email = models.EmailField("ایمیل", blank=True, null=True)
    message = models.TextField("پیام")
    created_at = models.DateTimeField("تاریخ ثبت", auto_now_add=True)

    class Meta:
        verbose_name = "درخواست تماس"
        verbose_name_plural = "درخواست‌های تماس"

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Product(models.Model):
    title = models.CharField("نام محصول", max_length=150)
    description = models.TextField("توضیح اصلی صفحه")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصول"

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField("تصویر", upload_to="product/")
    order = models.PositiveIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصول"

class ProductSection(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="sections"
    )

    title = models.CharField("عنوان سکشن", max_length=150)
    content = models.TextField("متن سکشن", blank=True)
    order = models.PositiveIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "سکشن محصول"
        verbose_name_plural = "سکشن‌های محصول"

    def __str__(self):
        return self.title

class ProductSectionImage(models.Model):
    section = models.ForeignKey(
        ProductSection,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField("تصویر", upload_to="product/sections/")
    order = models.PositiveIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "تصویر سکشن"
        verbose_name_plural = "تصاویر سکشن"

class ProductSectionSpec(models.Model):
    section = models.ForeignKey(
        ProductSection,
        on_delete=models.CASCADE,
        related_name="specs"
    )

    name = models.CharField("عنوان مشخصه", max_length=150)
    value = models.CharField("مقدار", max_length=150)

    class Meta:
        verbose_name = "مشخصه فنی"
        verbose_name_plural = "مشخصات فنی"

