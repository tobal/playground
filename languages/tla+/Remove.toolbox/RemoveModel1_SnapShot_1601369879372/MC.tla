---- MODULE MC ----
EXTENDS Remove, TLC

\* Constant expression definition @modelExpressionEval
const_expr_1601369877344104000 == 
Remove(3, <<1, 2, 3, 4>>)
----

\* Constant expression ASSUME statement @modelExpressionEval
ASSUME PrintT(<<"$!@$!@$!@$!@$!",const_expr_1601369877344104000>>)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 10:57:57 CEST 2020 by tobal
