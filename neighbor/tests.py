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

    def test_update_neighborhood
        