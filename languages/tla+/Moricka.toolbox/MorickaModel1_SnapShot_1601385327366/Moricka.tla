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

ManagerGivesWork == /\ \E m \in MS: /\ managerStates[m] = "CanSend"
                                    /\ coderInbox' = Append(coderInbox, m)
                                    /\ managerStates' = [managerStates EXCEPT ![m] = "Waiting"]
                    /\ UNCHANGED <<coderState, managerInboxes>> 

CoderBeginsWorking == /\ Len(coderInbox) > 0
                      /\ coderState = "Idle"
                      /\ coderInbox' = Tail(coderInbox)
                      /\ coderState' = Head(coderInbox)
                      /\ UNCHANGED <<managerInboxes, managerStates>>
                      
CoderFinishesWork == /\ \E m \in MS: /\ coderState = m 
                                     /\ coderState' = "Idle"
                                     /\ managerInboxes' = [managerInboxes EXCEPT ![m] = 
                                                           Append(managerInboxes[m], "2")]
                     /\ UNCHANGED <<coderInbox, managerStates>>

Next == \/ ManagerGivesWork
        \/ CoderBeginsWorking
        \/ CoderFinishesWork

\*        \/ /\ managerState = "Waiting"
\*           /\ Len(managerInbox) > 0
\*           /\ managerInbox' = Tail(managerInbox)
\*           /\ managerState' = "CanSend"
\*           /\ UNCHANGED <<coderState, coderInbox>>

=============================================================================
\* Modification History
\* Last modified Tue Sep 29 15:15:21 CEST 2020 by tobal
\* Created Tue Sep 29 14:07:02 CEST 2020 by tobal
