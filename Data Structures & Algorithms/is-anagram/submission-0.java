class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character,Integer> hs = new HashMap<>();
        HashMap<Character,Integer> ht = new HashMap<>();

        if (s.length()==t.length()){


            for(int i1=0; i1<s.length(); i1++){
                char x = s.charAt(i1);

                if (hs.containsKey(x)){
                    hs.put(x,hs.get(x)+1);
                }
                else{
                    hs.put(x,1);

                }
            }



            for(int i2=0; i2<t.length(); i2++){
                char x = t.charAt(i2);

                if (ht.containsKey(x)){
                    ht.put(x,ht.get(x)+1);
                }
                else{
                    ht.put(x,1);

                }
            }

            return hs.equals(ht);

        }
        else{
            return false;
        }

    }
}
