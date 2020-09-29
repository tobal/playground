---- MODULE MC ----
EXTENDS PaxosCommit, TLC

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
a1, a2, a3
----

\* MV CONSTANT declarations@modelParameterConstants
CONSTANTS
r1, r2
----

\* MV CONSTANT definitions Acceptor
const_160136854098080000 == 
{a1, a2, a3}
----

\* MV CONSTANT definitions RM
const_160136854098081000 == 
{r1, r2}
----

\* SYMMETRY definition
symm_160136854098082000 == 
Permutations(const_160136854098080000) \union Permutations(const_160136854098081000)
----

\* CONSTANT definitions @modelParameterConstants:0Ballot
const_160136854098083000 == 
{0,1}
----

\* CONSTANT definitions @modelParameterConstants:2Majority
const_160136854098084000 == 
{{a1, a2}, {a1, a3}, {a2, a3}}
----

\* INVARIANT definition @modelCorrectnessInvariants:1
inv_160136854098086000 ==
TCConsistent
----
=============================================================================
\* Modification History
\* Created Tue Sep 29 10:35:40 CEST 2020 by tobal
