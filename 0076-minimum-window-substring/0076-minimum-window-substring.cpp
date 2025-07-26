class Solution 
{
public:
    string minWindow(string s, string t) 
    {
        int m = s.length();
        int n = t.length();
        int l = 0, r = 0, stldx = -1, cnt = 0;
        int minlen = INT_MAX;
        int hash[256] = {0};

        for(int i=0; i<n; i++)
        {
            hash[t[i]]++;
        }
        while(r<m)
        {
            if(hash[s[r]]>0)
            cnt++;
            hash[s[r]]--;
            while(cnt==n)
            {
                if(r-l+1<minlen)
                {
                    minlen = r-l+1;
                    stldx = l;
                }
                hash[s[l]]++;
                if(hash[s[l]]>0)
                cnt--;
                l++;
            }
            r++;
        }
        return stldx == -1?"": s.substr(stldx, minlen);
    }
};