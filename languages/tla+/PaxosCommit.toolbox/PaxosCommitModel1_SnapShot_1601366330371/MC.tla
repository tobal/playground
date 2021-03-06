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
const_160136629112643000 == 
{a1, a2, a3}
----

\* MV CONSTANT definitions RM
const_160136629112644000 == 
{r1, r2}
----

\* SYMMETRY definition
symm_160136629112645000 == 
Permutations(const_160136629112643000) \union Permutations(const_160136629112644000)
----

\* CONSTANT definitions @modelParameterConstants:0Ballot
const_160136629112646000 == 
{0,1}
----

\* CONSTANT definitions @modelParameterConstants:2Majority
const_160136629112647000 == 
{{a1, a2}, {a1, a3}, {a2, a3}}
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 09:58:11 CEST 2020 by tobal
