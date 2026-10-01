class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();

        for(String str:strs){
            int n = str.length();
            encoded.append(n).append("#").append(str);
        }

        return encoded.toString();

    }

    public List<String> decode(String str) {

        int i = 0;
        List<String> al = new ArrayList<>();

        while (i<str.length()){
            int i2 = str.indexOf('#',i);
            int n = Integer.parseInt(str.substring(i,i2));
            al.add(str.substring(i2+1,i2+1+n));
            i = i2+1+n;

        }
        return al;


    }
}
