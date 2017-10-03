# fincalc

A simple Python module to perform annuity calculations.

To view the package in use on a basic web app, go to [link](http://fincalcapp.appspot.com)


## Overview

The following annuity calculations are supported:

 * present value `pv`
 * future value `fv`
 * repayment `pmt`
 * number of instalments `n`
 * interest rate `i`
 
   
## Installation
   
Copy ```fincalc.py``` into the same directory as your code.
   
## Usage
   
The examples below are based on an annuity loan repayment of `-1434.70948403` per month over 10 years (`120` months), with a present value of `100000`, a future value of `0` and an interest rate of 12% p.a. NACM (`0.01` per month).
   
```Python
import fincalc

print fincalc.fv(0.01, 120, 100000, -1434.70948403)

print fincalc.pv(0.01, 120, 0, -1434.70948403)

print fincalc.pmt(0.01, 120, 100000, 0)

print fincalc.n(0.01, 100000, 0, -1434.70948403)

print fincalc.i(120, 100000, 0, -1434.70948403)
```

   
## License
   
fincalc is released under the MIT License.





