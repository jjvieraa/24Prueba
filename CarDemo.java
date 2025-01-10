public class CarDemo{
    public static void main(String[] args) {  
        Car myCar = new Car("BMW", 2020);  
        myCar.drive();
        Car2 myCar2= new Car2();
        myCar2.brand="VW";
        myCar2.year=2024;
        myCar2.drive();
        myCar2.muestra();
    }  
}
