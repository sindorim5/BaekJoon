public class day5_ex_부분집합합10 {
    
    public static int count_ans = 1;
    public static int cnt;
    public static int [] a = new int [11];
    public static int Depth = 10;
    
    public static void process_solution(int a[], int k)
    {
        int sum = 0;
    
        for (int i = 0; i <= k; i++)
            if (a[i] == 1) sum += i;
    
        if (sum == 10)
        {
            System.out.printf("%d : (", count_ans++);
            for (int i = 0; i <= k; i++)
                if (a[i] == 1)
                    System.out.printf(" %d", i);
            System.out.printf(")\n");
        }
    }
    
    public static void backtrack(int k)
    {
        cnt++;
    
        if (k == Depth)  process_solution(a, k);
        else
        {
            a[++k] = 1;  backtrack(k);
            a[k] = 0;  backtrack(k);
        }
    }

    public static void main(String[] args) 
    {

        backtrack(0);

        System.out.printf("count : %d\n", cnt);
    }
}






//int sum = 0;
//a[++k] = 1;  
//
//for (int j = 0; j <= k; j++) 
//    if (a[j] == 1) sum += j;
//
//if (sum <= 10) backtrack(k);
//
//a[k] = 0;  backtrack(k);