from scanner import Scanner

class Case4Checker(Scanner):

    def __init__(self,stream):
        Scanner.__init__(self, stream)
        self.accepting_states=["S","E","E1","E1E2","E2","E2E1"]
        self.laststate = "S"
        self.dead = False

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
            if input == '1':
                return "E1"
            elif input == '2':
                return "E2"
            return "S"

        def E1():
            if input == 'G':
                return "E1G"
            elif input == 'E':
                return "E1E"
            elif input == '\043':
                return "Comment"
            return "E1"

        def E1G():
            if input == ' ':
                return "E1G_"
            return "Dead"

        def E1G_():
            if input == '2':
                return "Dead"
            elif input == "1":
                return "S"
            return "E1"

        def E1E():
            if input == ' ':
                return "E1E_"
            return "Dead"

        def E1E_():
            if input == '2':
                return "E1E2"
            return "E1"

        def E1E2():
            if input == 'G':
                return "E1E2G"
            elif input == '\043':
                return "Comment"
            return "E1E2"

        def E1E2G():
            if input == ' ':
                return "E1E2G_"
            return "Dead"

        def E1E2G_():
            if input == '2':
                print("track 2 got green light while train one arrived first!")
                return "Dead"
            elif input == "1":
                return "E2"
            return "E1E2"

        def E2():
            if input == 'G':
                return "E2G"
            elif input == 'E':
                return "E2E"
            elif input == '\043':
                return "Comment"
            return "E2"

        def E2G():
            if input == ' ':
                return "E2G_"
            return "Dead"

        def E2G_():
            if input == '1':
                return "Dead"
            elif input == "2":
                return "S"
            return "E2"

        def E2E():
            if input == ' ':
                return "E2E_"
            return "Dead"

        def E2E_():
            if input == '1':
                return "E2E1"
            return "E2"

        def E2E1():
            if input == 'G':
                return "E2E1G"
            elif input == '\043':
                return "Comment"
            return "E2E1"

        def E2E1G():
            if input == ' ':
                return "E2E1G_"
            return "Dead"

        def E2E1G_():
            if input == '1':
                return "Dead"
                print("track 2 got green light while train one arrived first!")
            elif input == "2":
                return "E1"
            return "E2E1"


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
            "E1": E1,
            "E1G": E1G,
            "E1G_": E1G_,
            "E1E": E1E,
            "E1E_": E1E_,
            "E1E2": E1E2,
            "E1E2G": E1E2G,
            "E1E2G_": E1E2G_,
            "E2": E2,
            "E2G": E2G,
            "E2G_": E2G_,
            "E2E": E2E,
            "E2E_": E2E_,
            "E2E1": E2E1,
            "E2E1G": E2E1G,
            "E2E1G_": E2E1G_,
            "Dead": Dead,
            "Comment": Comment
        }
        state = cases.get(state, S) # invalid states get mapped to start state
        return state()



    def entry(self, state, input):
        if state == "Dead":
            if not self.dead:
                print("Died in " + self.laststate + " on input " + input)
                self.dead = True

        if state != "Comment":
            self.laststate = state
