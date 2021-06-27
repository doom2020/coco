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
        and_filter_condition = kwargs['and_filter_condition']
        or_filter_condition = kwargs['or_filter_condition']
        order_by = kwargs['order_by']
        limit = kwargs['limit']
        objs = db_model.query.filter_by(**and_filter_condition).all()
        return objs






