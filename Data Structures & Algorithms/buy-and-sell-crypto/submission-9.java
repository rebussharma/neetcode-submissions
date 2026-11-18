class Solution {
    public int maxProfit(int[] prices) {
        /*
            10 1 5 6 7 1

        */
        int r = 1;
        int l = 0;
        int mp = 0;

        while (r < prices.length){
            if(prices[l] > prices[r]){
                l = r;
                r += 1;
                if (r >= prices.length) return mp;
            }
            int currentProfit = prices[r] - prices[l];
            mp = (currentProfit > mp) ? currentProfit : mp;
            r += 1;
        }

        return mp;
    }
}
