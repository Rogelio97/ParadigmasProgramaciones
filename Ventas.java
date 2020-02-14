/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercio3poo;

/**
 *
 * @author Espar
 */
public class Ventas extends Clientes {
    
     String nombrefru;
     String descripcion;
     float precio;

    public  Ventas(String nombres, String apellido, int edad, String correo, String telefono, String nombrefru, String descripcion, float precio) {
        super(nombres, apellido, edad, correo, telefono);
        this.nombrefru = nombrefru;
        this.descripcion = descripcion;
        this.precio = precio;
    }

   

   
     public void mostrardatos() {
        System.out.println("Nombre del cliente" + getNombres()
                + "\n" + getApellido()
                + "\n" + getEdad()
                + "\n" + getTelefono()
                + "\n" + getCorreo()
        );

        System.out.println("Lo que se compro es");
        System.out.println(nombrefru
                + "\n" + descripcion
                + "\n" + precio);

    }

}
