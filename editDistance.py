def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a table to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp[][] in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, the only option is to
            # insert all characters of the second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
    
            # If second string is empty, the only option is to
            # remove all characters of the first string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
    
            # If last characters are the same, ignore the last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
    
            # If the last character is different, consider all
            # possibilities and find the minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace
    
    return dp[m][n]

# Example usage
str1 = "kitten"
str2 = "sitting"
print("Edit Distance between '{}' and '{}' is {}".format(str1, str2, edit_distance(str1, str2)))
