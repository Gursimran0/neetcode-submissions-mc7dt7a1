class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int s:stones){
            minHeap.offer(-s);
        }
        while (minHeap.size()>1){
            int x = minHeap.poll();
            int y = minHeap.poll();
            if (x==y){
                continue;
            }
            else if (y>x){
                minHeap.offer(x-y);
            }
        }
        minHeap.offer(0);
        return Math.abs(minHeap.peek());
    }
}
