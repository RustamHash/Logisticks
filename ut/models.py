from django.db import models


class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=155)


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
    weight = models.DecimalField(max_digits=30, decimal_places=3)
    weight_netto = models.DecimalField(max_digits=30, decimal_places=3)
    length_box = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    width_box = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    height_box = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    barcode_block = models.CharField(max_length=155, null=True, blank=True)
    barcode_box = models.CharField(max_length=155, null=True, blank=True)
    barcode_pkge = models.CharField(max_length=155, null=True, blank=True)


class Agent(models.Model):
    program_id = models.IntegerField(verbose_name="ИД Программы")
    id = models.IntegerField(primary_key=True, verbose_name="ИД")
    item_name = models.CharField(max_length=255, verbose_name="")
    level_id = models.IntegerField(verbose_name="")
    is_active = models.BooleanField(verbose_name="")
    comment = models.CharField(max_length=255, verbose_name="", null=True, blank=True)
    date_create = models.DateTimeField(verbose_name="", null=True, blank=True)
    date_update = models.DateTimeField(verbose_name="", null=True, blank=True)
    group_id = models.IntegerField(verbose_name="", )
    contact_phone = models.CharField(max_length=155, verbose_name="", null=True, blank=True)
    contact_face = models.CharField(max_length=155, verbose_name="", null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="", null=True, blank=True)
    agent_dovoz_id = models.IntegerField(verbose_name="", )
    agent_id = models.IntegerField(verbose_name="", )
    ex_id = models.CharField(max_length=255, verbose_name="", null=True, blank=True)


class Invoice(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ИД')
    program_id = models.IntegerField(verbose_name="ИД Программы")
    acs_number = models.CharField(max_length=155, verbose_name="Номер накладной")
    is_active = models.BooleanField(verbose_name="Активный")
    date_doc = models.DateTimeField(verbose_name="Дата документа")
    is_entry = models.BooleanField(verbose_name="Проведен")
    invoice_type_id = models.IntegerField(verbose_name="Тип операции")
    from_id = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='invoice_from', verbose_name="От кого")
    to_id = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='invoice_to', verbose_name="Кому")
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='invoice', verbose_name="ИД Агента")
    date_create = models.DateTimeField(verbose_name="Дата создания")
    date_update = models.DateTimeField(verbose_name="Дата редактирования", null=True, blank=True)
    comment = models.CharField(max_length=155, verbose_name="Комментарий", null=True, blank=True)
    user_create = models.CharField(max_length=155, verbose_name="Пользователь_создан")
    user_update = models.CharField(max_length=155, verbose_name="Пользователь_изменен", null=True, blank=True)
    delivery = models.BooleanField(verbose_name="Признак доставки")
    uid = models.IntegerField(verbose_name="UID")
    order_number = models.CharField(max_length=155, verbose_name="Номер заказа", null=True, blank=True)


class InvoiceBody(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_body', verbose_name="")
    line_id = models.IntegerField()
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='invoice_body_goods', verbose_name="")
    price = models.DecimalField(max_digits=30, decimal_places=2)
    summa = models.DecimalField(max_digits=30, decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField()
