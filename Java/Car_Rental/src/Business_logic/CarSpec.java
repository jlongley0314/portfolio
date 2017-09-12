/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

/**
 *
 * @author Shazam
 */
public class CarSpec {
    private String make;
    private String model;
    private int year;
    private Size size;

    public CarSpec(String make, String model, int year, Size size) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.size = size;
    }

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    public Size getSize() {
        return size;
    }
    /**
      
    public boolean contains(String data){
        return (make.contains(data) || 
                (model.contains(data)) || 
                (""+year).contains(data)) ||
                (size.toString().contains(data));
    }*/
}
