class MyQueue {
public:
    MyQueue() {
        
    }
    
    // Time Complexity: O(1)
    void push(int x) {
        s1.push(x);
    }
    
    // Time Complexity: amortized O(1), worst case O(N)
    int pop() {
        // move queue content from s1 to s2
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int front = s2.top();
        s2.pop();
        return front;
    }
    
    int peek() {
        // move queue content from s1 to s2
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        front = s2.top();
        return front;
    }
    
    bool empty() {
        return s1.empty() && s2.empty();
    }
private:
    int front;
    stack<int> s1;
    stack<int> s2;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */