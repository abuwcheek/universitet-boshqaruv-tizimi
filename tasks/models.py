from django.db import models

from accounts.models import User
from faculties.models import Faculty
from departments.models import Department


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



STATUS_CREATED = "CREATED"
STATUS_IN_PROGRESS = "IN_PROGRESS"
STATUS_COMPLETED = "COMPLETED"

STATUS_CHOICES = (
    (STATUS_CREATED, "Yaratildi"),
    (STATUS_IN_PROGRESS, "Jarayonda"),
    (STATUS_COMPLETED, "Bajarildi"),
)



PRIORITY_LOW = "LOW"
PRIORITY_MEDIUM = "MEDIUM"
PRIORITY_HIGH = "HIGH"

PRIORITY_CHOICES = (
    (PRIORITY_LOW, "Past"),
    (PRIORITY_MEDIUM, "O'rta"),
    (PRIORITY_HIGH, "Yuqori"),
)



class Task(BaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Vazifa nomi"
    )

    description = models.TextField(
        verbose_name="Tavsif"
    )

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Xodim"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_tasks",
        verbose_name="Kim tomonidan berilgan"
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default=PRIORITY_MEDIUM
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED
    )

    deadline = models.DateField()


    def __str__(self):
        return self.title