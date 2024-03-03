import java.util.Scanner;

public class questions {
    public static int[] powFind(int number) {
        int[] arr = new int[20]; // Assuming the maximum number of powers is 20
        int position = 0;int count =0;// Initialize count and position

        for (int i = 0; i < 20 ; i++) {
            int power = (int) Math.pow(2, i); // Calculate the power of 2
            if (number % 2 == 1) { // If the remainder is 1
                arr[position++] = power; // Set the current power of 2
            }
            number /= 2;
        }
        for (int element : arr){
            if (element!=0){count++;}
        }
        int [] powers = new int[count];count = 0;
        for (int e : arr){if (e!=0){powers[count] = e;count++;}}

        return powers;
    }
    static void eval(){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        sc.close();
        String [] str = input.split(" ");
        int sum = 0;int val =0;
        int N = Integer.parseInt(str[0]);// Converting string to integer from list
        int K = Integer.parseInt(str[1]);
        int diff = K-N;

        System.out.print(powFind(diff).length);
    }
    public static void main(String[] args)  throws java.lang.Exception{
        eval();
    }
}
