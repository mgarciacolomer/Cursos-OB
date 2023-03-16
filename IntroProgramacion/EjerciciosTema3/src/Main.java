public class Main {
    public static void main(String[] args) {
        Coche c1 = new Coche();
        int n1 = 1;
        int n2 = 2;
        int n3 = 3;
        int res;

        System.out.println("PRIMERA PARTE");
        res = suma(n1, n2, n3);  // Llamada a suma
        System.out.println("La suma de los números es: " + res);

        System.out.println("SEGUNDA PARTE: ");


        System.out.println("El número de puertas original es: " + c1.num_puertas); // Puertas antes de incrementar
        c1.IncrementaPuertas();
        System.out.println("El número de puertas después de incrementar es: "+ c1.num_puertas);

    }
    public static int suma (int a, int b, int c){
        return a + b + c;
    }
}

class Coche{
    public int num_puertas = 5;

    public void IncrementaPuertas(){
        this.num_puertas++;
    }
}