---- MODULE MC ----
EXTENDS Moricka, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
m1, m2
----

\* MV CONSTANT definitions MS
const_1601385324349163000 == 
{m1, m2}
----

\* SYMMETRY definition
symm_1601385324349164000 == 
Permutations(const_1601385324349163000)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 15:15:24 CEST 2020 by tobal
