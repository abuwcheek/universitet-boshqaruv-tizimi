from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


ROLE_RECTOR = "RECTOR"
ROLE_VICE_RECTOR = "VICE_RECTOR"
ROLE_DEAN = "DEAN"
ROLE_HEAD_OF_DEPARTMENT = "HEAD_OF_DEPARTMENT"
ROLE_TEACHER = "TEACHER"

ROLE_CHOICES = (
    (ROLE_RECTOR, "Rektor"),
    (ROLE_VICE_RECTOR, "Prorektor"),
    (ROLE_DEAN, "Dekan"),
    (ROLE_HEAD_OF_DEPARTMENT, "Kafedra mudiri"),
    (ROLE_TEACHER, "O'qituvchi"),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan sana"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="O'zgartirilgan sana"
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name="O'chirilgan"
    )

    class Meta:
        abstract = True



class User(AbstractUser, BaseModel):
    username = None
    objects = UserManager()

    full_name = models.CharField(
        max_length=255,
        verbose_name="F.I.O."
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Telefon"
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        verbose_name="Email"
    )

    position = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default=ROLE_TEACHER,
        verbose_name="Lavozim",
        blank=True,
        null=True,
    )

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Maosh",
        null=True,
        blank=True
    )

    hire_date = models.DateField(
        verbose_name="Ishga qabul qilingan sana",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["full_name", 'phone']
    

    def __str__(self):
        return self.full_name
