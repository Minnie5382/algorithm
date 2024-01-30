class Solution {
    public int solution(String[] order) {
        int price = 0;
        
        for (String o : order) {
            if (o.contains("americano") || o.contains("anything")) {
                price += 4500; 
            } else {
                price += 5000;
            }
        }
        return price;
    }
}