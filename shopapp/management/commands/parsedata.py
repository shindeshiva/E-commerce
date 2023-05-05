import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from shopapp.models import information, customerinfo

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        information.objects.all().delete()
        customerinfo.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/shopapp/csvfile/shoppinglist.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                table1 = information.objects.create(
                Serialno = row[0],
                Product = row[2],
                Quantityordered = row[3],
                Purchaseaddresss = row[6],
                City = row[7]
                )
                table1.save()
        

        with open(str(base_dir) + '/shopapp/csvfile/shoppinglist.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                table2 = customerinfo.objects.create(
                Serialno = row[0],
                Orderid = information.objects.filter(Serialno = row[0]).first(),
                Priceeach = row[4],
                Orderdate = row[5],
                Custid = row[8]
                )
                table2.save()
        print("data parsed successfully")