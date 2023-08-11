import java.util.*;
import java.util.stream.IntStream;

public class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> answer_al = new ArrayList<>();
        int preNum = 10;
        for (int i=0 ; i<arr.length ; i++) {
            if( preNum == arr[i]) {
                continue;
            } else {
                answer_al.add(arr[i]);
                preNum = arr[i];
            }
        }
        
        int[] answer = new int[answer_al.size()];
        for (int j=0 ; j<answer.length ; j++) {
            answer[j] = answer_al.get(j);
        }
        
        return answer;
    }
    
    
}