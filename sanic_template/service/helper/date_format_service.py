from datetime import datetime, date

from sanic_template.consts import BASE_DATETIME_FORMAT, BASE_DATE_FORMAT

from sanic_template.utils.core import Singleton


class DateFormatService(Singleton):

    def format_datetime(self, date_time: datetime) -> str:
        return date_time.strftime(BASE_DATETIME_FORMAT)

    def format_date(self, date_obj: date) -> str:
        return date_obj.strftime(BASE_DATE_FORMAT)


date_format_service = DateFormatService()
