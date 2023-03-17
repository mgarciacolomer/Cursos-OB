public class Main {
    public static void main(String[] args) {
        Persona p = new Persona();
        p.setNombre("Felipe");
        p.setEdad(45);
        p.setTelefono(687944551);

        System.out.println("El nombre es: " + p.getNombre());
        System.out.println("La edad es: " + p.getEdad());
        System.out.println("El telefono es: " + p.getTelefono());
    }
}

class Persona{
    private String nombre;
    private int edad;
    private int telefono;

    public int getEdad(){
        return this.edad;
    }

    public void setEdad(int edad){
        this.edad = edad;
    }

    public String getNombre(){
        return nombre;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono){
        this.telefono = telefono;
    }

}