------------------------------ MODULE Moricka ------------------------------
EXTENDS Sequences, Integers
CONSTANTS MS
VARIABLES managerInboxes, coderInbox, managerStates, coderState

TypeOK == /\ coderState \in {"Idle"} \cup MS
          /\ managerStates \in [MS -> {"CanSend", "Waiting"}]
          
Init == /\ coderState = "Idle"
        /\ managerStates = [m \in MS |-> "CanSend"]
        /\ coderInbox = <<>>
        /\ managerInboxes = [m \in MS |-> <<>>]

Next == \/ /\ \E m \in MS: /\ managerStates[m] = "CanSend"
                           /\ coderInbox' = Append(coderInbox, m)
                           /\ managerStates' = [managerStates EXCEPT ![m] = "Waiting"]
           /\ UNCHANGED <<coderState, managerInboxes>>
        \/ /\ Len(coderInbox) > 0
           /\ coderState = "Idle"
           /\ coderInbox' = Tail(coderInbox)
           /\ coderState' = Head(coderInbox)
           /\ UNCHANGED <<managerInboxes, managerStates>>
\*        \/ /\ coderState = "Working"
\*           /\ coderState' = "Idle"
\*           /\ managerInbox' = Append(managerInbox, "2")
\*           /\ UNCHANGED <<coderInbox, managerState>>
\*        \/ /\ managerState = "Waiting"
\*           /\ Len(managerInbox) > 0
\*           /\ managerInbox' = Tail(managerInbox)
\*           /\ managerState' = "CanSend"
\*           /\ UNCHANGED <<coderState, coderInbox>>

=============================================================================
\* Modification History
\* Last modified Tue Sep 29 15:05:07 CEST 2020 by tobal
\* Created Tue Sep 29 14:07:02 CEST 2020 by tobal
