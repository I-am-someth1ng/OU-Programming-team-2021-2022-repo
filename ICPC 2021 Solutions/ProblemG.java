import java.util.Scanner;
import java.util.ArrayList;
public class ProblemG
{
    public static void  main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        String alphabet = input.nextLine();
        String queryString = input.nextLine();
        int numQuerys = input.nextInt();
        ArrayList<String> queries = new ArrayList<>(numQuerys);

        for(int i = 0 ; i < numQuerys ; i++)
        {
                 queries.add(input.nextLine());
        }


        for(int i = 0 ; i < numQuerys ; i++)
        {
            int pointerInString = 0;
            String currentQuery = queries.get(i);
            if(alphabet.length() != currentQuery.length())
            {
                System.out.println(0);
            }
            else
            {
                boolean fail = false;
                for (int j = 0; j < queryString.length(); j++)
                {
                    if (currentQuery.charAt(pointerInString) == queryString.charAt(j))
                    {
                        pointerInString++;
                        if (pointerInString >= currentQuery.length())
                        {
                            System.out.println(0);
                            fail = true;
                            break;
                        }
                    }
                    else
                    {

                    }
                }
                if(!fail)
                {
                    System.out.println(1);
                }
            }
        }

    }
}
