import pyinputplus as pyip
import random, time

score = 0

for i in range(10):
    first_number = random.randrange(0,9)
    second_number = random.randrange(0,9)
    result = first_number*second_number
    try:
        if pyip.inputInt("This is {2} question. What's {0} times {1} \n".format(first_number,second_number,i+1),
                         timeout=8,limit=3,allowRegexes=['^%s$' % (first_number * second_number)],blockRegexes=[('.*', 'Not correct')]) == result:
            print('Correct!')
            score += 1
    except (pyip.TimeoutException):
        print("you ran out of time for this question!")
    except (pyip.RetryLimitException):
        print("Too many tries! next question.")
    time.sleep(1)

print('Your score is {0}/10'.format(score))