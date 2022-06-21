from django.shortcuts import render


# Create your views here.
def home_work(request):
    return render(request, "home.html")


secret_num = ['1', '2', '3', '4']


def checking(self):
    if len(self.user_numbers) > 4 or len(self.user_numbers) < 4:
        return 'Wrong number of values'
    elif len(set(self.user_numbers)) < 4:
        return 'Values must not be repeated'
    try:
        for i in range(len(self.user_numbers)):
            if int(self.user_numbers[i]) < 1 or int(self.user_numbers[i]) > 9:
                return 'Enter values from 1 to 9'
    except ValueError:
        return "Enter only numbers"


def result_game(self):
    count_bulls = 0
    count_cows = 0
    for i in range(len(self.user_numbers)):
        if self.user_numbers[i] == self.secret_num[i]:
            count_bulls += 1
        elif self.user_numbers[i] in self.secret_num:
            count_cows += 1
    if count_bulls == 4:
        return 'Your Win!'
    elif count_bulls or count_cows:
        return f'You got {count_bulls} bulls and {count_cows} cows'
    else:
        'No identical values'
