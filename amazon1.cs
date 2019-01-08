using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {
    
    public class Point{
     public int x;
     public int y;
     public Point(int x, int y) {
         this.x = x;
         this.y = y;
     }
}

    // Complete the reverseArray function below.
    public  List<List<int>> ClosestXDestinations(int numDestinations, int[,] allocations, int numDeliveries) {
        Point[] points = new Point[numDestinations];
        for(int i=0;i<numDestinations; ++i){
            Point p = new Point(allocations[i,0],allocations[i,1]);
            points[i]=p;
        }
        Point origin = new Point(0,0);
        Point[] result = findKClosestPoints(points, numDeliveries, origin);
        
        List<List<int>> final_result = new List<List<int>>();
        
        for(int i=0; i< result.Length; ++i){
            List<int> point = new List<int>();
            point.Add(result[i].x);
            point.Add(result[i].y);
            final_result.Add(point);
        }
        return final_result;
    }
    
    
   public Point[] findKClosestPoints(Point[] points, int k, Point target) {
    if (points.Count() == 0 || k < 1 || k > points.Count()){
        return points;
    }   
    int left = 0;
    int right = points.Count() - 1;
    while (true) {
        int pos = partition(points, left, right, target);
        if (pos == k - 1){
            break;
        } 
        else{
            if (pos > k - 1){
                   right = pos - 1;
            }else{
                   left = pos + 1;       
            }
        }
    }
       
    Point[] res = new Point[k];
    for (int i = 0; i < k; i++)
        res[i] = points[i];
    return res;
}
    
    public int partition(Point[] points, int left, int right, Point target) {
    //shuffle(points);
    int idx = left;
    Point pivot = points[idx];
    int pDist = getDistance(pivot, target);
    swap(points, idx, right);
    for (int i = left; i < right; i++) {
        int iDist = getDistance(points[i], target);
        if (iDist < pDist){
            swap(points, i, idx++);
        }
    }
    swap(points, idx, right);
    return idx;
}

public int getDistance(Point p, Point target) {
    return (p.x - target.x) * (p.x - target.x) + (p.y - target.y) * (p.y - target.y);
}

public static void swap(Point[] points, int left, int right) {
     Point temp = points[left];
     points[left] = points[right];
     points[right] = temp;
}



    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int[,] allocations = new int[3,2]{{1,-3},{1,2},{3,4}};
        Solution sol =new Solution();
        List<List<int>> res = sol.ClosestXDestinations(3,allocations,1);

        //textWriter.WriteLine(string.Join(" ", res));

        textWriter.Flush();
        textWriter.Close();
    }
}
