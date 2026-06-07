#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

class MinStack {
private:
    // All class methods can access them
    stack<int> mainStack;
    stack<int> minStack;

public:
    MinStack() {}
    
    void push(int val) {
        mainStack.push(val);
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
        }
    }
    
    void pop() {
        if (mainStack.empty()) return;
        
        if (mainStack.top() == minStack.top()) {
            minStack.pop();
        }
        mainStack.pop();
    }
    
    int top() {
        return mainStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
