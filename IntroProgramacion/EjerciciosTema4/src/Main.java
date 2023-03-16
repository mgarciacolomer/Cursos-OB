public class Main {
    public static void main(String[] args) {
        int numeroIf = -5;

        if (numeroIf > 0)
            System.out.println("Es positivo");
        else if (numeroIf < 0)
            System.out.println("Es negativo");
        else
            System.out.println("Es cero");

        int numeroWhile = 0;
        while(numeroWhile < 3){
            System.out.println("El while dice: " + numeroWhile);
            numeroWhile++;
        }

        do{
            System.out.println("El do while dice: " + numeroWhile);
            numeroWhile++;
        }while(numeroWhile < 3);
        // No se cumple la condición, sólo se ejecuta una vez

        for (int numeroFor = 0; numeroFor <= 3; numeroFor++)
            System.out.println("El for dice: " + numeroFor);

        var Estacion = "PRIMAVERA";
        switch (Estacion){
            case "PRIMAVERA":
                System.out.println("Estamos en primavera");
                break;
            case "VERANO":
                System.out.println("Estamos en verano");
                break;
            case "OTOÑO":
                System.out.println("Estamos en otoño");
                break;
            case "INVIERNO":
                System.out.println("Estamos en invierno");
                break;
            default:
                System.out.println("Estacion no reconocida");

        }
    }
}