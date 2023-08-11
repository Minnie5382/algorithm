import java.util.*;

class Solution {
    public String solution(String s, int n) {
        String answer = "";

        for (int i=0 ; i<s.length() ; i++) {
            char c = s.charAt(i);
            if (c == ' ') {
                answer += " ";
            } else if ((int)c >= 65 & (int)c <= 90) { // 대문자
                answer += (char)( ((int)c + n - 65) % 26 + 65);
            } else if ((int)c >= 97 & (int)c <= 122) { // 소문자
                answer += (char)( ((int)c + n - 97) % 26 + 97);
            }
        }
    
        return answer;
    }
}