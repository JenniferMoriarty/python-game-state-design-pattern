#from abc import ABC, abstractmethod

#------------------------------------------------------------
class Context:

    #class variable
    state = None

    #class constructor
    def __init__(self, state):
        self.transition_to(state)

    #function that changes state
    def transition_to(self, state):
        print("transitioning state to", self.state)
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

#--------------------------------------------------------------------

class State():

    def context(self) -> Context:
        return self._context

    def context(self, context: Context) -> None:
        self._context = context

    def handle1(self) -> None:
        pass

    def handle2(self) -> None:
        pass

#--------------------------------------------------------------------
class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")

#--------------------------------------------------------------------
class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())

#MAIN--------------------------------------------------------------
if __name__ == "__main__":
    # The client code.

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()

