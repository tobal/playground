---- MODULE MC ----
EXTENDS Moricka, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
m1, m2, m3, m4
----

\* MV CONSTANT definitions MS
const_1601385994899213000 == 
{m1, m2, m3, m4}
----

\* SYMMETRY definition
symm_1601385994899214000 == 
Permutations(const_1601385994899213000)
----

\* INVARIANT definition @modelCorrectnessInvariants:1
inv_1601385994899216000 ==
 \E m \in MS: (Len(managerInboxes[m]) > 0 /\ managerStates[m] = "Waiting")
----
=============================================================================
\* Modification History
\* Created Tue Sep 29 15:26:34 CEST 2020 by tobal
