---- MODULE MC ----
EXTENDS Remove, TLC

\* Constant expression definition @modelExpressionEval
const_expr_1601370013220108000 == 
1..3 \X {"a", "b"}
----

\* Constant expression ASSUME statement @modelExpressionEval
ASSUME PrintT(<<"$!@$!@$!@$!@$!",const_expr_1601370013220108000>>)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 11:00:13 CEST 2020 by tobal
