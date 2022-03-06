import java.awt.geom.RectangularShape;
import java.util.Scanner;
public class ProblemK
{
    public static void main(String[] ags)
    {
        Scanner input = new Scanner(System.in);
        int num_people = input.nextInt();

        int result = num_people / 3;
        if(result > 3)
        {
            System.out.println(3);
        }
        else if(result < 1)
        {
            System.out.println(1);
        }
        else
        {
            System.out.println(result);
        }

    }


}
