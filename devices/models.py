from django.db import models
from fcm.models import AbstractDevice
from kolibree_notif_API.constants import DATABASE_CHOICES

class Device(AbstractDevice):
    account_id = models.IntegerField(db_index=True)
    profile_id = models.IntegerField(unique=True)
    database = models.CharField(choices=DATABASE_CHOICES, max_length=8)

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "profile_id": self.profile_id,
            "database": self.database,
            "reg_id": self.reg_id,
            "dev_id": self.dev_id,
            "name": self.name,
            "is_active": self.is_active
        }
