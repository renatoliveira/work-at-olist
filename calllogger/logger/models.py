from django.db import models


class Call(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    source = models.TextField(max_length=20)
    destination = models.TextField(max_length=20)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        CallStart.objects.create(call=self)


class CallStart(models.Model):
    call = models.ForeignKey('Call', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CallEnd(models.Model):
    call = models.ForeignKey('Call', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
