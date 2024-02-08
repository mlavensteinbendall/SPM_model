# spm_theme1

## Notes on structured population modelling
## Stephen Williams

# To do

- Perform the t-style solutions convergence test with the following (in order of increasing complexity)...
   1. $g(s)\neq 1$, this is essential to confirming that a size structured model is viable. Perhaps a good place to start here would be $g(s) = g0 - g0(s/s_{adult})$ (i.e. a population for which the growth is initially fastest and decreases until it reaches a maximum). Note, this type of growth leads to an asymptote in the PDE solution at $s=s_{adult}$, for this the time-step size needs to be carefully considered to avoid issues in the solver.
   2. $\mu(s)\neq 0$, this is a bit of a litmus test that confirms whether the Strang-Splitting is working for the time part of the solver.
   3. $r(s) \neq 0$, this would let us explore whether the boundary conditions are working as expected. This one is a little tricky, as the L and R boundary conditions are currently disabled subject to the idea that things never "get" to them. For this to work properly I think that the left boundary could potentially make the solver $<o(dt^2,ds^2)$.

- Can these be solved w/ method characteristics analytically?

- Once all the convergence testing is working as expected the next steps would be to re-write the parameter estimation code in python so it can be integrated with the refactored solver. 
- In parallel with this, it would be good also to write global sensitivity analysis code in python (again, using the refactored solver).

Need to type of the dt notes.
r potentially independent of s, hype.
no mortality is clear from exp'rm.

## Morgan Lavenstein Bendall's Running Notes
Files
conv_test_run.py        -- run file
function_LW.py          -- function that uses Lax-Wendroff method to solve the SPM
conv_processing_d*.py   -- converges of method

Functions
LW_SPM(ds,dt,ntag,filename) -- SPM model 
    - Ploting N -- y-axis is population, x-axis is ds [0,Nsize]


Task given by Steve:   
    - test the g(s) = exp(-s) and mu(s) = s
    - using analytic solution, check the convergence

Test these cases (no reproduction):
- original:             g(s) = 1 and mu(s) = 0
- changing mortality:   g(s) = 1 and mu(s) = s
- changing growth:      g(s) = exp(-s) and m(s) = 0
- changing g & mu:      g(s) = exp(-s) and m(s) = s

changing mortality 
-