from django.db import models

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    def reserve_table(self):
        self.is_occupied = True
        self.save()

    def free_table(self):
        self.is_occupied = False
        self.save()

    def __str__(self):
        return f"Table {self.table_number}"
    
class Item(models.Model):
    item_name = models.CharField(max_length=300)
    item_price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    status = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    order_status = models.CharField(max_length=10, choices=status, default= 'Pending')

    def add_item(self,item):
        self.item.add(item)
        self.calculate_total()
    
    def remove_item(self,item):
        self.item.remove(item)
        self.calculate_total()

    def calculate_total(self):
        self.total_amount = sum (Item.item_price for item in self.item.all())
        self.save()

    def __str__(self):
        return f"Order {self.id} for  Table {self.table.table_number}"
    

class Payment(models.Model):
    payment_choices= [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),
    ]
    order = models.OneToOneField(Order, on_delete= models.CASCADE)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=payment_choices, default='Card')
    payment_status = models.CharField(max_length=10, default='Pending')

    def process_payment(self):
        self.payment_status = 'Done'
        self.save()

class Manager(models.Model):
    name = models.CharField(max_length=200)

    def assign_table(self, table):
        Table.reserve_table()

    def view_order(self, order):
        return order
    
    def manage_payment(self,payment):
        Payment.process_payment()
    
    def __str__(self):
        return self.name

