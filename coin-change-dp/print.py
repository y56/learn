# A Dynamic Programming based Python3 program to  
# find minimum of coins to make a given change V 
  
# m is size of coins array (number of  
# different coins) 
def minCoins(coins, m, V): 
    
    INF = float('inf')
    
    # table[i] will be storing the minimum  
    # number of coins required for i value.  
    # So table[V] will have result 
    table = [0 for i in range(V+1)] 
    
    # Base case (If given value V is 0) 
    table[0] = 0
    
    # Initialize all table values as Infinite 
    for i in range(1, V+1): 
        table[i] = INF 
    
    # Compute minimum coins required  
    # for all values from 1 to V 
    for i in range(1, V + 1): 
        
        print(table)
        print("ask value =", i)
        
        # Go through all coins smaller than i 
        for j in range(m):
            
            print( "try coin:[", coins[j], "]")  
            
            if (coins[j] <= i):

                sub_res = table[i - coins[j]] 
                
                print("coin good")     
                print("check residual value =", i - coins[j], ", there we use", sub_res, "coins")
                print("so here we are using", sub_res+1, "coins")
                
                
                
                if (sub_res + 1 < table[i]): 
                    
                    print("we are using less coins")
                    table[i] = sub_res + 1
                else:
                    print("we are *NOT* use less coins")
            else:
                print("coin too large")
                
    print(table)
    return table[V] 


# Driver Code 
if __name__ == "__main__": 
  
    coins = [9, 6, 5, 1] 
    m = len(coins) 
    V = 11
    print("Minimum coins required is ",  
                 minCoins(coins, m, V)) 
  
