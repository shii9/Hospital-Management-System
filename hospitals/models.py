from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)

    def save(self, *args, **kwargs):
        if not self.id:

            used_ids = Doctor.objects.values_list('id', flat=True)
            for i in range(1, max(used_ids, default=0) + 2):
                if i not in used_ids:
                    self.id = i
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name;


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)


    def save(self, *args, **kwargs):
        if not self.id:

            used_ids = Patient.objects.values_list('id', flat=True)
            for i in range(1, max(used_ids, default=0) + 2):
                if i not in used_ids:
                    self.id = i
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name;



class Nurse(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)

    # other fields

    def save(self, *args, **kwargs):
        if not self.id:

            used_ids = Nurse.objects.values_list('id', flat=True)
            for i in range(1, max(used_ids, default=0) + 2):
                if i not in used_ids:
                    self.id = i
                    break
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name;


class WardBoy(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)

    def save(self, *args, **kwargs):
        if not self.id:

            used_ids = WardBoy.objects.values_list('id', flat=True)
            for i in range(1, max(used_ids, default=0) + 2):
                if i not in used_ids:
                    self.id = i
                    break
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name;


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} -- {self.patient.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
