import java.io.*;
import java.util.*;


public class Main {
	
	static int n;
	static List<BaseBallData> inputData = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		//입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		n = Integer.parseInt(s);
		
		for (int i = 0; i<n; i++) {
			s = br.readLine();
			StringTokenizer st = new StringTokenizer(s, " ");
			int check = Integer.parseInt((st.nextToken()));
			int strike = Integer.parseInt((st.nextToken()));
			int ball = Integer.parseInt((st.nextToken()));
			
			BaseBallData baseBallData = new BaseBallData(check, strike, ball);
			inputData.add(baseBallData);
			
		}
		System.out.println(callBaseBall());
		
	}
	
	static int callBaseBall() {
		int result = 0;
		
		for (int i = 123; i<=987;i++) {
				if(!checkSameNum(i)) continue;
			
			
			int allTestPass = 0;
			
			for (int j = 0; j < n; j++) {
				int strikeCount = 0;
				int ballCount =0;
				
				BaseBallData current = inputData.get(j);
				String currentDataString = Integer.toString(current.check);
				String myDataString = Integer.toString(i);
				
				for (int k = 0; k < 3 ; k++) {
					if (currentDataString.charAt(k) == myDataString.charAt(k)) {
						strikeCount++;
					}
				}
				
				for (int h = 0; h < 3;h++) {
					for (int u = 0; u <3; u++) {
						if(myDataString.charAt(h) == currentDataString.charAt(u)) {
							if (h != u)
								ballCount++;
						}
					}
				}
				
				if (current.strike == strikeCount && current.ball == ballCount) {
					allTestPass++;
				}			
			}
			if (allTestPass ==n) {
				result ++;
			}
		}
		return result;
	}
	
	
	static boolean checkSameNum(int num) {
		
		String numString = Integer.toString(num);
		
		if (numString.charAt(0) == numString.charAt(1)) {
			return false;
		}
		if (numString.charAt(1) == numString.charAt(2)) {
			return false;
		}
		if (numString.charAt(2) == numString.charAt(0)) {
			return false;
		}
		if (numString.charAt(0) == '0' || numString.charAt(1) == '0' || numString.charAt(2) == '0')
            return false;
		
		return true;
		
	}
	
	static class BaseBallData{
		int check;
		int strike;
		int ball;
		
		public BaseBallData(int check, int strike, int ball) {
			this.check = check;
			this.strike = strike;
			this.ball = ball;
		}
	}

}
