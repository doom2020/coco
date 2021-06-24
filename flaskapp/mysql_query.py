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
        model = kwargs['model']
        or_filter_condition = kwargs['or_filter_condition']
        and_filter_condition = kwargs['and_filter_condition']
        order_by = kwargs['order_by']
        limit = kwargs['limit']






