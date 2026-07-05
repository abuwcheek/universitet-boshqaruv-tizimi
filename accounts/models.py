from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


ROLE_ADMIN = "ADMIN"
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
    (ROLE_ADMIN, "Admin"),
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

    login = models.CharField(
        unique=True,
        max_length=100
    )

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
        blank=True,
        null=True,
        verbose_name="Email"
    )

    position = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default=ROLE_ADMIN,
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

    faculty = models.ForeignKey(
    "faculties.Faculty",
    on_delete=models.SET_NULL,
    null=True,
    blank=True
    )

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    USERNAME_FIELD = "login"

    REQUIRED_FIELDS = ["full_name", 'phone']
    

    def __str__(self):
        return self.full_name
