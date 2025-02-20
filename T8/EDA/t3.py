# Pairwise Function
def pairwise_tests(K):
    # If test is less than or equal to 1 then 0 is returned
    if K <= 1:
        return 0
    else:
        # Returns the recursive call to solve for K/2  plus the tests
        # needed for the current set of witnesses
        return pairwise_tests(K // 2) + K
# Set K to be the number of witnesses
K = int(input("Enter the number of witnesses (K): "))
# Calls for the resuly of the pairwise test with K witnesses
result = pairwise_tests(K)
# Prints out the number of tests needed 
print(f"Number of pairwise tests needed: {result}")
