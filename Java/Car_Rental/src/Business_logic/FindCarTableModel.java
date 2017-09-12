/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business_logic;

import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author shado
 */
public class FindCarTableModel extends AbstractTableModel {

    private String[] columnNames = {"Select", "ID", "Make", "Year", "Size"};

    private List<Car> carsList;
    private List<Boolean> isSelected;

    public FindCarTableModel(List<Car> carsList) {
        this.carsList = new ArrayList<>();
        this.isSelected = new ArrayList<>();

        this.carsList.addAll(carsList);
        isSelected.add(false);
    }

    public void addCar(Car car) {
        carsList.add(car);
        isSelected.add(false);
        fireTableDataChanged();
    }

    @Override
    public int getRowCount() {
        return carsList.size();

    }

    @Override
    public int getColumnCount() {

        return columnNames.length;
    }

    @Override
    public String getColumnName(int columnIndex) {
        return columnNames[columnIndex];
    }

    @Override
    public Class<?> getColumnClass(int columnIndex) {
        switch (columnIndex) {
            case 0:
                return Boolean.class;
            case 4:
                return Integer.class;
            default:
                return Size.class;
        }

    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {

        switch (columnIndex) {
            case 0:
                return isSelected.get(rowIndex);
            case 1:
                return carsList.get(rowIndex).getID();
            case 2:
                return carsList.get(rowIndex).getSpec().getMake();
            case 3:
                return carsList.get(rowIndex).getSpec().getModel();
            case 4:
                return carsList.get(rowIndex).getSpec().getYear();
            default:
                return carsList.get(rowIndex).getSpec().getSize();
        }
    }

    @Override
    public void setValueAt(Object aValue, int rowIndex, int columnIndex) {
        if (aValue instanceof Boolean && columnIndex == 0) {
            isSelected.set(rowIndex, (Boolean) aValue);
        }
    }

    public void rentCars(RentedCarTableModel returnedCarModel, String rentString, Customer customer) throws ParseException {

        for (int i = 0; i < isSelected.size(); ++i) {
            if (isSelected.get(i)) {
                Car car = carsList.get(i);
                car.rentCar(rentString);
                returnedCarModel.addRental(car.getLastRental());
                customer.addRental(car.getLastRental());
                

                carsList.remove(i);
                isSelected.remove(i);
                --i;

            }

        }
        fireTableDataChanged();
    }

}


