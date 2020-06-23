from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        teststore = StoreModel('test')

        self.assertEqual(teststore.name, 'test')

