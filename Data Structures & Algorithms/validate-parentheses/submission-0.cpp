class Solution {
public:
    bool isValid(string s) {
         stack<char> st;

        for (char c : s) {
            // If opening bracket, push it
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            else {
                // If closing bracket but stack is empty -> invalid
                if (st.empty()) return false;

                char top = st.top();

                // Check if closing matches the top opening
                if ((c == ')' && top == '(') ||
                    (c == '}' && top == '{') ||
                    (c == ']' && top == '[')) {
                    st.pop();
                } else {
                    return false; // mismatch
                }
            }
        }

        // Valid only if no leftover openings
        return st.empty();
    }
};
