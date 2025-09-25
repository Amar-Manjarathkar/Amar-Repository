// User function Template for Java

// User function Template for Java

class Solution {
    public int minimumApple(int[] arr) {
        // Complete the function
        Set<Integer> st =  new HashSet<>();
        for(int i: arr){
            st.add(i);
        }
        
        return st.size();
    }
}
