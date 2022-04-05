import graphene
import djangoGraphql.api.schema


class Query(djangoGraphql.api.schema.Query, graphene.ObjectType):
    pass


class Mutation(djangoGraphql.api.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
