## Team members:
## Divya Barsode
## Shivangi Shakya
## Mohit Bishnoi

from search import *



class MissCannibals(Problem):
    def __init__(self, initial, goal=(0,0,False), graph=None):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):

        moves = []
        man=0;can=0

        if state[2]:
            man = state[0]
            can = state[1]
        
        else:
            man = 3-state[0]
            can = 3-state[1]

        otherSideMan = 3 - man
        otherSideCan = 3 - can

        if man>=2 and ((man-2 >= can and man-2>0) or man-2==0) and (otherSideMan+2 >= otherSideCan):
            moves.append("MM")

        if man>=1 and ((man - 1 >= can and man-1>0) or man-1==0) and (otherSideMan+1 >= otherSideCan):
            moves.append("M")
       
        if can>=2 and ((otherSideCan+2 <= otherSideMan and otherSideMan>0) or otherSideMan==0):
            moves.append("CC")

        if can>=1 and ((otherSideCan+1 <= otherSideMan and otherSideMan>0) or otherSideMan==0):
            moves.append("C")

        if (can >=1 and man >=1 ) and ((man-1>=can-1 and man-1>0) or man-1==0) and (otherSideMan+1 >= otherSideCan+1):
            moves.append("MC")

        return moves
    

    def isValid(self):
        # first checking for the negative number: not possible
        if self.initial[0] < 0 or self.initial[1] < 0 or self.initial[0] > 3 or self.initial[1] > 3:
            return False   
        # then check whether missionaries outnumbered by cannibals
        if self.initial[1] > self.initial[0] and self.initial[0] > 0:    # more cannibals then missionaries on original shore
            return False
        if self.initial[1] < self.initial[0] and self.initial[0] < 3:    # more cannibals then missionaries on other shore
            return False
        return True

    
    def result(self, state, action):
        actionsPoss= list(action)
        man=0;can=0
        for act in actionsPoss:
            if act=="M":
                man+=1
            else:
                can+=1

        stateList = list(state)
        if stateList[2]:
            stateList[0]-=man
            stateList[1]-=can
        else:
            stateList[0]+=man
            stateList[1]+=can

        stateList[2]= not stateList[2]



        
        return tuple(stateList)



    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':
    initial_state = (3,3,True)
    misscann = MissCannibals(initial_state)
    # print(misscann)



    path = depth_first_graph_search(misscann).solution()
    print("Moves to be taken:",path)

    print( "MMM CCC (B) ~~~ ")
    state = initial_state
    for action in path:
        state = misscann.result(state, action)
        str=""
        for i in range(state[0]):
           str+="M"
        str+=" "
        for i in range(state[1]):
           str+="C"

        if state[2]:
            str+= " (B)"

        str+= " ~~~~ "

        for i in range(3-state[0]):
           str+="M"
        str+=" "
        for i in range(3-state[1]):
           str+="C"

        if not state[2]:
            str+= " (B)"

        print(str)






