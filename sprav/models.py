from django.db import models


class ProductionEquipment(models.Model):
    name = models.CharField("Тип производственного оборудования", unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип производственного оборудования"
        verbose_name_plural = "Типы производственного оборудования"


class MachinesType(models.Model):
    equip_type = models.ForeignKey(ProductionEquipment, models.DO_NOTHING, verbose_name="Тип производственного оборудования")
    name = models.CharField("Тип станка", unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип станка"
        verbose_name_plural = "Типы станков"


class Machine(models.Model):
    type = models.ForeignKey(MachinesType, models.DO_NOTHING, verbose_name="Тип станка")
    name = models.CharField("Название станка", unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Станок"
        verbose_name_plural = "Станки"


# Create your models here.
class ProductionArea(models.Model):
    type = models.ForeignKey(Machine, models.DO_NOTHING, verbose_name="Станок")
    area = models.FloatField("Производственная площадь")

    class Meta:
        verbose_name = "Производственная площадь"
        verbose_name_plural = "Производственная площади"


