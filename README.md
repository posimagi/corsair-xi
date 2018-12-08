# corsair-xi

## Monte Carlo simulation of Phantom Roll strategy for Corsair in FFXI

### How to use

You can tweak the simulation's assumptions by modifying the following variables:
* `LUCKY`: The roll's Lucky number.
* `UNLUCKY`: The roll's Unlucky number.
* `SNAKE_EYE_LEVEL`: The number of merits put into Snake Eye.
* `CONSECUTIVE_ROLLS`: How many Phantom Rolls will be executed before Job Abilities (e.g. Snake Eye) come off cooldown.
* `RUNS`: How many simulations to perform;. A larger number will provide more accurate results, but take longer to execute.

### Limitations

* At this time, the simulation does not support rolls with different sets of Lucky and Unlucky numbers.

### Future enhancements

* Implementation of Fold.
* Adding the ability to modify the strategy employed.
