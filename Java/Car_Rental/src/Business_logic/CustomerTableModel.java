/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

import java.util.ArrayList;
import java.util.List;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author shado
 */
public class CustomerTableModel extends AbstractTableModel {
    
    private String[] columnNames = {"Name" , "Telephone" , "Address"};
    
    private List<Customer> customersList = new ArrayList();
    
    public CustomerTableModel(List<Customer> customers){
        this.customersList = customers;
        
    }

    @Override
    public int getRowCount() {
        return customersList.size();


    }

    @Override
    public int getColumnCount() {
        return columnNames.length;
    }
    
    @Override
    public String getColumnName(int columnIndex){
        return columnNames[columnIndex];
    }
    
    @Override
    public Class<?> getColumnClass(int columnIndex){
        return String.class;
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        if(columnIndex == 0){
            return customersList.get(rowIndex).getName();
            
        }
        if(columnIndex == 1){
            return customersList.get(rowIndex).getPhone();
            
        }
        return customersList.get(rowIndex).getAddress();

    }
    
    public Customer getCustomer(int rowIndex){
        return customersList.get(rowIndex);
    }
    
    
    
    
    
}
