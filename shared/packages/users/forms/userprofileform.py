modelname = "User"


class Userprofileform:
    def __init__(self, request):
        self.password = {
            "required": True,
            'autofocus': 'autofocus',
        }
