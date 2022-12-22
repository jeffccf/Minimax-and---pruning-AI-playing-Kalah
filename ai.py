import time
import random 
import io

class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"

class ai:
    def __init__(self):
        pass
    class state:
        def __init__(self, a, b, a_fin, b_fin):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin

    # Kalah:
    #         b[5]  b[4]  b[3]  b[2]  b[1]  b[0]
    # b_fin                                         a_fin
    #         a[0]  a[1]  a[2]  a[3]  a[4]  a[5]
    # Main function call:
    # Input:
    # a: a[5] array storing the stones in your holes
    # b: b[5] array storing the stones in opponent's holes
    # a_fin: Your scoring hole (Kalah)
    # b_fin: Opponent's scoring hole (Kalah)
    # t: search time limit (ms)
    # a always moves first
    #
    # Return:
    # You should return a value 0-5 number indicating your move, with search time limitation given as parameter
    # If you are eligible for a second move, just neglect. The framework will call this function again
    # You need to design your heuristics.
    # You must use minimax search with alpha-beta pruning as the basic algorithm
    # use timer to limit search, for example:
    # start = time.time()
    # end = time.time()
    # elapsed_time = end - start
    # if elapsed_time * 1000 >= t:
    #    return result immediately 
    # def move(self, a, b, a_fin, b_fin, t):
    #     #For test only: return a random move
    #     r = []
    #     for i in range(6):
    #         if a[i] != 0:
    #             r.append(i)
    #     # To test the execution time, use time and file modules
    #     # In your experiments, you can try different depth, for example:
    #     f = open('time.txt', 'a') #append to time.txt so that you can see running time for all moves.
    #     # Make sure to clean the file before each of your experiment
    #     for d in [3, 5, 7]: #You should try more
    #         f.write('depth = '+str(d)+'\n')
    #         t_start = time.time()
    #         self.minimax(depth = d)
    #         f.write(str(time.time()-t_start)+'\n')
    #     f.close()
    #     return r[random.randint(0, len(r)-1)]
        #But remember in your final version you should choose only one depth according to your CPU speed (TA's is 3.4GHz)
        #and remove timing code. 
        
        #Comment all the code above and start your code here

    def move(self, a, b, a_fin, b_fin, t):
        # #For test only: return a random move
        # r = []
        # for i in range(6):
        #     if a[i] != 0:
        #         r.append(i)
        # # To test the execution time, use time and file modules
        # # In your experiments, you can try different depth, for example:
        # f = open('time.txt', 'a') #append to time.txt so that you can see running time for all moves.
        # # Make sure to clean the file before each of your experiment
        # for d in [3, 5, 7]: #You should try more
        #     f.write('depth = '+str(d)+'\n')
        #     t_start = time.time()
        #     self.minimax(3, a, b, a_fin, b_fin)
        #     f.write(str(time.time()-t_start)+'\n')
        # f.close()
        # return r[random.randint(0, len(r)-1)]
        #But remember in your final version you should choose only one depth according to your CPU speed (TA's is 3.4GHz)
        #and remove timing code.
        start=time.time()
        depth = 8 # Set the depth
        state = self.state(a,b,a_fin,b_fin) # Initial state
        move = self.minimax(depth-1, state) # Run minimax to find the move
        print(time.time()-start)
        return move

    def minimax(self, depth, state):
        # example: doing nothing but wait 0.1*depth sec
        # time.sleep(0.1*depth)
        val, move = self.max_layer(depth, state, float('inf')) # call max layer, this is the root node so that beta equals infinity
        return move

    def next_hole(self,cur): # Given a hole, return its next hole (string type)
        if cur=='a_fin': # if previous hole is ai's kalah, next hole is b[0]
            return 'b0'
        if cur=='b_fin': # if previous hole is opponent's kalah, next hole is a[0]
            return 'a0'
        side = cur[0] # Previous hole is not kalah, get the side of the hole (side='a' or 'b')
        i = int(cur[1]) # Previous hole is not kalah, get the index of the hole
        if side=='a':
            if i==5:
                return 'a_fin' # Previous hole is a[5], next hole is ai's kalah
            return side+str(i+1) # Previous hole is a[i],next hole is a[i+1]
        if side=='b':
            if i==5:
                return 'b_fin' # Previous hole is b[5], next hole is opponent's kalah
            return side+str(i+1) # Previous hole is b[i],next hole is b[i+1]

    # This method returns the state given current state and a possible move
    def next_state(self, nextstate, side, i): #side='a','b','a_fin' or 'b_fin'
        turn = 'ai' if side=='a' else 'oppo' # Who's turn
        if side=='a': # If it is ai turn, count the stones of the chosen hole
            cnt = nextstate.a[i] # Number of stones in the chosen hole
            nextstate.a[i] = 0 # The stones in the hole becomes 0
            next_h = 'a'+str(i) # Current hole in string type
        else: # If it is opponents turn, count the stones of the chosen hole
            cnt = nextstate.b[i] # Number of stones in the chosen hole
            nextstate.b[i] = 0 # The stones in the hole becomes 0
            next_h = 'b'+str(i) # Current hole in string type
        while cnt>0: # Loop until all stones are placed
            next_h=self.next_hole(next_h) # Get the next hole
            if len(next_h)==2: # If the hole is not a_fin nor b_fin
                side = next_h[0] # Side to put the stone
                i = int(next_h[1]) # Index of the hole
                if side=='a': # Put the stones
                    nextstate.a[i]+=1
                else:
                    nextstate.b[i]+=1
            else: # If current hole is one of the kalah
                if next_h=='a_fin':
                    if turn=='ai': # If the hole is a_fin and its ai's turn, a_fin+=1
                        nextstate.a_fin+=1
                    else: # If the hole is a_fin and its opponent's turn, continue so that cnt won't -1
                        continue
                else:
                    if turn=='oppo': # If the hole is b_fin and its opponent's turn, b_fin+=1
                        nextstate.b_fin+=1
                    else: # If the hole is b_fin and its ai's turn, continue so that cnt won't -1
                        continue
            cnt-=1
        if (turn=='ai' and next_h=='a_fin') or (turn=='oppo' and next_h=='b_fin'):
        # If last stone lands in the player's kalah, return the state and True. The boolean parameter indicates whether the last stone lands in kalah
            return nextstate, True
        if nextstate.a[i]==1 and side=='a' and turn=='ai' and nextstate.b[5-i]>0:
        # If the last stone lands in ai's empty hole and its ai's turn and opponent's direct hole has stones, take all the stones in that hole
        # Update the holes
            nextstate.a_fin+=nextstate.b[5-i]+1
            nextstate.a[i] = 0
            nextstate.b[5-i] = 0
        elif nextstate.b[i]==1 and side=='b' and turn=='oppo' and nextstate.a[5-i]>0:
        # Same thing happens on the opponents side
            nextstate.b_fin+=nextstate.a[5-i]+1
            nextstate.a[5-i] = 0
            nextstate.b[i] = 0
        return nextstate, False # Return the state and False, the last stone didn't land in kalah

    def heuristic(self,  state): # arr[0]=a, arr[1]=b, arr[2]=a_fin, arr[3]=b_fin
        if state.a_fin>36 or (sum(state.b)==0 and sum(state.a)+state.a_fin>36): # ai wins
            return 1000000 # Returns a large number
        if state.b_fin>36 or (sum(state.a)==0 and sum(state.b)+state.b_fin>36): # opponent wins
            return -1000000 # Return a small number
        num = 5 # If the ith hole has 6-i stones (mod13), pick this hole gives the player an extra turn, give this a score
        score = 0 # Count the score
        for i in range(6):
            if state.a[i]%13==6-i: # The ith hole has 6-i stones, pick this hole gives ai and extra turn, add num*i to the score
                score+=num
            if state.b[i]%13==6-i: # Same thing for the opponent
                score-=num
        weight = 7 # The weight of the stones in the kalah
        stone_num=1 # The weight of the number of stones in holes
        return score+(state.a_fin-state.b_fin)*weight+(sum(state.a)-sum(state.b))*stone_num

    def max_layer(self, depth, state, beta): # Max layer
        if sum(state.a)==0 or sum(state.b)==0 or state.a_fin>36 or state.b_fin>36 or depth==0: # Death state, return the heuristic
            return self.heuristic(state), None

        candidates = [] # Store the holes with stones

        for i in range(6):
            if state.a[i]!=0:
                candidates.append(i)

        curmax = float('-inf') # Current value of the state

        for i in candidates:
            a = list(state.a)
            b = list(state.b)
            a_fin = int(state.a_fin)
            b_fin = int(state.b_fin) # store the parameters of the state
            temp_state = self.state(a, b, a_fin, b_fin) # Temporary state
            next_state, kalah = self.next_state(temp_state,'a',i) # Get the next state, kalah is true if the player has an extra turn
            if kalah: # If ai has an extra turn, get the state value from max layer instead of min layer
                val, _ = self.max_layer(depth - 1, next_state, float('inf'))
            else: # Get the state value from min layer with alpha equals current value
                val, _ = self.min_layer(depth-1, next_state, curmax)
            if val>curmax: # If the new value is larger than the current value
                curmax = val # Update the largest value
                move = i # Update the argmax
                if beta<curmax: # Beta-pruning
                    return curmax, move
        return curmax, move # Return the value and the move

    def min_layer(self, depth, state, alpha): # Min layer
        if sum(state.a)==0 or sum(state.b)==0 or state.a_fin>36 or state.b_fin>36 or depth==0: # Death state, return the heuristic
            return self.heuristic(state), None

        candidates = [] # Store the holes with stones

        for i in range(6):
            if state.b[i]!=0:
                candidates.append(i)

        curmin = float('inf') # Current value of the state

        for i in candidates:
            a = list(state.a)
            b = list(state.b)
            a_fin = int(state.a_fin)
            b_fin = int(state.b_fin) # store the parameters of the state
            temp_state = self.state(a, b, a_fin, b_fin) # Temporary state
            next_state, kalah = self.next_state(temp_state,'b',i) # Get the next state, kalah is true if the player has an extra turn
            if kalah: # If opponent has an extra turn, get the state value from min layer instead of max layer
                val, _ = self.min_layer(depth - 1, next_state, float('-inf'))
            else: # Get the state value from max layer with beta equals current value
                val, _ = self.max_layer(depth-1, next_state, curmin)
            if val<curmin: # If the new value is smaller than the current value
                curmin = val # Update the current value
                move = i # Update the argmin
                if alpha>curmin: # alpha-pruning
                    return curmin,move
        return curmin, move # Return the value and the move


