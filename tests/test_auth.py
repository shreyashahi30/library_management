import unittest
from flask import Flask, jsonify
from app.auth import token_required

TOKEN = "secure_token"


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

        @self.app.route("/protected", methods=["GET"])
        @token_required
        def protected():
            return jsonify({"message": "Success"})

        self.client = self.app.test_client()

    def test_valid_token(self):
        response = self.client.get(
            "/protected", headers={"Authorization": TOKEN}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Success")

    def test_invalid_token(self):
        response = self.client.get(
            "/protected", headers={"Authorization": "invalid_token"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()["error"], "Unauthorized")

    def test_missing_token(self):
        response = self.client.get("/protected")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()["error"], "Unauthorized")


if __name__ == "__main__":
    unittest.main()

