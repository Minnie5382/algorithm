class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        int count = 0;
        for (String s : seoul) {
            if (s.equals("Kim")) {
                break;
            } else {
                count++;
            }
        }
        answer = String.format("김서방은 %d에 있다", count);
        return answer;
    }
}