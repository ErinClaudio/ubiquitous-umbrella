from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        test = UserModel('test_user', 'test_password')

        self.assertEqual(test.username, 'test_user')
        self.assertEqual(test.password, 'test_password')
