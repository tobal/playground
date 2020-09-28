------------------------------ MODULE DieHard ------------------------------
EXTENDS Integers
VARIABLES small, big

TypeOK == /\ small \in 0..3
          /\ big \in 0..5

Init == /\ small = 0
        /\ big = 0

FillSmall == /\ small' = 3
             /\ big' = big

FillBig == /\ big' = 5
           /\ small' = small

EmptySmall == /\ small' = 0
              /\ big' = big


EmptyBig == /\ big' = 0
            /\ small' = small

SmallToBig == IF big + small =< 5
                THEN /\ big' = big + small
                     /\ small' = 0
                ELSE /\ small' = small - (5 - big)
                     /\ big' = 5

BigToSmall == IF big + small =< 3
                THEN /\ small' = big + small
                     /\ big' = 0
                ELSE /\ big' = small - (3 - big)
                     /\ small' = 3

Next == \/ FillSmall
        \/ FillBig
        \/ EmptySmall
        \/ EmptyBig
        \/ SmallToBig
        \/ BigToSmall 

=============================================================================
\* Modification History
\* Last modified Mon Sep 28 12:53:37 CEST 2020 by tobal
\* Created Mon Sep 28 12:20:04 CEST 2020 by tobal
