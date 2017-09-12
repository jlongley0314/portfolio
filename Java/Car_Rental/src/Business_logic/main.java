package Business_logic;

import UserInterface.CustomerFrame;
import java.util.ArrayList;
import java.util.List;
import java.text.ParseException;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Shazam
 */
public class main {
    public static void main(String[] args) throws ParseException{
         List<Customer> customers = new ArrayList();
        customers.add(new Customer("1","Samir James", "816-878-1111", "6102 NE Antioch Rd"));
        customers.add(new Customer("2","Kim Sam", "816-847-888", "7123 Main Street"));
        customers.add(new Customer("3","Mehmet Scholl", "816-444-2387", "12 Rockhil Rd"));
        
        // List of cars in the system
        List<Car> cars = new ArrayList<>();
        cars.add(new Car("5321", new CarSpec("Altima", "Nissan", 2012, Size.small)));
        cars.add(new Car("4874", new CarSpec("Altima", "Nissan", 2012, Size.midsize)));
        cars.add(new Car("1234", new CarSpec("Passat", "Volks Wagen", 2002, Size.large)));
        cars.add(new Car("5321", new CarSpec("Benz", "Mercedes", 2000, Size.midsize)));
        cars.add(new Car("5123", new CarSpec("Hundai", "", 2011, Size.midsize)));
        cars.add(new Car("4196", new CarSpec("Hundai", "", 2010, Size.small)));
        cars.add(new Car("2721", new CarSpec("Benz", "Mercedes", 2010, Size.large)));
        
        // List of rental for above cars
        List<Rental> rentalList = new ArrayList<>();
        Rental rental1 = new Rental("01/12/12","01/15/12", cars.get(0), Status.returned);
        Rental rental2 = new Rental("01/12/12","01/16/12", cars.get(1), Status.returned);
        Rental rental3 = new Rental("05/06/12","05/06/12", cars.get(2), Status.returned);
        Rental rental4 = new Rental("01/01/10","01/12/10", cars.get(3), Status.returned);
        Rental rental5 = new Rental("04/18/12","04/23/12", cars.get(4), Status.rented);
        Rental rental6 = new Rental("11/21/12","11/25/12", cars.get(5), Status.rented);
        Rental rental7 = new Rental("01/12/12","01/15/12", cars.get(6), Status.rented);
        
        // Add the rental to the car
        cars.get(0).addRental(rental1);
        cars.get(1).addRental(rental2);
        cars.get(2).addRental(rental3);
        cars.get(3).addRental(rental4);
        cars.get(4).addRental(rental5);
        cars.get(5).addRental(rental6);
        cars.get(6).addRental(rental7);
        
        rentalList.add(rental1);
        rentalList.add(rental2);
        rentalList.add(rental3);
        rentalList.add(rental4);
        rentalList.add(rental5);
        rentalList.add(rental6);
        rentalList.add(rental7);
        
        // Add the list of rental to first cusotmer
        for (Rental r : rentalList) {
            customers.get(0).addRental(r);
        }
            
        CarRentalSystem system = new CarRentalSystem();
        system.addAllCars(cars);
        CustomerFrame cf = new CustomerFrame(system, customers);
        cf.setVisible(true);
    
    }
}
