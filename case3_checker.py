from scanner import Scanner

class Case3Checker(Scanner):

    def __init__(self,stream):
        Scanner.__init__(self, stream)
        self.accepting_states=["S","E3"]
        self.laststate = "S"
        print(stream)

    def __str__(self):
        return "" 

    def transition(self, state, input):
        def S():
            if input == 'E':
                return "E"
            if input == '\043':
                return "Comment"
            return "S"

        def E():
            if input == ' ':
                return "E_"
            return "Dead"

        def E_():
            if input == '3':
                return "E3"
            return "S"

        def E3():
            if input == 'G':
                return "G"
            elif input == 'X':
                return "X"
            elif input == '\043':
                return "Comment"
            return "E3"

        def G():
            if input == ' ':
                return "G_"
            return "Dead"

        def G_():
            if input == '1' or input == '2':
                return "Dead"
            return "E3"

        def X():
            if input == ' ':
                return "X_"
            return "Dead"

        def X_():
            if input == '3':
                return "S"
            return "E3"

        def Dead():
            return "Dead"

        def Comment():
            if input == '\n':
                return self.laststate
            return "Comment"


        cases = {
            None: S,
            "S": S,
            "E": E,
            "E_": E_,
            "E3": E3,
            "G": G,
            "G_": G_,
            "X": X,
            "X_": X_,
            "Dead": Dead,
            "Comment": Comment
        }
        state = cases.get(state, S) # invalid states get mapped to start state
        return state()



    def entry(self, state, input):
        if state != "Comment":
            self.laststate = state
