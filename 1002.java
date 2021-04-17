import java.util.*;

class main {
    public static void main(String[]args){
        System.out.println("Hi");
    }

    class solve{
        public List<String> solve1002(String[] A){
            int[] count = new int[26];
            Arrays.fill(count, Integer.MAX_VALUE);
            for(String each:A){
                int[] cnt = new int[26];
                each.chars().forEach(c -> ++cnt[c-'a']); 
                for(int i=0;i<26;i++) count[i] = Math.min(count[i], cnt[i]);
            }
            List<String> ans = new ArrayList<>();
            for(int i=0;i<26;i++){
                while(count[i]-->0){
                    ans.add(Character.toString('a'+i));
                }
            }
            return ans;
        }
    }
}

