class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        // sort
        for (int i=0 ; i<d.length-1 ; i++) {
            for(int j=i+1 ; j<d.length ; j++) {
                if (d[i] > d[j]) {
                    int tmp = d[j];
                    d[j] = d[i];
                    d[i] = tmp;
                }
            }
        }
        
        for (int i : d) {
            budget -= i;
            if (budget >= 0) {
                answer ++;
            } else {
                break;
            }
        }

        return answer;
    }
}