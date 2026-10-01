class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> hm = new HashMap<>();
        int[] result = new int[k];
        PriorityQueue<Integer> p = new PriorityQueue<>(
            (a,b) -> hm.get(a)-hm.get(b)
        );

        for(int num:nums){
            if(hm.containsKey(num)){
                hm.put(num,hm.get(num)+1);
            }
            else{
                hm.put(num,1);
            }
        }

        for(int n: hm.keySet()){
            p.add(n);
            if (p.size() > k) {
                p.poll();
            }
        }

        for (int i = 0; i < k; i++) {
            result[i] = p.poll();
        }

        return result;




    }
}
