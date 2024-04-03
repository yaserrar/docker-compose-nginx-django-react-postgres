from django.core.files.storage import FileSystemStorage
import jwt
from datetime import datetime, timedelta
from django.conf import settings


class CustomFileSystemStorage(FileSystemStorage):
    def url(self, name):
        url = super().url(name)
        expiration_time = datetime.utcnow() + timedelta(minutes=5)
        token = jwt.encode({"exp": expiration_time}, settings.SECRET_KEY, algorithm="HS256")

        if "?" in url:
            url += f"&token={token}"
        else:
            url += f"?token={token}"
        return url
