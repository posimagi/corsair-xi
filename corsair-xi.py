#!/usr/bin/env python

OTHER = 1
TEN = 10
ELEVEN = 11
BUST = 12

LUCKY = 5
UNLUCKY = 9
SNAKE_EYE_LEVEL = 5
CONSECUTIVE_ROLLS = 2
RUNS = 10000

import random

from collections import Counter

class Roll:
    def __init__(self, lucky, unlucky):
        self.lucky_number = lucky
        self.unlucky_number = unlucky

        self.lucky = False
        self.unlucky = False
        self.eleven = False
        self.bust = False

        self.value = 0
        self.rolls = []
        self.snake_eye_available = True
        # self.fold_available = True

    def reset(self):
        # Snake Eye and Fold will be unavailable if used on the previous roll.
        self.lucky = False
        self.unlucky = False
        self.eleven = False
        self.bust = False

        self.value = 0
        self.rolls = []

    def add(self, roll):
        self.lucky = False
        self.unlucky = False

        self.value += roll
        self.rolls.append(roll)

        if self.value == self.lucky_number:
            self.lucky = True
        if self.value == self.unlucky_number:
            self.unlucky = True
        if self.value == ELEVEN:
            self.eleven = True
        if self.value > ELEVEN:
            self.bust = True
    
    def almost_lucky(self):
        return self.value == self.lucky_number - 1

    def make_eleven(self):
        self.add(ELEVEN - self.value)

    def double_up(self):
        value = random.randint(1, 6)
        self.add(value)
        
    def snake_eye(self):
        if random.randint(1, 10) <= SNAKE_EYE_LEVEL - 1:
            self.make_eleven()
        else:
            self.add(1)
        self.snake_eye_available = False

def monte_carlo(runs, rolls, lucky, unlucky):
    print "============== Corsair XI =============="
    print "Starting monte carlo simulation with runs:", runs
    print "Rolls per run:", rolls
    print "Strategy: Snake Eye (if available) on 10, Unlucky, and (Lucky - 1). Stand on 8 and 9."
    print "Lucky number: " + str(lucky) + "; Unlucky number: " + str(unlucky)
    results = []
    for _ in xrange(runs):
        roll = Roll(lucky, unlucky)
        for _ in xrange(CONSECUTIVE_ROLLS):
            roll.reset()
            while True:
                if roll.bust:
                    results.append(BUST)
                    break
                elif roll.eleven:
                    results.append(ELEVEN)
                    break
                elif roll.lucky:
                    results.append(LUCKY)
                    break
                elif roll.unlucky:
                    if roll.snake_eye_available:
                        roll.snake_eye()
                    else:
                        results.append(UNLUCKY)
                        break
                elif roll.value == TEN:
                    if roll.snake_eye_available:
                        roll.snake_eye()
                    else:
                        results.append(TEN)
                        break
                elif roll.almost_lucky() and roll.snake_eye_available:
                    roll.snake_eye()
                elif roll.value == 8 or roll.value == 9:
                    results.append(OTHER)
                    break
                else:
                    roll.double_up()

    count = Counter(results)
    print "================ Result ================"
    print "Lucky   : " + str(count[LUCKY]  ) + " (" + str(count[LUCKY]  /float(runs * CONSECUTIVE_ROLLS) * 100) + "%)"
    print "Unlucky : " + str(count[UNLUCKY]) + " (" + str(count[UNLUCKY]/float(runs * CONSECUTIVE_ROLLS) * 100) + "%)"
    print "Eleven  : " + str(count[ELEVEN] ) + " (" + str(count[ELEVEN] /float(runs * CONSECUTIVE_ROLLS) * 100) + "%)"
    print "Bust    : " + str(count[BUST]   ) + " (" + str(count[BUST]   /float(runs * CONSECUTIVE_ROLLS) * 100) + "%)"
    print "Others  : " + str(count[OTHER]  ) + " (" + str(count[OTHER]  /float(runs * CONSECUTIVE_ROLLS) * 100) + "%)" 
    print "========================================"

if __name__ == "__main__":
    monte_carlo(RUNS, CONSECUTIVE_ROLLS, LUCKY, UNLUCKY)
