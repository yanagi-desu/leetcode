import java.util.*;

class main {
    public static void main(String [] args){
        Solution_684 solution = new Solution();
        solution.solve(null);
        System.out.println("Hi");
    }
}


class Solution_684 {
    public int[] solve(int[][] edges){
        int[] parent = new int[2001];
        for(int i=0;i<parent.length;i++) parent[i] = i;
        for(int[] each: edges){
            if(findparent(parent, each[0])==findparent(parent, each[1])){
                return each;
            }
            union(each[0],each[1],parent);
        }
        return new int[2];
    }

    private int findparent(int[] parent, int find){
        if(parent[find]!=find){
            parent[find] = findparent(parent,parent[find]);
        }
        return parent[find];
    }

    private void union(int a, int b, int[] parent){
        int roota = findparent(parent, a);
        int rootb = findparent(parent, b);
        if (roota == rootb) return;
        parent[roota] = parent[rootb];
    }
}
