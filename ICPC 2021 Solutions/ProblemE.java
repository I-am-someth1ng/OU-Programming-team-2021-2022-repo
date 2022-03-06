import java.util.Scanner;
import java.util.ArrayList;
public class ProblemE
{

    public static void main()
    {
        Scanner input = new Scanner(System.in);
        int numStudents = input.nextInt();
        int numQuestions = input.nextInt();
        ArrayList<String> responses = new ArrayList<>(numStudents);
        int fewestXIndex = 0;
        int fewestXindexnum = -1;
        for(int i = 0 ; i < numStudents ; i++)
        {
            responses.add(input.next());
            int numxs = 0;
            for(int j = 0 ; j < numQuestions ; j++)
            {
                if(responses.get(i).charAt(j) == 'X')
                {
                    numxs++;
                }
            }
            if(numxs > fewestXindexnum)
            {
                fewestXindexnum = numxs;
                fewestXIndex = i;
            }
        }

        //generate all failing tests for one with lowest xs
        ArrayList<String> bestFails = new ArrayList<>();
        String bestTofail = responses.get(fewestXIndex);
        while(true)
        {
            /*for(i < )
            {

            }*/
        }



    }

}
