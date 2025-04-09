import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

public class main {
    public static void Main(String[] args) {
      Map<String, BigDecimal> ratesMap = new HashMap<>();
      Scanner input = new Scanner(System.in);
        
        try {
            // Input amount
            System.out.print("Enter the amount: ");
            BigDecimal amount = new BigDecimal(input.nextLine());

            // Input province
            System.out.print("Enter the province code: ");
            String prov = input.nextLine();

            ratesMap.put("BC", new BigDecimal(0.12));
            ratesMap.put("MN", new BigDecimal(0.12));
            ratesMap.put("ON", new BigDecimal(0.13));
            ratesMap.put("QC", new BigDecimal(0.14975));
            ratesMap.put("AB", new BigDecimal(0.05));
            ratesMap.put("YT", new BigDecimal(0.05));
            ratesMap.put("NT", new BigDecimal(0.05));
            ratesMap.put("NU", new BigDecimal(0.05));
            ratesMap.put("SK", new BigDecimal(0.11));
            ratesMap.put("PEI", new BigDecimal(0.15));
            ratesMap.put("NS", new BigDecimal(0.15));
            ratesMap.put("NL", new BigDecimal(0.15));
            ratesMap.put("NB", new BigDecimal(0.15));
            ratesMap.put("PEI", new BigDecimal(0.15));
            BigDecimal totalbig = amount.multiply(ratesMap.get(prov)).add(amount);
            BigDecimal total = totalbig.setScale(2, RoundingMode.HALF_UP);
            System.out.println(total);
    } catch (Exception e) {
      System.out.println(e);
    } finally {
      input.close();
    }
    }
  }
