from sqlalchemy import or_, and_


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
        desc = kwargs.get('desc', '')
        and_query_condition = kwargs.get('and_query_condition', {})
        or_query_condition = kwargs.get('or_query_condition', {})
        query_content = None
        if and_query_condition and or_query_condition:
            query_content = db_model.query.filter_by(and_(and_(**and_query_condition), or_(**or_query_condition)))
        elif and_query_condition:
            query_content = db_model.query.filter_by(**and_query_condition)
        elif or_query_condition:
            query_content = db_model.query.filter_by(or_(**or_query_condition))
        if group_by:
            query_content = query_content.group_by(group_by)
        if order_by:
            if desc:
                query_content = query_content.order_by(desc(order_by))
            else:
                query_content = query_content.order_by(order_by)
        if limit:
            query_content = query_content.limit(limit)
        if offset:
            query_content = query_content.offset(offset)
        if query_type == 'all':
            query_obj = query_content.all()
        elif query_type == 'first':
            query_obj = query_content.first()
        elif query_type == 'one':
            query_obj = query_content.one()
        return query_obj
