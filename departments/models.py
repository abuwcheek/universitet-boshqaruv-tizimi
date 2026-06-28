from django.db import models
from faculties.models import Faculty
from accounts.models import User




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



class Department(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Kafedra nomi"
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="departments",
        verbose_name="Fakultet"
    )

    head = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="headed_departments",
        verbose_name="Kafedra mudiri"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Tavsif"
    )

    def __str__(self):
        return self.name