---- MODULE MC ----
EXTENDS Moricka, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
m1, m2
----

\* MV CONSTANT definitions MS
const_1601384723766160000 == 
{m1, m2}
----

\* SYMMETRY definition
symm_1601384723766161000 == 
Permutations(const_1601384723766160000)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 15:05:23 CEST 2020 by tobal
