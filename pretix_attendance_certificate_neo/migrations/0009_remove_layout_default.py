from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pretix_attendance_certificate_neo", "0008_signing_timestamp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendancecertificatelayout",
            name="default",
        ),
    ]
