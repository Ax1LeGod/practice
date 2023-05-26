from datetime import datetime

class ResponseFactory(object):


    @staticmethod
    def model_to_dict(obj, *ignore:str):
        data = dict()
        for c in obj.__table__.columns:
            '''obj继承db.model类，都有table属性'''
            if c.name in ignore:
                '''如果字段忽略，则不转换'''
                continue

            val = getattr(obj, c.name)
            '''返回obj中c.name'''
            if isinstance(val, datetime):
                data[c.name]=val.strftime('%Y-%m-%d %H:%M:%S')
            else:
                data[c.name] = val
        return data


    @staticmethod
    def model_to_list(data:list, *ignore:str):
        return [ResponseFactory.model_to_dict(x, *ignore)for x in data]


