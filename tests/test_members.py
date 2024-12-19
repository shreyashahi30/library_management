import unittest
from app.models.member import member_model
from app.services.member_service import MemberService


class TestMemberService(unittest.TestCase):
    def setUp(self):
        self.service = MemberService
        # Clear the member model before each test
        member_model.data.clear()
        member_model.counter = 1

    def test_create_member(self):
        member = self.service.create_member("John Doe", "john.doe@example.com")
        self.assertEqual(member["name"], "John Doe")
        self.assertEqual(member["email"], "john.doe@example.com")
        self.assertIn("id", member)

    def test_get_all_members(self):
        self.service.create_member("John Doe", "john.doe@example.com")
        self.service.create_member("Jane Smith", "jane.smith@example.com")
        members = self.service.get_all_members()
        self.assertEqual(len(members), 2)

    def test_get_member(self):
        member = self.service.create_member("John Doe", "john.doe@example.com")
        retrieved = self.service.get_member(member["id"])
        self.assertEqual(retrieved["name"], "John Doe")

    def test_update_member(self):
        member = self.service.create_member("John Doe", "john.doe@example.com")
        updated = self.service.update_member(member["id"], "John Updated", "john.updated@example.com")
        self.assertEqual(updated["name"], "John Updated")

    def test_delete_member(self):
        member = self.service.create_member("John Doe", "john.doe@example.com")
        deleted = self.service.delete_member(member["id"])
        self.assertEqual(deleted["name"], "John Doe")
        self.assertIsNone(member_model.get_by_id(member["id"]))


if __name__ == "__main__":
    unittest.main()

