---- MODULE MC ----
EXTENDS Moricka, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
m1, m2, m3, m4
----

\* MV CONSTANT definitions MS
const_1601385701450182000 == 
{m1, m2, m3, m4}
----

\* SYMMETRY definition
symm_1601385701450183000 == 
Permutations(const_1601385701450182000)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 15:21:41 CEST 2020 by tobal
