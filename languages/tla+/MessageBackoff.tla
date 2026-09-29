--------------------------- MODULE MessageBackoff ---------------------------
CONSTANTS MESSAGES
VARIABLES state, numServiceRecievedMessage

Message == [type: {"Request", "Response"}]

TypeOK == /\ state \in {"Idle", "WaitingForResponse"}
          /\ MESSAGES \subseteq Message

Init == /\ state = "Idle"
        /\ numServiceRecievedMessage = 0

IdleState == IF state = "Idle"
               THEN IF MESSAGES[0].type = "Request"
                      THEN /\ numServiceRecievedMessage' = numServiceRecievedMessage + 1
                           /\ state' = "WaitingForResponse"

WaitingForResponseState == IF state = "WaitingForResponse"

Next == IdleState \/ WaitingForResponseState

=============================================================================
\* Modification History
\* Last modified Tue Sep 29 14:06:24 CEST 2020 by tobal
\* Created Tue Sep 29 13:30:35 CEST 2020 by tobal
