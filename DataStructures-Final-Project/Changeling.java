package Changeling;
import java.io.*; 
import java.util.*; 
import java.net.*;

public class Changeling {

   public static ArrayList<String> threeWordList(String inputFile) throws FileNotFoundException{
      ArrayList<String> threeLetterWords = new ArrayList<String>();
      URL path = createSmallWordList.class.getResource(inputFile);
      File inputList = new File(path.getFile());
      Scanner sc = new Scanner(inputList);
      while(sc.hasNextLine()){
         String word = sc.nextLine();
         if(word.length() == 3){
            threeLetterWords.add(word);
         }
      }
      //System.out.println(Arrays.toString(threeLetterWords.toArray()));
      return threeLetterWords;
   }
   
   public static Graph makeGraph(ArrayList<String> wordList){
      Graph wordGraph = new Graph(wordList.size());
         for(int i = 0 ; i < wordList.size() ; i ++){
            wordGraph.addWord(wordList.get(i));
            //wordGraph = Graph.listReturn();
         }
      return wordGraph;
   }

   public static String[] changePath(Graph wordGraph, ArrayList list){
      String[] result = new String[list.size()];
      for(int i = 0 ; i < list.size() ; i++){
         result[list.size() - (i+1)] = wordGraph.getWord((int) list.get(i));
      }
      
      return result;
   }

   public static void main(String[] args) throws FileNotFoundException{
     System.out.println("Please enter the name of the file followed by two three-letter words, each term separated by a space.");
     System.out.println("If you are using the directory we wrote this program in, the name of the file will be wordList.txt.");
     Scanner in = new Scanner(System.in);
     String[] words = in.nextLine().split(" ");
     String filename = words[0];
     ArrayList<String> wordList = threeWordList(filename);
     System.out.println(filename);
     System.out.println(words[1] + " " + words[2]);
     if((words.length == 3) && (wordList.contains(words[1])) && (wordList.contains(words[2]))){
         Graph wordGraph = makeGraph(wordList);
         //wordGraph.printGraph();
         int fromWord = wordGraph.getLocation(words[1]);
         int toWord = wordGraph.getLocation(words[2]);
         //System.out.println(wordGraph.getContents(3).get(0));
         //System.out.println(fromWord + " " + toWord);
         ArrayList path = new ArrayList();
         path = wordGraph.BFS(fromWord, toWord);
         String[] finalPath = changePath(wordGraph, path);
         System.out.println("The path from " + words[1] + " to " + words[2] + " takes the following path: ");
         System.out.println(Arrays.toString(finalPath));
     }
     else{
         System.out.println("Please only enter two lowercase three-letter words following the name of the dictionary file, each term separated by one space"); 
     }
     
   }
}

