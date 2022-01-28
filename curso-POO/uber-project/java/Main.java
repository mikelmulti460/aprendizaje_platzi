
class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        UberX uberX = new UberX("AIR15278", new Account("Adrian", "ADN2135"), "Tesla", "modelB");
        uberX.setPassenger(5);
        uberX.printDataCar();

        /*Car car2 = new Car("QWE567", new Account("Mikel Aranda", "MARANDA548"));
        car2.passenger = 2;
        car2.printDataCar();*/

        UberVan uberVan = new UberVan("miafw29", new Account("mikel", "169a4fa"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();
        
    }
}