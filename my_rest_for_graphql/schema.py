import graphene
import my_rest_for_graphql.simple_api.schema
class Query(my_rest_for_graphql.simple_api.schema.Query, graphene.ObjectType):
  # This class will inherit from multiple Queries
  # as we begin to add more apps to our project
  pass

schema = graphene.Schema(query=Query)