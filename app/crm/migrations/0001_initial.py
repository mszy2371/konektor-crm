# Generated by Django 3.2.4 on 2022-10-04 14:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('system_ads', models.SmallIntegerField(blank=True, choices=[(1, 'Google Ads'), (2, 'Facebook Ads'), (3, 'Internet'), (4, 'Newsletter')], null=True)),
                ('default', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.customer')),
            ],
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('link', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.customer')),
            ],
        ),
        migrations.CreateModel(
            name='LeadExtend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField(choices=[(1, 'Good'), (2, 'Bad'), (3, 'Duplicate')], default=1)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=15)),
                ('info', models.TextField(blank=True, null=True)),
                ('rodo', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('task_clickup_id', models.CharField(blank=True, max_length=12, null=True)),
                ('sms_id', models.CharField(blank=True, max_length=128, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.campaign')),
                ('landing_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.landingpage')),
                ('lead_extend', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.leadextend')),
            ],
        ),
    ]