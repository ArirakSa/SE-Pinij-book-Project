from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStampedModel(models.Model):
    class Meta:
        abstract = True # ทำให้ไม่สร้างตารางในฐานข้อมูล

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

# คลาส Member ใช้สำหรับเก็บข้อมูลสมาชิกในระบบ
class Member(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture_url = models.CharField(max_length=500, default='')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = 'สมาชิก'
        verbose_name = 'สมาชิก'
