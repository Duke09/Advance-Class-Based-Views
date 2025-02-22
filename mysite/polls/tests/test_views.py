from django.test import TestCase, RequestFactory, Client

from django.urls import reverse

from model_mommy import mommy

from ..views import VoteView
from ..models import Choice

class TestVoteViewIntegration(TestCase):
    def setUp(self):
        self.client = Client()
        self.question_model = mommy.make('polls.Question')
        self.choice_models = mommy.make(
            'polls.Choice',
            question=self.question_model,
            _quantity=3
        )

    def test_post_success(self):
        choice = self.choice_models[0]
        response = self.client.post(
            reverse(
                'polls:vote',
                kwargs={
                    'pk': choice.question.id
                }
            ),
            {
                'choice': choice.id
            },
            follow=True
        )
        self.assertIn(302, response.redirect_chain[0])
        self.assertTemplateUsed(response, 'polls/results.html')

    def test_post_failure(self):
        choice = self.choice_models[0]
        response = self.client.post(
            reverse(
                'polls:vote',
                kwargs={
                    'pk': choice.question.id
                }
            ),
            follow=True
        )
        self.assertIn(302, response.redirect_chain[0])
        self.assertTemplateUsed(response, 'polls/detail.html')


class TestVote(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.question_model = mommy.make('polls.Question')
        self.choice_models = mommy.make(
            'polls.Choice',
            question=self.question_model,
            _quantity=3
        )
    
    def test_get_queryset(self):
        choice = self.choice_models[0]
        view = VoteView()
        queryset = view.get_queryset(choice.pk)
        self.assertEquals(queryset.choice_text, choice.choice_text)

    def test_post_votes(self):
        choice = self.choice_models[1]
        votes = choice.votes + 1
        # RequestFactory just fakes a django request
        request = self.factory.post(
            'some-fake/url/',
            data={'choice': choice.id}
        )
        view = VoteView.as_view()
        response = view(request, pk=choice.question.id)
        new_votes = Choice.objects.get(pk=choice.id).votes
        self.assertEquals(votes, new_votes)

    def test_redirect_fail(self):
        choice = self.choice_models[2]
        request = self.factory.post(
            'some-fake/url/',
            data={'choice': 500}
        )
        view = VoteView.as_view()
        response = view(request, pk=choice.question.id)
        self.assertEquals(response.status_code, 302)