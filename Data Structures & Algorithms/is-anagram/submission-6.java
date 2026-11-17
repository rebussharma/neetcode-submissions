class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> hm = new HashMap<>();
        for (int i = 0 ; i < s.length(); i++){
            char s_c = s.charAt(i);
            char t_c = t.charAt(i);
            hm.put(s_c, hm.getOrDefault(s_c, 0) + 1);
            hm.put(t_c, hm.getOrDefault(t_c, 0) - 1);
        }

        for (int cnt: hm.values()){
            if( cnt != 0) return false;
        }
        return true;
    }
}
