from django.db import models
from django.core.validators import RegexValidator
from approval.models import ApprovableModelMixin, ApprovableManager
from simple_history.models import HistoricalRecords

LAW_CHOICES = [
    ('44-FZ', '44-ФЗ'),
    ('223-FZ', '223-ФЗ'),
]

PROCUREMENT_METHOD_CHOICES = [
    ('single_supplier', 'Единственный поставщик'),
]

FINANCING_SOURCE_CHOICES = [
    ('budget', 'Бюджетные средства'),
    ('non_budget', 'Небюджетные средства'),
    ('oms', 'Средства ОМС'),
]

CONCLUSION_BASIS_CHOICES = [
    ('c4p1', 'п. 4 ч. 1 ст. 93 Закупка объемом до 600 тысяч рублей'), 
    ('c5p1', 'п. 5 ч. 1 ст. 93 Закупка объёмом до 600 тысяч рублей')
]

class MainContract(models.Model):
    law = models.CharField(max_length=255, choices=LAW_CHOICES)
    procurement_method = models.CharField(max_length=255, choices=PROCUREMENT_METHOD_CHOICES)
    conclusion_basis = models.CharField(max_length=255, choices=CONCLUSION_BASIS_CHOICES)
    number = models.TextField()

    validity_period_start = models.DateField()
    validity_period_end = models.DateField()
    
    contract_subject = models.TextField()
    conclusion_place = models.CharField(max_length=255) # TODO: сделать выбор адреса реальный

    procurement_id = models.CharField(
        max_length=36,
        validators=[RegexValidator(r'^\d+$', 'Введите число.')]
    )
    financing_source = models.CharField(max_length=255, choices=FINANCING_SOURCE_CHOICES)
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    advance = models.DecimalField(max_digits=12, decimal_places=2)
    
    customer_details = models.ForeignKey('tender_auth.TenderUser', on_delete=models.CASCADE, related_name='customer_details')
    performer_details = models.ForeignKey('tender_auth.TenderUser', on_delete=models.CASCADE, related_name='performer_details')

    signer = models.TextField()
    general_info = models.TextField()
    bank_details = models.TextField()

    contact_details_phone = models.CharField(max_length=15)
    contact_details_email = models.EmailField()

    delivery_info = models.TextField()

    records_history = HistoricalRecords()


class Specification(models.Model):
    main_contract = models.ForeignKey(MainContract, on_delete=models.CASCADE, related_name='specifications')

    name = models.CharField(max_length=255)
    okpd2 = models.CharField(max_length=255)
    price_with_vat = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    vat = models.DecimalField(max_digits=5, decimal_places=2)
    total_with_vat = models.DecimalField(max_digits=10, decimal_places=2)


class SupplyConfig(models.Model):
   main_contract = models.ForeignKey(MainContract, on_delete=models.CASCADE, related_name='supply_configs')

   address = models.CharField(max_length=200)
   delivery_term = models.CharField(max_length=200)
   product_name = models.CharField(max_length=200)
   price_with_vat = models.DecimalField(max_digits=10, decimal_places=2)
   quantity = models.IntegerField()
   total_with_vat = models.DecimalField(max_digits=10, decimal_places=2)
