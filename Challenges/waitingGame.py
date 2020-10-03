import random
import time

def waiting_game():
    target = random.randint(2,4)
    print('\nYour target time is {} seconds'.format(target))

    input('----Press enter to beging----')
    start=time.perf_counter()

    input('\n....Press enter again after {} seconds...'.format(target))
    elapsed = time.perf_counter() - start

    print('\nElapsed time:{0:.3f} seconds'.format(elapsed))

    if elapsed == target:
        print("Unbelievable!!!")
    elif elapsed < target:
        print('({0:.3f} seconds too fast)'.format(target-elapsed))
    else:
        print('({0:.3f} seconds too slow)'.format(target-elapsed))


waiting_game()
