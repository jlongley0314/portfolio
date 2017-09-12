/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

import java.util.List;
import java.util.LinkedList;

/**
 *
 * @author Shazam
 */

//Main Class that talks to other classes
public class CarRentalSystem {
    List<Car> carList;
    List<Customer> customerList;

    public CarRentalSystem() {
        carList = new LinkedList();
        customerList = new LinkedList();
    }
 
    public List<Car> getCarList() {
        return this.carList;
    }
    
    public List<Customer> getCustomerList(){
        return customerList;
    }
    
    public void addCar(String make, String model, int year, Size size) {
        CarSpec spec = new CarSpec(make, model, year, size);
        String ID = Integer.toString(carList.size());
        Car car = new Car(ID, spec);
        carList.add(car);
    }
    /**
    public List<Car> findCar(String data) {
        List<Car> list = new LinkedList();
        for (Car car: carList) {
            if (car.contains(data)) {
                list.add(car);
            }
        }
        return list;
    }
    
    public Boolean rentCar(String data) {
        List<Car> car = findCar(data);
        for (Car rentCar: car) {
            if (!rentCar.isAvailable()) {
                rentCar.rentCar();
                return true;
            }
        }
        return false;
    }
    
    public Boolean returnCar(String ID) {
        for (Car car: carList) {
            if (car.getID().equals(ID)) {
                car.returnCar();
                return true;
            }
        }
        return false;
    }*/
    public void addAllCars(List<Car> cars){
        this.carList.addAll(cars);
        
    }
    public void addCustomer(String ID, String name, String phone, String address){
        Customer customer = new Customer ( ID, name , phone, address);
        customerList.add(customer);
    }

    
}
