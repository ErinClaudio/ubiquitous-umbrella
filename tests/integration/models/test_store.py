from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [], "error message")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'), 'found Store with the name test')

            store.save_to_db()

            self.assertIsNone(StoreModel.find_by_name('test'), 'did not find a store with name test')

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'),
                              'found a store with name "test" after having been deleted from  database')

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()




            expected = {
                'name': 'test',
                'items': [{'name': 'test_item',
                           'price': 19.99}]

            }

            self.assertDictEqual(store.json(), expected)











        with self.app_context():
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item iwth name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relatioship(self):
        with self.app_context():
            store = StoreModel('Test Store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'Test Store')





