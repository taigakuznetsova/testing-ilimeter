from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View
from .models import (
    Interactive, TextQuestion, TextAnswer, NumberQuestion, NumberAnswer,
    AudienceQA, Networking, StarVotingQuestion, StarVote, SingleChoiceQuestion,
    SingleChoiceAnswer, MultipleChoiceQuestion, MultipleChoiceAnswer, Survey,
    SurveyQuestion, SurveyAnswer, Quiz, QuizAnswer
)
from .forms import (
    InteractiveForm, TextQuestionForm, TextAnswerForm, NumberQuestionForm,
    NumberAnswerForm, AudienceQAForm, NetworkingForm, StarVotingQuestionForm,
    StarVoteForm, SingleChoiceQuestionForm, SingleChoiceAnswerForm,
    MultipleChoiceQuestionForm, MultipleChoiceAnswerForm, SurveyForm,
    SurveyQuestionForm, SurveyAnswerForm, QuizForm, QuizAnswerForm
)


# Interactive Views
class InteractiveCreateView(CreateView):
    model = Interactive
    form_class = InteractiveForm
    template_name = 'interactive_elements/interactive_create.html'
    success_url = reverse_lazy('interactive_list')


class InteractiveUpdateView(UpdateView):
    model = Interactive
    form_class = InteractiveForm
    template_name = 'interactive_elements/interactive_update.html'
    success_url = reverse_lazy('interactive_list')


class InteractiveDetailView(DetailView):
    model = Interactive
    template_name = 'interactive_elements/interactive_detail.html'


class InteractiveListView(ListView):
    model = Interactive
    template_name = 'interactive_elements/interactive_list.html'
    context_object_name = 'interactives'


# Text Question Views
class TextQuestionCreateView(CreateView):
    model = TextQuestion
    form_class = TextQuestionForm
    template_name = 'interactive_elements/text_question_create.html'
    success_url = reverse_lazy('interactive_list')

    def form_valid(self, form):
        # Создаем интерактив
        interactive = Interactive.objects.create(
            meeting=form.cleaned_data['meeting'],
            title=form.cleaned_data['title'],
            type='text_question',
            description=form.cleaned_data['description']
        )
        form.instance.interactive = interactive
        return super().form_valid(form)


class TextQuestionUpdateView(UpdateView):
    model = TextQuestion
    form_class = TextQuestionForm
    template_name = 'interactive_elements/text_question_update.html'
    success_url = reverse_lazy('interactive_list')


class TextQuestionDetailView(DetailView):
    model = TextQuestion
    template_name = 'interactive_elements/text_question_detail.html'


class TextAnswerCreateView(CreateView):
    model = TextAnswer
    form_class = TextAnswerForm
    template_name = 'interactive_elements/text_question_answer.html'
    success_url = reverse_lazy('interactive_list')


# Number Question Views
class NumberQuestionCreateView(CreateView):
    model = NumberQuestion
    form_class = NumberQuestionForm
    template_name = 'interactive_elements/number_question_create.html'
    success_url = reverse_lazy('interactive_list')

    def form_valid(self, form):
        # Создаем интерактив
        interactive = Interactive.objects.create(
            meeting=form.cleaned_data['meeting'],
            title=form.cleaned_data['title'],
            type='number_question',
            description=form.cleaned_data['description']
        )
        form.instance.interactive = interactive
        return super().form_valid(form)


class NumberQuestionUpdateView(UpdateView):
    model = NumberQuestion
    form_class = NumberQuestionForm
    template_name = 'interactive_elements/number_question_update.html'
    success_url = reverse_lazy('interactive_list')


class NumberQuestionDetailView(DetailView):
    model = NumberQuestion
    template_name = 'interactive_elements/number_question_detail.html'


class NumberAnswerCreateView(CreateView):
    model = NumberAnswer
    form_class = NumberAnswerForm
    template_name = 'interactive_elements/number_question_answer.html'
    success_url = reverse_lazy('interactive_list')


# Audience QA Views
class AudienceQACreateView(CreateView):
    model = AudienceQA
    form_class = AudienceQAForm
    template_name = 'interactive_elements/audience_qa_form.html'
    success_url = reverse_lazy('interactive_list')


# Networking Views
class NetworkingCreateView(CreateView):
    model = Networking
    form_class = NetworkingForm
    template_name = 'interactive_elements/networking_form.html'
    success_url = reverse_lazy('interactive_list')


# Star Voting Views
class StarVotingQuestionCreateView(CreateView):
    model = StarVotingQuestion
    form_class = StarVotingQuestionForm
    template_name = 'interactive_elements/star_voting_question_create.html'
    success_url = reverse_lazy('interactive_list')

    def form_valid(self, form):
        # Создаем интерактив
        interactive = Interactive.objects.create(
            meeting=form.cleaned_data['meeting'],
            title=form.cleaned_data['title'],
            type='star_voting',
            description=form.cleaned_data['description']
        )
        form.instance.interactive = interactive
        return super().form_valid(form)


class StarVotingQuestionUpdateView(UpdateView):
    model = StarVotingQuestion
    form_class = StarVotingQuestionForm
    template_name = 'interactive_elements/star_voting_question_update.html'
    success_url = reverse_lazy('interactive_list')


class StarVotingQuestionDetailView(DetailView):
    model = StarVotingQuestion
    template_name = 'interactive_elements/star_voting_question_detail.html'


class StarVoteCreateView(CreateView):
    model = StarVote
    form_class = StarVoteForm
    template_name = 'interactive_elements/star_vote_form.html'
    success_url = reverse_lazy('interactive_list')


# Single Choice Views
class SingleChoiceQuestionCreateView(CreateView):
    model = SingleChoiceQuestion
    form_class = SingleChoiceQuestionForm
    template_name = 'interactive_elements/single_choice_question_create.html'
    success_url = reverse_lazy('interactive_list')

    def form_valid(self, form):
        interactive = Interactive.objects.create(
            meeting=form.cleaned_data['meeting'],
            title=form.cleaned_data['title'],
            type='single_choice',
            description=form.cleaned_data['description']
        )
        form.instance.interactive = interactive
        options = self.request.POST.getlist('options')
        form.instance.options = options

        return super().form_valid(form)


class SingleChoiceQuestionUpdateView(UpdateView):
    model = SingleChoiceQuestion
    form_class = SingleChoiceQuestionForm
    template_name = 'interactive_elements/single_choice_question_update.html'
    success_url = reverse_lazy('interactive_list')


class SingleChoiceQuestionDetailView(DetailView):
    model = SingleChoiceQuestion
    template_name = 'interactive_elements/single_choice_question_detail.html'


class SingleChoiceAnswerCreateView(CreateView):
    model = SingleChoiceAnswer
    form_class = SingleChoiceAnswerForm
    template_name = 'interactive_elements/single_choice_answer_form.html'
    success_url = reverse_lazy('interactive_list')


# Multiple Choice Views
class MultipleChoiceQuestionCreateView(CreateView):
    model = MultipleChoiceQuestion
    form_class = MultipleChoiceQuestionForm
    template_name = 'interactive_elements/multiple_choice_question_create.html'
    success_url = reverse_lazy('interactive_list')

    def form_valid(self, form):
        interactive = Interactive.objects.create(
            meeting=form.cleaned_data['meeting'],
            title=form.cleaned_data['title'],
            type='multiple_choice',
            description=form.cleaned_data['description']
        )
        form.instance.interactive = interactive
        options = self.request.POST.getlist('options')
        form.instance.options = options

        return super().form_valid(form)


class MultipleChoiceQuestionUpdateView(UpdateView):
    model = MultipleChoiceQuestion
    form_class = MultipleChoiceQuestionForm
    template_name = 'interactive_elements/multiple_choice_question_update.html'
    success_url = reverse_lazy('interactive_list')


class MultipleChoiceQuestionDetailView(DetailView):
    model = MultipleChoiceQuestion
    template_name = 'interactive_elements/multiple_choice_question_detail.html'


class MultipleChoiceAnswerCreateView(CreateView):
    model = MultipleChoiceAnswer
    form_class = MultipleChoiceAnswerForm
    template_name = 'interactive_elements/multiple_choice_answer_form.html'
    success_url = reverse_lazy('interactive_list')


# Survey Views
class SurveyCreateAndAddQuestionView(View):
    template_name = 'interactive_elements/survey_create_and_add_question.html'

    def get(self, request, *args, **kwargs):
        form = SurveyForm()
        question_form = SurveyQuestionForm()
        questions = request.session.get('survey_questions', [])
        return render(request, self.template_name, {
            'form': form,
            'question_form': question_form,
            'questions': questions
        })

    def post(self, request, *args, **kwargs):
        if 'add_question' in request.POST:
            return self.add_question(request)
        elif 'create_survey' in request.POST:
            return self.create_survey(request)
        else:
            return self.get(request)

    def add_question(self, request):
        question_form = SurveyQuestionForm(request.POST)
        if question_form.is_valid():
            question_text = question_form.cleaned_data['question_text']
            questions = request.session.get('survey_questions', [])
            questions.append(question_text)
            request.session['survey_questions'] = questions
        return redirect('survey_create')

    def create_survey(self, request):
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.interactive = Interactive.objects.create(
                meeting=form.cleaned_data['meeting'],
                title=form.cleaned_data['title'],
                type='survey',
                description=form.cleaned_data['description']
            )
            survey.save()
            questions = request.session.get('survey_questions', [])
            for question_text in questions:
                SurveyQuestion.objects.create(
                    survey=survey,
                    question_text=question_text
                )
            request.session['survey_questions'] = []
            return redirect(reverse_lazy('interactive_list'))
        else:
            question_form = SurveyQuestionForm()
            questions = request.session.get('survey_questions', [])
            return render(request, self.template_name, {
                'form': form,
                'question_form': question_form,
                'questions': questions
            })


class SurveyQuestionUpdateView(UpdateView):
    model = SurveyQuestion
    form_class = SurveyQuestionForm
    template_name = 'interactive_elements/survey_question_update.html'
    success_url = reverse_lazy('interactive_list')


class SurveyQuestionDetailView(DetailView):
    model = SurveyQuestion
    template_name = 'interactive_elements/survey_question_detail.html'


class SurveyAnswerCreateView(CreateView):
    model = SurveyAnswer
    form_class = SurveyAnswerForm
    template_name = 'interactive_elements/survey_answer_form.html'
    success_url = reverse_lazy('interactive_list')


# Quiz Views
class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'interactive_elements/quiz_create.html'
    success_url = reverse_lazy('interactive_list')

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.interactive = Interactive.objects.create(
            meeting=form.cleaned_data['meeting'],
            title=form.cleaned_data['title'],
            type='quiz',
            description=form.cleaned_data['description']
        )
        quiz.save()
        return super().form_valid(form)


class QuizUpdateView(UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'interactive_elements/quiz_form.html'
    success_url = reverse_lazy('interactive_list')


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'interactive_elements/quiz_detail.html'


class QuizAnswerCreateView(CreateView):
    model = QuizAnswer
    form_class = QuizAnswerForm
    template_name = 'interactive_elements/quiz_answer_form.html'
    success_url = reverse_lazy('interactive_list')