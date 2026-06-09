class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            // Calculate carry bits (unsigned avoids overflow errors)
            int carry = (unsigned int)(a & b) << 1;
            // Add bits without carrying
            a = a ^ b;
            // Move carry to b for the next iteration
            b = carry;
        }
        return a;
        
    }
};
