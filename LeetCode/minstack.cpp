// C++ solution using a vector of pairs
// <the current value, the minimum value up to that point>

class MinStack {
public:
    MinStack() {
    }
    
    void push(int val) {
        if (vec.empty()) {
            vec.push_back({val, val});
        }
        else {
            vec.push_back({val, min(vec.back().second, val)});
        }
    }
    
    void pop() {
        vec.pop_back();
    }
    
    int top() {
        return vec.back().first;    
    }
    
    int getMin() {
        return vec.back().second;        
    }
private:
    vector<pair<int, int>> vec;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */