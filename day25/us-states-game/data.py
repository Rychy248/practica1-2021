import pandas

class PandaData():
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv") 

    def find_a_state(self,state):
        result = False
        if len(self.data[self.data.state == state]) != 0:
            result = True

        return result 
    
    def get_coor_state(self,state):
        result = self.data[self.data.state == state]
        coor = (float(result["x"]),float(result["y"]))
        return coor 

    def save_missed_states(self,rights_answers=[]):
        all_states = self.data.state.to_list()
        missed_states = [ state for state in all_states if str(state) not in rights_answers]
        print("Missed states")
        index = 1
        for state in missed_states:
            print(f"{index} - ",state,end="")
            if index%5 == 0:
                print("")
            else:
                print(" ~ ",end="")
            index += 1
        print("")
        save_dict = {
            "states":missed_states
        }
        df = pandas.DataFrame(save_dict)
        df.to_csv("missed_states.csv")
