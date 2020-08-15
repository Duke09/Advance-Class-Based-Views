import graphene
from graphene_django import DjangoObjectType

from ..models import Question, Choice

# Chustom Object Type
'''
class QuestionType(graphene.ObjectType):
    question_text = graphene.String()
    pub_date = graphene.types.datetime.DateTime()
'''

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice

class CustomType(graphene.ObjectType):
    message = graphene.String()
    question_str = graphene.String()
    question = graphene.Field(QuestionType)

    def resolve_question_str(self, infor, **kwargs):
        return self.question.__str__()