/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.List;
import java.util.ArrayList;
import java.util.Objects;

/**
 *
 * @author Shazam
 */
public class Car {
    private String ID;
    private CarSpec spec;
    private List<Rental> rentalList;
    
    public Car(String ID, CarSpec spec){
        this.ID = ID;
        this.spec = spec;
        this.rentalList = new ArrayList<>();
        
    }

    public String getID() {
        return ID;
    }

    public CarSpec getSpec() {
        return spec;
    }
    
    public List<Rental> getRentalList() {
        return rentalList;
    }
    
    
    public void addRental(Rental rental){
        rentalList.add(rental);
    }
    
    public Rental getLastRental(){
        if(rentalList.size() == 0){
            throw new IllegalStateException("There are no rentals available for this car.");
            
        }
        return rentalList.get(rentalList.size() - 1);
    }
    
    public void rentCar(String rentDate)throws ParseException {
        Rental rental = new Rental(this);
        rental.rentCar(rentDate);
        rentalList.add(rental);
        
    }
        
        
    
    
    public void returnCar(String returnDate)throws ParseException, IllegalStateException {
        if(isAvailable()){
            throw new IllegalStateException("Car is not rented. Can't return it.s");
            
        }
        Rental rental =rentalList.get(rentalList.size() - 1);
        rental.returnCar(returnDate);
    }
    
    public Boolean isAvailable() {
        if(rentalList.isEmpty())
            return true;
        return (rentalList.get(rentalList.size() -1).getStatus().equals(Status.returned));
        
    }
    /**
    public boolean contains(String data){
        return ID.contains(data) || spec.contains(data);
    }*/
    
    @Override
    public int hashCode(){
        int hash = 7;
        
        hash = 89 * hash + Objects.hashCode(this.ID);
        hash = 89 * hash + Objects.hashCode(this.spec);
        return hash;
    }
    
    @Override
    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        if (obj == null){
            return false;
        }
        if(getClass() != obj.getClass()){
            return false;
        }
        final Car other = (Car) obj;
        if(!Objects.equals(this.ID, other.ID)){
            return false;
        }
        if(!Objects.equals(this.spec, other.spec)){
            return false;
        }
        return true;
    }
    @Override
    public String toString(){
        return "Car{" + "ID="+ ID + ", spec="+ spec + '}';
    }
}
