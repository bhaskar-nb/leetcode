import java.util.*;

class Solution 
{
    public List<Integer> findSubstring(String s, String[] words) 
    {
        List<Integer> result = new ArrayList<>();
        if (s.length() == 0 || words.length == 0) return result;

        int wordLen = words[0].length();
        int wordCount = words.length;
        int totalLen = wordLen * wordCount;

        Map<String, Integer> wordMap = new HashMap<>();
        for (String word : words) 
        {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i < wordLen; i++) 
        {
            int left = i, count = 0;
            Map<String, Integer> seenMap = new HashMap<>();

            for (int right = i; right + wordLen <= s.length(); right += wordLen) 
            {
                String word = s.substring(right, right + wordLen);

                if (wordMap.containsKey(word)) 
                {
                    seenMap.put(word, seenMap.getOrDefault(word, 0) + 1);
                    count++;

                    while (seenMap.get(word) > wordMap.get(word))
                    {
                        String leftWord = s.substring(left, left + wordLen);
                        seenMap.put(leftWord, seenMap.get(leftWord) - 1);
                        count--;
                        left += wordLen;
                    }

                    if (count == wordCount) 
                    {
                        result.add(left);
                    }
                } 
                else 
                {
                    seenMap.clear();
                    count = 0;
                    left = right + wordLen;
                }
            }
        }

        return result;
    }
}
