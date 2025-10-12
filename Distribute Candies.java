class Solution {
    private int moves;  // global counter for total moves
    
    public int distCandy(Node root) {
        moves = 0;
        dfs(root);
        return moves;
    }
    
    private int dfs(Node node) {
        if (node == null) return 0;
        
        int left = dfs(node.left);
        int right = dfs(node.right);
        
        // total moves are sum of absolute transfers from children
        moves += Math.abs(left) + Math.abs(right);
        
        // net balance of candies for this subtree
        return node.data + left + right - 1;
    }
}
