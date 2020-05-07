import java.util.StringTokenizer;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.lang.*;

/*
   1. 아래와 같은 명령어를 입력하면 컴파일이 이루어져야 하며, Solution4 라는 이름의 클래스가 생성되어야 채점이 이루어집니다.
       javac Solution2.java -encoding UTF8


   2. 컴파일 후 아래와 같은 명령어를 입력했을 때 여러분의 프로그램이 정상적으로 출력파일 output4.txt 를 생성시켜야 채점이 이루어집니다.
       java Solution2

   - 제출하시는 소스코드의 인코딩이 UTF8 이어야 함에 유의 바랍니다.
   - 수행시간 측정을 위해 다음과 같이 time 명령어를 사용할 수 있습니다.
       time java Solution2
   - 일정 시간 초과시 프로그램을 강제 종료 시키기 위해 다음과 같이 timeout 명령어를 사용할 수 있습니다.
       timeout 0.5 java Solution2   // 0.5초 수행
       timeout 1 java Solution2     // 1초 수행
 */

class Solution2 {

    /*
        ** 주의사항
        정답의 숫자가 매우 크기 때문에 답안은 반드시 int 대신 long 타입을 사용합니다.
        그렇지 않으면 overflow가 발생해서 0점 처리가 됩니다.
        Answer[0]을 a의 개수, Answer[1]을 b의 개수, Answer[2]를 c의 개수라고 가정했습니다.
    */
    static int n;                           // 문자열 길이
    static String s;                        // 문자열
    static long[] Answer = new long[3];     // 정답

    public static void main(String[] args) throws Exception {
		/*
		   동일 폴더 내의 input2.txt 로부터 데이터를 읽어옵니다.
		   또한 동일 폴더 내의 output4.txt 로 정답을 출력합니다.
		 */
        BufferedReader br = new BufferedReader(new FileReader("input2.txt"));
        StringTokenizer stk;
        PrintWriter pw = new PrintWriter("output2.txt");

		/*
		   10개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		 */
        for (int test_case = 1; test_case <= 10; test_case++) {
			/*
			   각 테스트 케이스를 파일에서 읽어옵니다.
               첫 번째 행에 쓰여진 문자열의 길이를 n에 읽어들입니다.
               그 다음 행에 쓰여진 문자열을 s에 한번에 읽어들입니다.
			 */
            stk = new StringTokenizer(br.readLine());
            n = Integer.parseInt(stk.nextToken());
            s = br.readLine();

//            System.out.println(n);
//            System.out.println(string);

            long [][] resA = new long[n+1][n+1]; // resA[i][j] , s의 i~j 까지 a가 나오는 경우
            long [][] resB = new long[n+1][n+1]; // resB[i][j] , s의 i~j 까지 b가 나오는 경우
            long [][] resC = new long[n+1][n+1]; // resC[i][j] , s의 i~j 까지 c가 나오는 경우

            for (int i=0; i<n; ++i){ // string [i][i]는 그 글자 하나만 해당 되므로, 그 해당글자의 arr count 를 늘려준다

                if (s.charAt(i)=='a') resA[i+1][i+1]= 1;
                else if (s.charAt(i)=='b') resB[i+1][i+1]= 1;
                else if (s.charAt(i)=='c') resC[i+1][i+1]= 1;

            }

            for (int i=1; i<=n-1; ++i){
                for (int j=1; j<=n-i; ++j){
                    int k = i+j;
                    for (int l=j; l<=k-1; ++l){
                        resA[j][k] += (resA[j][l] * resC[l+1][k]) + (resB[j][l] * resC[l+1][k]) + (resC[j][l] * resA[l+1][k]);
                        resB[j][k] += (resA[j][l] * resA[l+1][k]) + (resA[j][l] * resB[l+1][k]) + (resB[j][l] * resB[l+1][k]);
                        resC[j][k] += (resB[j][l] * resA[l+1][k]) + (resC[j][l] * resB[l+1][k]) + (resC[j][l] * resC[l+1][k]);
                    }
                }
            }


            /////////////////////////////////////////////////////////////////////////////////////////////
			/*
			   이 부분에서 여러분의 알고리즘이 수행됩니다.
			   정답을 구하기 위해 주어진 문자열 s를 여러분이 원하시는 대로 가공하셔도 좋습니다.
			   문제의 답을 계산하여 그 값을 Answer(long 타입!!)에 저장하는 것을 가정하였습니다.
			 */

			/*

	        행렬의 곱셈 순서와 비슷하게 접근
	        마지막 덩어리(?)의 곱셈이 수행되는 상황?
	        <n-1가지의 가능성>

	        1번째     S(1) * { S(2) * S(3) * ... S(n) }
	        2번째     { S(1)*S(2) } * { S(3)*..*S(n) }
	        ...
	        n-1번쨰   { S(1)*S(2)...*S(n-1) } * S(n)

	        따라서 A(ij), B(ij), C(ij)를 다음과 같이 표현할 수 있음
	        A(ij) : S(i)부터 S(j) 까지의 곱이 'a'가 되는 경우의 수
	        B(ij) : S(i)부터 S(j) 까지의 곱이 'b'가 되는 경우의 수
	        C(ij) : S(i)부터 S(j) 까지의 곱이 'c'가 되는 경우의 수

	        재귀적으로 표현하면,      A(ij) :  if (i=j) 그냥 1, else A(ik)*C(kj)+ B(ik)*C(kj) + C(ik)*A(kj) 이렇게
	            a   b   c
	        a   b   b   a
	        b   c   b   a
	        c   a   c   c

	     
			 */





            /////////////////////////////////////////////////////////////////////////////////////////////
            Answer[0] = resA[1][n];  // a 의 갯수
            Answer[1] = resB[1][n];  // b 의 갯수
            Answer[2] = resC[1][n];  // c 의 갯수


            // output4.txt로 답안을 출력합니다.
            pw.println("#" + test_case + " " + Answer[0] + " " + Answer[1] + " " + Answer[2]);
			/*
			   아래 코드를 수행하지 않으면 여러분의 프로그램이 제한 시간 초과로 강제 종료 되었을 때,
			   출력한 내용이 실제로 파일에 기록되지 않을 수 있습니다.
			   따라서 안전을 위해 반드시 flush() 를 수행하시기 바랍니다.
			 */
            pw.flush();
        }

        br.close();
        pw.close();
    }
}

