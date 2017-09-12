/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

import java.text.SimpleDateFormat;

import java.util.Calendar;

/**
 *
 * @author Shazam
 */
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.ArrayList;
import java.util.List;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author Shazam
 */
public class ReturnedCarTableModel extends AbstractTableModel {

    private String[] ColumnNames = {"ID", "Make", "Model", "Year", "Rented", "Returned"};

    private Customer customer;

    private List<Rental> rentalsList;

    private List<Boolean> isSelected;

    public ReturnedCarTableModel(List<Rental> rentalList, Customer customer) {
        this.customer = customer;
        this.rentalsList = new ArrayList<>();

        this.isSelected = new ArrayList<>();

        this.rentalsList.addAll(rentalList);
        for (Rental r : rentalsList) {
            isSelected.add(false);
        }
    }

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
    public String getColumnName(int columnIndex) {
        return ColumnNames[columnIndex];
    }

    @Override
    public int getColumnCount() {
        return ColumnNames.length;
    }

    @Override
    public Class<?> getColumnClass(int columnIndex) {
        switch (columnIndex) {
            case 3:
                return Integer.class;
            default:
                return String.class;
        }
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {

        if (columnIndex == 0) {
            return rentalsList.get(rowIndex).getCar().getID();
        } else {
            CarSpec spec = rentalsList.get(rowIndex).getCar().getSpec();

            if (columnIndex == 1) {
                return spec.getMake();
            } else if (columnIndex == 2) {
                return spec.getModel();
            } else if (columnIndex == 3) {
                return spec.getYear();
            } else if (columnIndex == 4) {
                Calendar cal = rentalsList.get(rowIndex).getRentDate();
                return (cal == null) ? "" : new SimpleDateFormat("dd/mm/yy").format(cal.getTime());
            } else {
                Calendar cal = rentalsList.get(rowIndex).getRentDate();
                return (cal == null) ? "" : new SimpleDateFormat("dd/mm/yy").format(cal.getTime());

            }
        }

    }

}
