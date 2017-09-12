/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

import java.text.ParseException;
import java.util.Calendar;
import java.text.SimpleDateFormat;

/**
 *
 * @author Shazam
 */
public class Rental {
    private Calendar rentDate;
    private Calendar returnDate;
    private Status status;
    private Car car;

    public Rental(Car car) {
        
        this.status = Status.returned;
        this.car = car;
    }
    
    public Rental(String rentDate, String returnDate, Car car, Status status)throws ParseException{
        this.car = car;
        
        setRentDate(rentDate);
        setReturnDate(returnDate);
        this.status = status;
    }
    
    public Calendar getRentDate() {
        return this.rentDate;
    }

    public Calendar getReturnDate() {
        return this.returnDate;
    }
    
    public Car getCar(){
        return car;
    }
    
    public Status getStatus() {
        return this.status;
    }
    
    private void setRentDate(String rentDate)throws ParseException{
        SimpleDateFormat sdf = new SimpleDateFormat("mm/dd/yy");
        sdf.parse(rentDate);
        this.rentDate = sdf.getCalendar();
    }
    
    private void setReturnDate(String returnDate) throws ParseException{
        SimpleDateFormat sdf = new SimpleDateFormat("mm/dd/yy");
        sdf.parse(returnDate);
        this.returnDate = sdf.getCalendar();
    }
    
    public void rentCar(String rentDate)throws ParseException {
        setRentDate(rentDate);
        this.status = Status.rented;
    }
    
    public void returnCar(String returnDate) throws ParseException{
        setReturnDate(returnDate);
             
        this.status = Status.returned;
    }
    
    @Override
    public String toString(){
        return "Rental{"+ "rentDate=" + rentDate.getTime() + "returnDate=" + returnDate.getTime() + ", status=" + status + ", car=" + car + '}';
        
    }
}
