---- MODULE MC ----
EXTENDS Moricka, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
m1, m2, m3, m4
----

\* MV CONSTANT definitions MS
const_1601385665640172000 == 
{m1, m2, m3, m4}
----

\* SYMMETRY definition
symm_1601385665640173000 == 
Permutations(const_1601385665640172000)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 15:21:05 CEST 2020 by tobal
