/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

import java.util.Calendar;
import java.text.SimpleDateFormat;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author Shazam
 */
public class RentedCarTableModel extends AbstractTableModel {
    
    private String[] ColumnNames = {"Select", "Make", "Model", "Year", "Rented"};
    
    private Customer customer;
    //private List<Customer> CustomersList = new ArrayList();
    
    //private List<Car> carsList;
    private List<Rental> rentalsList;

    private List<Boolean> isSelected;
    
    public RentedCarTableModel(List<Rental> rentalList, Customer customer) {
        
        //this.carsList  = new ArrayList<>();
        this.rentalsList = new ArrayList<>();
        this.isSelected = new ArrayList<>();
        
        this.rentalsList.addAll(rentalList);
        for (Rental rn: rentalList) {
            isSelected.add(false);
        }
        
        fireTableDataChanged();
    }
    public void addAllRental(List<Rental> rentalList){
        for(Rental rental : rentalList){
            rentalList.add(rental);
            isSelected.add(false);
        }
        fireTableDataChanged();
    }
    // Method to add a rental to the List
    
    public void addRental(Rental rental) {
        rentalsList.add(rental);
        isSelected.add(false);
        fireTableDataChanged();
    }
    
    
    @Override
    public int getRowCount() {
        return rentalsList.size();
        
    }
    
    @Override
    public String getColumnName(int columnIndex){
        return ColumnNames[columnIndex];
    }

    @Override
    public int getColumnCount() {
        return ColumnNames.length;
    }
    
    
    
    @Override
    public Class<?> getColumnClass(int columnIndex) {
        switch (columnIndex) {
            case 0:
                return Boolean.class;
            case 3:
                return Integer.class;
            default:
                return Size.class;
        }
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        
        if(columnIndex == 0){
            return isSelected.get(rowIndex);
        }
        else{
            Car car = rentalsList.get(rowIndex).getCar();
            CarSpec spec = car.getSpec();
            if(columnIndex == 1){
                return spec.getMake();
            }else if(columnIndex == 2){
                return spec.getModel();
                
            }else if(columnIndex == 3){
                return spec.getYear();
            }else{
                Calendar cal = rentalsList.get(rowIndex).getRentDate();
                return (cal == null) ? "" : new SimpleDateFormat("dd/mm/yy").format(cal.getTime());
            }
        }
    }
    
    @Override
    public void setValueAt(Object aValue, int rowIndex, int columnIndex) {
        if (aValue instanceof Boolean && columnIndex == 0) {
            isSelected.set(rowIndex, (Boolean) aValue);
        }
    }
    
    /**
     *
     * @param returnedCarModel
     * @param findCarModel
     * @param returnString
     */
    public void retunCars(ReturnedCarTableModel returnedCarModel,FindCarTableModel findCarModel, String returnString )throws ParseException {
        for(int i = 0; i < isSelected.size(); ++i){
            if(isSelected.get(i)){
                Rental rental = rentalsList.get(i);
                
                Car car = rental.getCar();
                
                car.returnCar(returnString);
                
                findCarModel.addCar(car);
                
                returnedCarModel.addRental(rental);
                
                rentalsList.remove(i);
                isSelected.remove(i);
                --i;
                
            }
            
        }
        fireTableDataChanged();
    }
    
}
