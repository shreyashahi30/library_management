from app.models.member import member_model

class MemberService:
    @staticmethod
    def create_member(name, email):
        return member_model.create({"name": name, "email": email})

    @staticmethod
    def get_all_members():
        return member_model.get_all()

    @staticmethod
    def get_member(member_id):
        return member_model.get_by_id(member_id)

    @staticmethod
    def update_member(member_id, name, email):
        return member_model.update(member_id, {"name": name, "email": email})

    @staticmethod
    def delete_member(member_id):
        return member_model.delete(member_id)

