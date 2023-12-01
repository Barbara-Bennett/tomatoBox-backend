from django.db import models

class Box(models.Model):
    BOXTYPES = (
        ("premium", "Premium"),
        ("common", "Common"),
    )

    box_type = models.CharField(max_length=15, primary_key=True, choices=BOXTYPES)
    new_boxes = models.IntegerField(default=0)
    qtt_total = models.IntegerField(default=0)
    box_qtt = models.IntegerField(default=0)
    damaged_box_qtt = models.IntegerField(default=0)
    borrowed_producer = models.IntegerField(default=0)
    borrowed_merchant = models.IntegerField(default=0)