package Changeling;
import java.io.*; 
import java.util.*; 
import java.net.*;

public class createSmallWordList {

   public static ArrayList<String> threeWordList() throws FileNotFoundException{
      ArrayList<String> threeLetterWords = new ArrayList<String>();
      URL path = createSmallWordList.class.getResource("wordList.txt");
      File inputList = new File(path.getFile());
      Scanner sc = new Scanner(inputList);
      while(sc.hasNextLine()){
         String word = sc.nextLine();
         if(word.length() == 3){
            threeLetterWords.add(word);
            
         }
      }
      System.out.println(Arrays.toString(threeLetterWords.toArray()));
      return threeLetterWords;
   }

   public static void main(String[] args) throws FileNotFoundException {
      threeWordList();
   }


}