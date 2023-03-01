from core.globals.global_functions import add_months
from datetime import timedelta
# from django.db.models import Q, Max
from hours.models import Hour
from users.models import User


def dict_hourgrid(self):
    allusers = User.objects.filter(is_active=True)
    allusers = allusers.values(
        'id',
        'fullname',
        "mobile",
        'email',
        'userid_hour__id',
        'userid_hour__issuedate',
        'userid_hour__projectid_id',
        'userid_hour__projectid__description',
        'userid_hour__description',
        'userid_hour__amounthours',
    )

    dict_users = dict()
    for user in allusers:
        # Fill the columndata with the dates from the range
        if user['id'] not in dict_users:
            dict_users.update({user['id']: {
                "id": user['id'],
                "fullname": user['fullname'],
                "mobile": user['mobile'],
                "email": user['email'],
                "columndata": {}
            }})
        for columndate, columndatas in self.columndates.items():
            dict_users[user['id']]['columndata'].update({columndate: {}})

    users = User.objects.filter(is_active=True)
    users = users.filter(userid_hour__issuedate__gte=self.startdate, userid_hour__issuedate__lte=self.enddate)
    users = users.values(
        'id',
        'fullname',
        "mobile",
        'email',
        'userid_hour__id',
        'userid_hour__issuedate',
        'userid_hour__projectid_id',
        'userid_hour__projectid__description',
        'userid_hour__description',
        'userid_hour__amounthours',
    )
    users = users.order_by("fullname")

    for user in users:
        dict_users[user['id']]['columndata'][format(user['userid_hour__issuedate'], "%d-%m-%Y")].update({
            user['userid_hour__id']: {
                "userid_hour__issuedate": user['userid_hour__issuedate'],
                "userid_hour__projectid_id": user['userid_hour__projectid_id'],
                "userid_hour__projectid__description": user['userid_hour__projectid__description'],
                "userid_hour__description": user['userid_hour__description'],
                "userid_hour__amounthours": user['userid_hour__amounthours'],
            },
        })
    return dict_users
