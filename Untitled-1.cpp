#include<bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;
/* 
int main() {
    using namespace std;
    string s1;
    getline(cin, s1);
    cout << "You entered: " << s1 << endl;
    string s2 = "";

    int c =0 ;
    for(char ch : s1){
        if(ch == '#'){
            c++;
        }
        else{
            s2 += ch;
        }
    }
    cout<< string(c, '#') + s2 << endl;
    return 0;
}
    

int main() {
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    unordered_map<int,int> mp;
    for ( int i = 0; i<n; i++){
        mp[a[i]]++;
    }
    for (auto it : mp){
        cout << it.first << " " << it.second << endl;
    }
    return 0;

}
*/

int main () { 
    string s1;
    string s2;
    getline(cin, s1);
    getline(cin, s2);

    if(s1.length() != s2.length()){
        cout<<"Not Anagram"<<endl;
    }
    else{
        sort(s1.begin() , s1.end());
        sort(s2.begin() , s2.end());
        if(s1 == s2){
            cout<<"yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }

}