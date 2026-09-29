---- MODULE MC ----
EXTENDS TwoPhase, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
r1, r2, r3
----

\* MV CONSTANT definitions RM
const_160136863090699000 == 
{r1, r2, r3}
----

\* SYMMETRY definition
symm_1601368630906100000 == 
Permutations(const_160136863090699000)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 10:37:10 CEST 2020 by tobal
