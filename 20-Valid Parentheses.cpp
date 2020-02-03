class Solution {
public:
    bool isValid(string s) {
        vector<char> check;
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                check.push_back('(');
            } else if (s[i] == '[') {
                check.push_back('[');
            } else if (s[i] == '{') {
                check.push_back('{');
            } else if (s[i] == ')') {
                if (check.size() == 0 || '(' != check[check.size()-1]) {
                    return false;
                }
                check.pop_back();
            } else if (s[i] == ']') {
                if (check.size() == 0 || '[' != check[check.size()-1]) {
                    return false;
                }
                check.pop_back();
            } else if (s[i] == '}') {
                if (check.size() == 0 || '{' != check[check.size()-1]) {
                    return false;
                }
                check.pop_back();
            }
        }
        
        if (check.size() > 0) {
            return false;
        }
        return true;
    }
};
