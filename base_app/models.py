from django.db import models
from django.urls import reverse_lazy


class Filial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, verbose_name="URL")
    url_pg = models.CharField(max_length=255, verbose_name="Строка подключения к PG")
    url_wms = models.CharField(max_length=255, verbose_name="Название базы WMS")
    prog_id = models.IntegerField(default=0, verbose_name="Код программы Логистика")
    position = models.IntegerField(default=0, verbose_name="Позиция в меню")
    as_active = models.BooleanField(default=True, verbose_name="Признак активности")

    def __str__(self):
        return self.name

    def get_home_url(self):
        return reverse_lazy(f"{self.slug}:{self.slug}_home")

    class Meta:
        ordering = ('position',)
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Наименование")
    filial = models.ManyToManyField(Filial, related_name='menus', verbose_name="Филиал")
    slug = models.SlugField(max_length=255, verbose_name="URL")
    position = models.IntegerField(default=0, verbose_name="Позиция в меню")
    as_active = models.BooleanField(default=True, verbose_name="Признак активности")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('menu-detail', kwargs={'slug': self.slug})

    def get_home_url(self):
        return reverse_lazy(f"{self.filial.slug}:{self.slug}")

    class Meta:
        ordering = ('position',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Contracts(models.Model):
    id = models.AutoField(primary_key=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name='contracts', verbose_name="Филиал")
    name = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, verbose_name="URL")
    path_saved_order = models.CharField(max_length=255, verbose_name="Папка сохранения заявок XML")
    position = models.IntegerField(default=0, verbose_name="Позиция в меню")
    as_active = models.BooleanField(default=True, verbose_name="Признак активности")
    path_saved_reports = models.CharField(max_length=255, verbose_name="Папка сохранения отчетов")
    id_groups_goods = models.IntegerField(default=0, verbose_name="Код папки товаров")
    id_groups_vod = models.IntegerField(default=0, verbose_name="Код папки водителей, для ОК")
    id_groups_vod_tls = models.IntegerField(default=0, verbose_name="Код папки водителей ТЛС, для ОК")
    id_postav = models.IntegerField(default=0, verbose_name="Код поставщика", null=True, blank=True)
    id_client = models.IntegerField(default=0, verbose_name="Код клиента", null=True, blank=True)
    id_sklad = models.IntegerField(default=0, verbose_name="Код склада", null=True, blank=True)
    id_agent = models.IntegerField(default=0, verbose_name="Код агента", null=True, blank=True)
    delivery_type = models.IntegerField(default=2, verbose_name="Тип доставки")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('operations-detail', kwargs={'slug': self.slug})

    def get_home_url(self):
        return reverse_lazy(f'operations', kwargs={'_contract_slug': self.slug, '_filial_slug': self.filial.slug})

    class Meta:
        ordering = ('position',)
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'


class SubMenu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Наименование")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_submenu', verbose_name="Меню")
    contract = models.ManyToManyField(Contracts, related_name='menu_filial', verbose_name="Филиал", null=True, blank=True)
    slug = models.SlugField(max_length=255, verbose_name="URL")
    position = models.IntegerField(default=0, verbose_name="Позиция в меню")
    as_active = models.BooleanField(default=True, verbose_name="Признак активности")

    def __str__(self):
        return self.name

    def get_home_url(self):
        return reverse_lazy(f'{self.menu.filial.slug}:{self.slug}')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
