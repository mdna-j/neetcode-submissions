class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty, return an empty string
        if not strs:
            return ""
        
        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check if this character matches the same position in all other strings
            for string in strs[1:]:
                # If the current string is shorter than index 'i' or characters mismatch
                if i == len(string) or string[i] != char:
                    # Return the valid prefix found up to this point
                    return strs[0][:i]
                    
        return strs[0]