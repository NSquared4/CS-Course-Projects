package Changeling;
import java.util.*;

public class Graph {

   private int count;
   private LinkedList<String>[] adjList;
      
   //constructor
   public Graph(int numVertices){
      adjList = new LinkedList[numVertices];
      for(int i = 0 ; i < numVertices; i++){
        adjList[i] = new LinkedList<String>();
      }
      count = 0;
   }
   
   public LinkedList<String> getContents(int index){
      return adjList[index];
   }
   
   //this method checks if two words are adjacent to one another
   static boolean isAdjacent(String base, String compare){
      int countCheck = 0;
      if(base.length() != compare.length()){
         return false;
      }
      for (int k = 0 ; k < base.length() ; k++){
         if (base.charAt(k) != compare.charAt(k)){
            countCheck++;
         }
      }
      if(countCheck == 1){
         return true;
      }
      else{
         return false;
      }
   }
   
   public LinkedList<String>[] listReturn(){
      return adjList;
   }
   
   //this method adds a vertex containing the word and then draws edges to all adjacent words
   public boolean addWord(String word){
      adjList[count].add(word);
      for(int j = 0 ; j < count; j++){
         if(Graph.isAdjacent(adjList[count].get(0), adjList[j].get(0))){
            adjList[count].add(adjList[j].get(0));
            adjList[j].add(adjList[count].get(0));
         }
      }
      count++;
      return true;
   }
   
   //this method takes a three-letter word and returns its location in adjList
   public int getLocation(String s){
      int where = 0;
      while(!(adjList[where].getFirst().contains(s))){
         where++;;
      }
      return where;
   }
   
   //this method takes a location in adjList and returns the corresponding word
   public String getWord(int w){
      return adjList[w].get(0);
   }
   
   //this method prints the adjacency list, each linked list on a new line
   public void printGraph(){
      for(int k = 0 ; k < adjList.length ; k++){
         for(int j = 0 ; j < adjList[k].size() ; j++){
            System.out.print(adjList[k].get(j));
         }
         System.out.println();
      }
   }

   
   public ArrayList BFS(int startWord, int endWord){
      ArrayList result = new ArrayList(); 
      boolean[] visited = new boolean[adjList.length];
      int[] parents = new int[adjList.length];
      for (int d = 0 ; d < adjList.length ; d++){
         parents[d] = -1;
      }
      Queue queue = new LinkedList<Integer>();
      queue.add(startWord);

      int currentWord = startWord;
      while(queue.size() != 0){
         currentWord = (int) queue.poll();
         if (currentWord == endWord){
            break;
         }
         for (int i = 0 ; i < adjList[currentWord].size() ; i++){
            if(visited[getLocation(adjList[currentWord].get(i))] == false){
               queue.add(getLocation(adjList[currentWord].get(i)));
               parents[getLocation(adjList[currentWord].get(i))] = currentWord;
               visited[getLocation(adjList[currentWord].get(i))] = true;
            }
        }
      }
      if(currentWord != endWord){
         return result;
      }
      else{
         //return the path to reach currentWord based on parents
         while (currentWord != startWord){
            result.add(currentWord);
            currentWord = parents[currentWord];
         }
      }
      return result;
      }   


}

