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
const_160136650942767000 == 
{a1, a2, a3}
----

\* MV CONSTANT definitions RM
const_160136650942768000 == 
{r1, r2}
----

\* SYMMETRY definition
symm_160136650942769000 == 
Permutations(const_160136650942767000) \union Permutations(const_160136650942768000)
----

\* CONSTANT definitions @modelParameterConstants:0Ballot
const_160136650942770000 == 
{0,1}
----

\* CONSTANT definitions @modelParameterConstants:2Majority
const_160136650942771000 == 
{{a1, a2}, {a1, a3}, {a2, a3}}
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 10:01:49 CEST 2020 by tobal
