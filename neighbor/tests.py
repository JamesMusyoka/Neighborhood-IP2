from django.test import TestCase
from .models import *

class NeighborhoodTestClass(TestCase):

    def setUp(self):
        self.kingkong= Neighborhood(neighborhood_name = 'Kingkong', neighborhood_location = 'Westlands')

    def test_instance(self):
        self.assertTrue(isinstance(self.kingkong, Neighborhood))

    def test_save_method(self):
        self.kingkong.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)

    def test_create_neighborhood(self):
        self.kingkong.create_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)

    def test_find_neighborhood(self):
        self.kingkong.find_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)

    def test_update_neighborhood(self):
        self.kingkong.update_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertFalse(len(neighborhood) > 0)

    def update_occupands(self):
        self.kingkong.update_occupands()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)

    def test_delete_neighborhood(self):
        self.kingkong.delete_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)
        

class BusinessTestClasss(TestCase):

    def setUp(self):
        self.newgeneration= Business(business_name = 'Newgeneration')

    def test_instance(self):
        self.assertTrue(isinstance(self.newgeneration, Business))


    def test_save_method(self):
        self.newgeneration.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    # def test_create_business(self):
    #     self.newgeneration.create_neighborhood()
    #     business = Business.objects.all()
    #     self.assertTrue(len(business) == 1)