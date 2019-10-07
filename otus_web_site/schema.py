import graphene
from online_school.schema import Query as OnlineSchoolQuery


class Query(OnlineSchoolQuery, graphene.ObjectType, ):
    pass


schema = graphene.Schema(query=Query)
