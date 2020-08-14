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

class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType, id=graphene.Int())

    def resolve_all_questions(self, info):
        return Question.objects.all()
    
    def resolve_question(self, info, **kwargs):
        qid = kwargs.get('id')

        if qid is not None:
            return Question.objects.get(pk=qid)
        return None

schema = graphene.Schema(query=Query)
