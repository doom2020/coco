from sqlalchemy import or_, and_


class MysqlQuery(object):

    @classmethod
    def query_all(cls, *args, **kwargs):
        pass

    @classmethod
    def query_first(cls, modal_class):
        return

    @classmethod
    def query_filter(cls, *args, **kwargs):
        """
        位置传参模型
        字典传参,查询条件
        """
        db_model = args[0]
        and_filter_condition = kwargs.get('and_filter_condition', {})
        or_filter_condition = kwargs.get('or_filter_condition', {})
        order_by = kwargs.get('order_by', '')
        limit = kwargs.get('limit', '')
        offset = kwargs.get('offset', '')
        slice = kwargs.get('slice', '')
        query_type = kwargs.get('query_type', 'all')
        group_by = kwargs.get('group_by', '')
        query_content = None
        if and_filter_condition:
            query_content = db_model.query.filter_by(**and_filter_condition)
        if or_filter_condition:
            query_content = db_model.query.filter_by(or_(**or_filter_condition))
        if and_filter_condition and or_filter_condition:
            query_content = db_model.query.filter_by(and_(**and_filter_condition, or_(**or_filter_condition)))
        if order_by:
            pass
        if limit:
            pass
        if offset:
            pass
        if slice:
            pass
        if group_by:
            pass
        if query_type == 'all':
            query_obj = query_content.all()
        elif query_type == 'first':
            query_obj = query_content.first()
        elif query_type == 'one':
            query_obj = query_content.one()
        else:
            query_obj = None
        return query_obj






