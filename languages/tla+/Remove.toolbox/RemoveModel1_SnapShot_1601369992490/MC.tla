---- MODULE MC ----
EXTENDS Remove, TLC

\* Constant expression definition @modelExpressionEval
const_expr_1601369990465106000 == 
(1..3) \X {"a", "b"}
----

\* Constant expression ASSUME statement @modelExpressionEval
ASSUME PrintT(<<"$!@$!@$!@$!@$!",const_expr_1601369990465106000>>)
----

=============================================================================
\* Modification History
\* Created Tue Sep 29 10:59:50 CEST 2020 by tobal
