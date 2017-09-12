/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Shazam
 */
public class Customer {
    private String ID;
    private String name;
    private String phone;
    private String address;
    private List<Rental> rentalList;

    public Customer(String ID , String name, String phone, String address) {
        this.name = name;
        this.phone = phone;
        this.address = address;
        this.rentalList = new ArrayList<>();
        
    }
    public String getID(){
        return ID;
    }
    public String getName(){
        return name;
    }
    
    
    
    public String getPhone(){
        return phone;
    }
    
        
    public String getAddress(){
        return address;
    }
    
    public void addRental(Rental rental){
        rentalList.add(rental);
    }
    
    public List<Rental> getRentalList(){
        return rentalList;
    }
    
}
