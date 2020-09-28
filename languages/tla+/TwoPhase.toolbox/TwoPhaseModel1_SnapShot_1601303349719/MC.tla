---- MODULE MC ----
EXTENDS TwoPhase, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
r1, r2, r3
----

\* MV CONSTANT definitions RM
const_160130334668441000 == 
{r1, r2, r3}
----

\* SYMMETRY definition
symm_160130334668442000 == 
Permutations(const_160130334668441000)
----

=============================================================================
\* Modification History
\* Created Mon Sep 28 16:29:06 CEST 2020 by tobal
