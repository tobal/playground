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

ManagerReceivesAck == /\ \E m \in MS: /\ Len(managerInboxes[m]) > 0
                                      /\ managerInboxes' = [managerInboxes EXCEPT ![m] =
                                                            Tail(managerInboxes[m])]
                                      /\ managerStates' = [managerStates EXCEPT ![m] = "CanSend"]
                      /\ UNCHANGED <<coderState, coderInbox>>


Next == \/ ManagerGivesWork
        \/ CoderBeginsWorking
        \/ CoderFinishesWork
        \/ ManagerReceivesAck

Invariant == \E m \in MS: /\ Len(managerInboxes[m]) > 0
                          /\ managerStates[m] = "Waiting"

=============================================================================
\* Modification History
\* Last modified Tue Sep 29 15:26:23 CEST 2020 by tobal
\* Created Tue Sep 29 14:07:02 CEST 2020 by tobal
