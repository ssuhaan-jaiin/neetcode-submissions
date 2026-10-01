class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> mai = new HashMap<>();

        for(String start : strs){
            char[] chars = start.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            if(mai.containsKey(key)){
                mai.get(key).add(start);
            }
            else{
                List<String> list = new ArrayList<>();
                list.add(start);
                mai.put(key, list);
            }
            
        }
        return new ArrayList<>(mai.values());

        
    }
}
