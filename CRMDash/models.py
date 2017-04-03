from django.db import models

# Create your models here.

# TODO These are views that are required to be generated on the OpenERP / Odoo server first

class calls_by_status(models.Model):
    id = models.IntegerField(primary_key=True)
    nooftickets = models.IntegerField()
    stage = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'calls_by_status'


class inprogress_by_user(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=64)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inprogress_by_user'


class ticket_by_stage(models.Model):
    id = models.IntegerField(primary_key=True)
    stage = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'ticket_by_stage'
