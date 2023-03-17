public class Main {
    public static void main(String[] args) {
        Cliente c = new Cliente();
        c.nombre = "Manolo";
        c.edad = 40;
        c.telefono = 654487911;
        c.credito = 465.11;

        System.out.println("DATOS DEL CLIENTE:");
        System.out.println("Nombre: " + c.nombre);
        System.out.println("Edad: " + c.edad);
        System.out.println("Telefono: " + c.telefono);
        System.out.println("Credito: " + c.credito);

        Trabajador t = new Trabajador();
        t.nombre = "Hermenegildo";
        t.edad = 33;
        t.telefono = 687444411;
        t.salario = 1825.01;

        System.out.println("DATOS DEL TRABAJADOR:");
        System.out.println("Nombre: " + t.nombre);
        System.out.println("Edad: " + t.edad);
        System.out.println("Telefono: " + t.telefono);
        System.out.println("Salario: " + t.salario);
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



