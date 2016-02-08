"""
extension wtform validators
"""
from gdg_flask import db
from wtforms import ValidationError


class DuplicateCheck(object):
    def __init__(self, table_name, column_name, message=None):
        if not message:
            message = u'field is duplicated True'
        self.table_name = table_name
        self.column_name = column_name
        self.message = message

    def __call__(self, form, field):
        sql_query = "SELECT %s FROM %s WHERE %s='%s'" % (field.id, self.table_name, self.column_name, field.data)

        # sql proxy
        sql_prx = db.engine.execute(sql_query)
        sql_result = sql_prx.fetchall()

        sql_prx.close()

        if sql_result:
            # 존재하면
            raise ValidationError(self.message)

duplicate_check = DuplicateCheck
