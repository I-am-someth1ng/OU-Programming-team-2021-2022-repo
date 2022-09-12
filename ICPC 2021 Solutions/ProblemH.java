import java.util.Scanner;
import java.util.HashMap;
public class ProblemH
{

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int testCases = input.nextInt();

        String currentCase = "";
        String result = "";
        HashMap<Character,Integer> lettertoNum = new HashMap<Character, Integer>();

        lettertoNum.put('J',0);
        lettertoNum.put('L',1);
        lettertoNum.put('S',2);
        lettertoNum.put('Z',3);
        lettertoNum.put('I',4);
        lettertoNum.put('O',5);
        lettertoNum.put('T',6);

        //outermost for loop handles each test case individually
        boolean[] pieces = new boolean[7];

        for(int i = 0 ; i < pieces.length ; i++)
        {
            pieces[i] = true;
        }

        for(int caseNum = 0 ; caseNum < testCases ; caseNum++)
        {
            currentCase = input.next();
            boolean exit = false;
            boolean first7 = true;
            boolean first7reset = false;
            //int sevenCounter = 0;
            int dontrefresh = -1;
            for(int i = 0 ;( i < currentCase.length() ) && (exit == false); i++)
            {


                if(pieces[lettertoNum.get(currentCase.charAt(i))] == false)
                {
                    if(first7)
                    {
                        first7 = false;
                        first7reset = true;
                        dontrefresh = lettertoNum.get(currentCase.charAt(i));
                    }
                    else
                    {
                        //System.out.println("0");
                        result = result + "0\n";
                        exit = true;
                    }

                }
                else
                {
                    pieces[lettertoNum.get(currentCase.charAt(i))] = false;
                }

                //reset array to all true
                if( ( ( (i%7) == 0) && (i!=0) )   || (first7reset) )
                {
                    first7reset = false;
                    first7 = false;

                    for (int T = 0; T < pieces.length; T++)
                    {

                        pieces[T] = true;
                    }
                    if(dontrefresh >-1)
                    {
                        pieces[dontrefresh] = false;
                    }
                }

            }

            if (exit == false)
            {
                //System.out.println("1");
                result = result + "1\n";
            }
            //reset array to all true
            for(int T = 0 ; T < pieces.length ; T++)
            {
                pieces[T] = true;
            }

        }
        System.out.println(result.strip());
    }

}
