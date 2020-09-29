---- MODULE MC ----
EXTENDS Moricka, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
m1, m2
----

\* MV CONSTANT definitions MS
const_1601384710761153000 == 
{m1, m2}
----

\* SYMMETRY definition
symm_1601384710761154000 == 
Permutations(const_1601384710761153000)
----

\* INVARIANT definition @modelCorrectnessInvariants:1
inv_1601384710762156000 ==
Len(coderInbox) < 2
----
=============================================================================
\* Modification History
\* Created Tue Sep 29 15:05:10 CEST 2020 by tobal
