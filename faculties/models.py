from django.db import models



class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqti"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="O'zgartirilgan vaqti"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Faol"
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name="O'chirilgan"
    )

    class Meta:
        abstract = True



class Faculty(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Fakultet nomi"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Tavsif"
    )

    def __str__(self):
        return self.name