from django import forms

from pretix_attendance_certificate_neo.models import AttendanceCertificateLayout


class OrganizerLayoutForm(forms.ModelForm):
    class Meta:
        model = AttendanceCertificateLayout
        fields = ["name"]
