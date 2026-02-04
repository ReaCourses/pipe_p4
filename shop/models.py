from django.db import models

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование коллекции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Clothes(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование позиции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=36, verbose_name='Размер')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    def __str__(self):
        return f"{self.name} - ({self.price} рублей.)"
    
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'



class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY = [
        (SHOP, 'Самовывоз'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_surname = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.TextField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Комментарий')
    delivery_address = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Тип доставки')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения заказа')

    clothes = models.ManyToManyField('Clothes', through='Pos_order', verbose_name='Товар')

    def __str__(self):
        return f'#{self.pk} - {self.buyer_name} {self.buyer_surname} {self.buyer_firstname} ({self.date_create})'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.PROTECT, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

    def __str__(self):
        return f'{self.order.pk} {self.clothes.name} ({self.order.buyer_firstname} {self.order.buyer_name})'
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
