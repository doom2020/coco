from sqlalchemy import or_, and_
from flaskapp import db


class MysqlQuery(object):

    @classmethod
    def query_all(cls, *args, **kwargs):
        pass

    @classmethod
    def query_first(cls, modal_class):
        return

    @classmethod
    def query_filter(cls, **kwargs):
        """
        字典传参,查询条件
        """
        db_model = kwargs.get('db_model')
        order_by = kwargs.get('order_by', '')
        limit = kwargs.get('limit', '')
        offset = kwargs.get('offset', '')
        query_type = kwargs.get('query_type', 'all')
        group_by = kwargs.get('group_by', '')
        filter_condition = kwargs.get('filter_condition')
        print(f'查询条件: %s' % filter_condition)
        query_content, query_obj = None, None
        query_content = db_model.query.filter(*filter_condition)
        if group_by:
            query_content = query_content.group_by(group_by)
        if order_by:
            query_content = query_content.order_by(order_by)
        if limit:
            query_content = query_content.limit(limit)
        if offset:
            query_content = query_content.offset(offset)
        print(f'查询语句: %s' % query_content)
        if query_type == 'all':
            query_obj = query_content.all()
        elif query_type == 'first':
            query_obj = query_content.first()
        elif query_type == 'one':
            query_obj = query_content.one()
        print(f'查询结果: %s' % query_obj)
        return query_obj
