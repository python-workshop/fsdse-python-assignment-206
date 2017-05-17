# Given a real number between 0 and 1, print the binary representation. If the length of the representation is > 32, return 'ERROR'.

## Constraints
* Is the input a float?
    * Yes
* Is the output a string?
    * Yes
* Is 0 and 1 inclusive?
    * No
* Does the result include a trailing zero and decimal point?
    * Yes
* Is the leading zero and decimal point counted in the 32 char limit?
    * Yes
* Can we assume the inputs are valid?
    * No
* Can we assume this fits memory?
    * Yes


## Algorithm
* Set the result to '0.'
* Start with a fraction of 0.5, which is 0.1 in base 2
* Loop while num > 0
    * Check num versus fraction
        * If num > fraction, add a 1 to the result, num -= fraction
        * Else, add a 0 to the result
        * If the len(result) > 32, return 'ERROR'