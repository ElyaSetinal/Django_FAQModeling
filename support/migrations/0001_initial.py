# Generated by Django 4.0.4 on 2022-04-19 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('NM', '일반'), ('AC', '계정'), ('ET', '기타')], max_length=2, verbose_name='카테고리')),
                ('title', models.TextField(verbose_name='제목')),
                ('emailAddress', models.TextField(verbose_name='이메일주소')),
                ('phonenumber', models.TextField(verbose_name='전화번호')),
                ('question', models.TextField(verbose_name='내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='질문')),
                ('category', models.CharField(blank=True, choices=[('NM', '일반'), ('AC', '계정'), ('ET', '기타')], max_length=2, null=True, verbose_name='카테고리')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='답변')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('created_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
                ('last_modify_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='최종 수정자')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='답변내용')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('created_person', models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
                ('last_modify_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='최종 수정자')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.inquiry')),
            ],
        ),
    ]
