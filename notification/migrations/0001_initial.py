# Generated by Django 5.1.4 on 2025-02-20 18:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("NotificationID", models.AutoField(primary_key=True, serialize=False)),
                ("Message", models.TextField()),
                ("DateSent", models.DateTimeField(auto_now_add=True)),
                (
                    "NotificationType",
                    models.CharField(
                        choices=[
                            ("urgent", "Urgent"),
                            ("important", "Important"),
                            ("info", "Info"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "Sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_notifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-DateSent"],
            },
        ),
        migrations.CreateModel(
            name="NotificationRecipient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("read", models.BooleanField(default=False)),
                ("read_date", models.DateTimeField(blank=True, null=True)),
                (
                    "notification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="notification.notification",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("notification", "recipient")},
            },
        ),
        migrations.AddField(
            model_name="notification",
            name="Recipients",
            field=models.ManyToManyField(
                related_name="received_notifications",
                through="notification.NotificationRecipient",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
