------------------------------- MODULE Remove -------------------------------
EXTENDS Integers, Sequences

Remove(i, seq) == [j \in 1..(Len(seq) - 1) |->
                   IF j < i THEN seq[j] ELSE seq[j - 1]]

=============================================================================
\* Modification History
\* Last modified Tue Sep 29 10:56:40 CEST 2020 by tobal
\* Created Tue Sep 29 10:53:56 CEST 2020 by tobal
