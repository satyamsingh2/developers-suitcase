from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models.owners import Owner
from ..serilizers.owners import OwnerSerializer

# APITestCase -> it allows use of APIClient which allows get, put and other func.

# import pdb   # it is for python debugging (just use pdb.set_trace() method to find problem) on success u can even see response data ,etc. (c + enter -> to exit)


class OwnerTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Owner.objects.create(name="test1", email='test1@example.com', mobile_number='9999999999',
                                          address='test_add')

    # checking create endpoint working fine
    def test_owner_create(self):
        payload = {
            "name": "test2",
            "email": 'test2@example.com',
            "mobile_number": '9999999999',
            'address': 'test_add2',
        }
        response = self.client.post(reverse('owner-list'), payload)
        exists = Owner.objects.filter(name=payload['name']).exists()
        self.assertTrue(exists)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # checking list endpoint
    def test_owner_list(self):
        response = self.client.get(reverse('owner-list'), format='json')
        # pdb.set_trace()
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_owner_detail(self):
        response = self.client.get(reverse('owner-detail', kwargs={'owner_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'test1')

    def test_owner_update(self):
        response = self.client.put(reverse('owner-detail', kwargs={'owner_id': 1}),
                                   {'name': "test1", 'email': 'test1@example.com', 'mobile_number': '9999999999',
                                    'address': 'test_add1'})
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['address'], 'test_add1')

"""
* unit testing (component testing)
** file -> always starts with test
** func -> always starts with test as prefix
** run by python manage.py test 
** verbose mode  python manage.py test -v 2
** particular test package (run) python manage.py test <package-name>
"""