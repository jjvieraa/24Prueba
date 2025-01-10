
public class HelloWorld {  
    public static void main(String[] args) {  
        System.out.println("Hello, World!"); 
        int x = 10; // Integer  
        double y = 3.14; // Float (in Java: double)  
        String name = "Alice"; // String  
        boolean isStudent = true; // Boolean

        int age = 18;  
        if (age >= 18) {
            System.out.println("You are an adult");
        }   
        for (int i = 0; i < 5; i++) {  
            System.out.println(i);  
        }
        int count=0;
        while(count<5){
            System.out.println(count);
            count++;
        }
        greet("Alice");

        for (int i = 0; i < 5; i++) {  System.out.println(i);  
        }
   }  

   public static void greet(String name){
         System.out.println("Hello, " + name + "!"); 
   }
  /*  En Java, es común declarar métodos como públicos o privados, dependiendo de si deben ser llamados desde otras clases. Los métodos en Java también deben especificar el tipo de retorno (void si no se devuelve nada) y el tipo de datos de los parámetros.*/
}
 