#include "lc_pub.h"

class TextEditor {
public:
    TextEditor() {
    }
    
    void addText(string text) {
        left += text;
    }
    
    int deleteText(int k) {
        int l = left.size();
        k = min(k, l);
        left.resize(l - k);
        return k;
    }
    
    string cursorLeft(int k) {
        k = min(left.size(), (size_t)k);
        for (int i=0;i<k;i++) {
            right += left.back();
            left.pop_back();
        }
        int l = left.size();
        int l1 = min(10, l);
        return left.substr(l - l1);
    }
    
    string cursorRight(int k) {
        k = min(right.size(), (size_t)k);
        for (int i=0;i<k;i++) {
            left += right.back();
            right.pop_back();
        }
        int l = left.size();
        int l1 = min(10, l);
        return left.substr(l - l1);
    }
    string left;
    string right;
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    TextEditor so;
    so.addText("leetcode");
    cout << so.deleteText(10) << endl;
    return 0;
}
