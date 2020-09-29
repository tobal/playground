---- MODULE MC ----
EXTENDS Moricka, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
m1, m2
----

\* MV CONSTANT definitions MS
const_1601384683297149000 == 
{m1, m2}
----

\* SYMMETRY definition
symm_1601384683297150000 == 
Permutations(const_1601384683297149000)
----

\* INVARIANT definition @modelCorrectnessInvariants:1
inv_1601384683299152000 ==
Len(coderInbox) < 2
----
=============================================================================
\* Modification History
\* Created Tue Sep 29 15:04:43 CEST 2020 by tobal
