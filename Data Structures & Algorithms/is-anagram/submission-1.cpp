class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        string s_sort = s;
        string t_sort = t;
        sort(s_sort.begin(), s_sort.end());
        sort(t_sort.begin(), t_sort.end());

        return s_sort == t_sort;
    }
};
