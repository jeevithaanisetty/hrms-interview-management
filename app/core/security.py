class MockUser:
    def __init__(self):
        self.id="00000000-0000-0000-000000000001"    # system / default UUID format 
        self.role="admin"
        self.email="admin@gmail.com"

def get_mock_user():
        return MockUser()