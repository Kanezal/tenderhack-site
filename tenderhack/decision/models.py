from django.db import models
from django.core.validators import RegexValidator
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
    law = models.CharField(max_length=255, choices=LAW_CHOICES, null=True, blank=True)
    procurement_method = models.CharField(max_length=255, choices=PROCUREMENT_METHOD_CHOICES, null=True, blank=True)
    conclusion_basis = models.CharField(max_length=255, choices=CONCLUSION_BASIS_CHOICES, null=True, blank=True)
    number = models.TextField(null=True, blank=True)

    # validity_period_start = models.DateField(null=True, blank=True)
    # validity_period_end = models.DateField(null=True, blank=True)
    
    contract_subject = models.TextField(null=True, blank=True)
    conclusion_place = models.CharField(max_length=255, null=True, blank=True) # TODO: сделать выбор адреса реальный

    procurement_id = models.CharField(
        max_length=36,
        validators=[RegexValidator(r'^\d+$', 'Введите число.')],
        null=True, blank=True
    )
    financing_source = models.CharField(max_length=255, choices=FINANCING_SOURCE_CHOICES, null=True, blank=True)
    
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    advance = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    customer_details = models.ForeignKey('tender_auth.TenderUser', on_delete=models.CASCADE, related_name='customer_details', blank=True)
    performer_details = models.ForeignKey('tender_auth.TenderUser', on_delete=models.CASCADE, related_name='performer_details', blank=True)

    signer = models.TextField(null=True, blank=True)
    general_info = models.TextField(null=True, blank=True)
    bank_details = models.TextField(null=True, blank=True)

    contact_details_phone = models.CharField(max_length=15, null=True, blank=True)
    contact_details_email = models.EmailField(null=True, blank=True)

    # delivery_info = models.TextField(null=True, blank=True)

    records_history = HistoricalRecords()

    is_being_edited = models.BooleanField(default=False)
    last_edited_by = models.ForeignKey('tender_auth.TenderUser', on_delete=models.SET_NULL, null=True, blank=True)


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
