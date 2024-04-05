from django.shortcuts import render

# Create your views here.
def spotify_login(request):
    return render(request, 'login.html')

def quiz(request):
    questions = [
        {
            'question': 'Question 1: Select your favourite music genre',
            'choices': ['Electronic/Dance', 'Pop', 'Hip Hop', 'Metal', 'Country', 'Jazz', 'K-Pop', 'Classical']
        },
        {
            'question': 'Question 2: Do you have a preference for speed in your music?',
            'choices': ['No preference', '80-89bpm', '90-99bpm', '100-109bpm', '110-119bpm', '120-129bpm', '130-139bpm', '140-149bpm', '150-159bpm', '160-169bpm', '170-179bpm']
        },
        {
            'question': 'Question 3: What is your preference for energy in your music rated from 0 to 1. 0 being low energy and 1 being high energy.',
            'choices': ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
        },
        {
            'question': 'Question 4: Do you prefer music with lyrics or without? Select an option from 0 to 1 with 1 being a song with no lyrics and 0 being a song with lyrics throughout.',
            'choices': ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
        },
        {
            'question': 'Question 5: Do you prefer positive music? Select an option from 0 to 1 with 1 beign a song with positive sound and 0 being a song with negative sounds.',
            'choices': ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
        }
    ]
    context = {
        'questions': questions,
    }
    return render(request, 'quiz.html', context)
