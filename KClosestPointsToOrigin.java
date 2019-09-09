//We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

//(Here, the distance between two points on a plane is the Euclidean distance.)

//You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)


class Solution {
    public int[][] kClosest(int[][] points, int K) {
        if (points.length == K){
            return points;
        }
        HashMap<Double,int[]> map = new HashMap<Double,int[]>();
        for (int[] point : points){
            double distance = Math.sqrt((point[0]*point[0]) + (point[1]*point[1]));
            if (map.containsKey(distance)){
                map.put(distance+0.01,point);
            }
            else{
            map.put(distance,point);
            }
        }
        
        int[][] result = new int[K][];
        ArrayList<Double> distances = new ArrayList<Double>();
        for (double d: map.keySet()){
            distances.add(d);
        }
        Collections.sort(distances);
        
        
        for (int i=0; i<K; i++){
            result[i] = map.get(distances.get(i));
        }
        
        
        return result;
    }
}