from rest_framework.exceptions import APIException


class PropertyNotFound (APIException):
    status_code = 404
    defsult_detail = 'The Request Property Does Not Exist'
