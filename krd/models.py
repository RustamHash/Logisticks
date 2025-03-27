from django.db import models


class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    marking_goods = models.CharField(max_length=155)
    item_name = models.CharField(max_length=155)
    group_id = models.IntegerField()
    is_active = models.BooleanField()
    shelf_life = models.IntegerField()
    pieces_pkge = models.IntegerField()
    amount_inblock = models.IntegerField()
    amount_inbox = models.IntegerField()
    amount_inpallet = models.IntegerField()
    user_create = models.CharField(max_length=155, null=True, blank=True)
    date_create = models.DateTimeField(null=True, blank=True)
    user_update = models.CharField(max_length=155, null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True)
    weight = models.DecimalField(max_digits=30, decimal_places=2)
    weight_netto = models.DecimalField(max_digits=30, decimal_places=2)
    length_box = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    width_box = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    height_box = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    barcode_block = models.CharField(max_length=155, null=True, blank=True)
    barcode_box = models.CharField(max_length=155, null=True, blank=True)
    barcode_pkge = models.CharField(max_length=155, null=True, blank=True)

    class Meta:
        ordering = ('id', 'marking_goods')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Agent(models.Model):
    program_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=255)
    level_id = models.IntegerField()
    is_active = models.BooleanField()
    comment = models.CharField(max_length=255, null=True, blank=True)
    date_create = models.DateTimeField(null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True)
    group_id = models.IntegerField()
    contact_phone = models.CharField(max_length=155, null=True, blank=True)
    contact_face = models.CharField(max_length=155, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('id', 'item_name')
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'


class Invoice(models.Model):
    class TypeOrder(models.IntegerChoices):
        ORDER = 103
        PORDER = 203

    id = models.IntegerField(primary_key=True)
    program_id = models.IntegerField(verbose_name="Код программы")
    acs_number = models.CharField(max_length=155, verbose_name="Номер накладной")
    is_active = models.BooleanField(verbose_name="Активный")
    date_doc = models.DateField(verbose_name="Дата накладной")
    is_entry = models.BooleanField(verbose_name="Проведен")
    invoice_type_id = models.IntegerField(verbose_name="Тип операции", choices=TypeOrder)
    from_id = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='invoice_from', verbose_name="От кого")
    to_id = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='invoice_to', verbose_name="Кому")
    from_req_id = models.IntegerField(verbose_name="От имени")
    to_req_id = models.IntegerField(verbose_name="На имя")
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='invoice', verbose_name="Агент")
    date_create = models.DateField(verbose_name="Дата создания")
    date_update = models.DateField(verbose_name="Дата изменения", null=True, blank=True)
    comment = models.CharField(max_length=155, verbose_name="Комментарий", null=True, blank=True)
    user_create = models.CharField(max_length=155, verbose_name="Создан пользователем")
    user_update = models.CharField(max_length=155, verbose_name="Изменен пользователем", null=True, blank=True)
    delivery = models.BooleanField(verbose_name="Доставка")
    uid = models.IntegerField(verbose_name="uid")
    order_number = models.CharField(max_length=155,verbose_name="Номер заказа", null=True, blank=True)

    class Meta:
        ordering = ["-date_doc"]
        verbose_name = "Операция"
        verbose_name_plural = "Операции"


class InvoiceBody(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_body', verbose_name="")
    line_id = models.IntegerField()
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='invoice_body_goods', verbose_name="")
    price = models.DecimalField(max_digits=30, decimal_places=2)
    summa = models.DecimalField(max_digits=30, decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField()

    class Meta:
        ordering = ("id", "invoice_id", "goods_id",)
        verbose_name = "Строка операции"
        verbose_name_plural = "Строки операций"
