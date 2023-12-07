package Options;

import Models.Polynomial;

import java.util.ArrayList;
import java.util.List;

public class SequentialClassic {
    public static Polynomial multiply(Polynomial poly1, Polynomial poly2) {
        List<Integer> coefficients1 = poly1.getCoefficients();
        List<Integer> coefficients2 = poly2.getCoefficients();
        int degree1 = poly1.getDegree();
        int degree2 = poly2.getDegree();

        List<Integer> resultCoefficients = new ArrayList<>();
        for (int i = 0; i <= degree1 + degree2; i++) {
            resultCoefficients.add(0);
        }


        for (int i = 0; i <= degree1; i++) {
            for (int j = 0; j <= degree2; j++) {
                int coeffProduct = coefficients1.get(i) * coefficients2.get(j);
                resultCoefficients.set(i + j, resultCoefficients.get(i + j) + coeffProduct);
            }
        }

        return new Polynomial(resultCoefficients);
    }
}
