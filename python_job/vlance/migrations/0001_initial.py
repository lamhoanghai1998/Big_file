# Generated by Django 2.2.1 on 2019-05-31 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DichVu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('text', models.TextField(default='')),
                ('img', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='KyNang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LinhVuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ThanhPho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ViecTheoDuAn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='', max_length=255, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(max_length=255)),
                ('infojob', models.TextField(default='', max_length=500, verbose_name='Mô tả công việc')),
                ('time_ex', models.DateField(default='', verbose_name='Hạn chào giá')),
                ('NStu', models.IntegerField(default='', verbose_name='Ngân sách từ ')),
                ('NSden', models.IntegerField(default='', verbose_name='Ngân sách đến')),
                ('hinh', models.ImageField(default='', upload_to='', verbose_name='Hình ảnh đính kèm')),
                ('Dich_Vu', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vlance.DichVu', verbose_name='Dịch Vụ ')),
                ('Ky_nang', models.ManyToManyField(default='', to='vlance.KyNang', verbose_name='Kỹ Năng')),
                ('Linh_Vuc', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vlance.LinhVuc', verbose_name='Lĩnh vực')),
                ('Thanh_Pho', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vlance.ThanhPho', verbose_name='Chọn Thành Phố')),
            ],
        ),
    ]
