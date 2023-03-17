public class Main {
    public static void main(String[] args) {
        Cliente c = new Cliente();
        c.nombre = "Manolo";
        c.edad = 40;
        c.telefono = 654487911;
        c.credito = 465.11;

        System.out.println("El cliente es: " + c.nombre + " de edad " + c.edad + ", telefono " + c.telefono
                + " y dispone de un credito de " + c.credito);
        Trabajador t = new Trabajador();
        t.nombre = "Hermenegildo";
        t.edad = 33;
        t.telefono = 687444411;
        t.salario = 1825.01;

        System.out.println("El trabajador es: " + t.nombre + " de edad " + t.edad + ", telefono " + t.telefono
                + " y tiene un salario de " + t.salario);
    }
}

class Persona{
    String nombre;
    int edad;
    int telefono;
}

class Cliente extends Persona{
    double credito;
}

class Trabajador extends Persona{
    double salario;
}



