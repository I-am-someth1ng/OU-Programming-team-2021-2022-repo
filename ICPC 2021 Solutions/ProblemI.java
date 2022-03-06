import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class ProblemI {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int numRounds = scan.nextInt();
        int close = scan.nextInt();

        int players = (int)Math.pow(2.0, (double)numRounds);

        ArrayList<Integer> ratings = new ArrayList<>();

        for(int i = 0; i < players; i++) {
            ratings.add(scan.nextInt());
        }
        Collections.sort(ratings);

        int count = 0;
        int ratingDiff = 0;
        //I added


        int i, j;
        for(i = ratings.size() - 1; i > 1; i--) {
            for(j = 0; j <i ; j++) {

                ratingDiff = ratings.get(i) - ratings.get(j);
                ratingDiff = Math.abs(ratingDiff);

                if( ratingDiff <= close) {

                    //System.out.println(ratings.get(i) + "-" + ratings.get(j));
                    count++;

                    if(ratings.get(i) > ratings.get(j)) {
                        if(ratings.get(j) == Collections.min(ratings)){
                            ratings.remove(j);
                            i--;
                        }

                    }

                }


            }
        }

        System.out.println(count);
    }
}
