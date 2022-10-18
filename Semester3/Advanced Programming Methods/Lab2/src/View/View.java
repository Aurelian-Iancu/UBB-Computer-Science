package View;

import Controller.Controller;
import Exception.CustomException;
import Model.Animal;
import jdk.jshell.Snippet;

import java.util.Objects;
import java.util.Scanner;

public class View {
    private Controller controller;

    public View(Controller controller) {
        this.controller = controller;
    }

    private static void printMenu(){
        System.out.println("\tMenu");
        System.out.println("1. Print the list of animals");
        System.out.println("2. Add an animal");
        System.out.println("3. Remove an animal");
        System.out.println("4. Display all the animals that have a weight higher than a given one");
        System.out.println("5. Exit");
    }

    private void printAll(){
        Animal[] animals = this.controller.getAllController();
        if(this.controller.getSizeController() == 0){
            System.out.println("There are no animals in the repository!");
        }
        else{
            int index;
            for(index = 0; index < this.controller.getSizeController(); index++){
                System.out.println((index + 1) + ". " + animals[index].toText());
            }
        }
    }

    private void addAnimal() throws CustomException {
        System.out.println("Enter type: ");
        Scanner readType = new Scanner(System.in);
        String type = readType.nextLine();
        if(Objects.equals(type, "bird") || Objects.equals(type, "cow") || Objects.equals(type, "pig")){
            System.out.println("Enter weight");
            Scanner readWeight = new Scanner(System.in);
            float weight = readWeight.nextFloat();
            if(weight <= 0){
                throw new CustomException("Invalid weight!");
            }
            else{
                this.controller.add(type, weight);
            }
        }else {
            throw new CustomException("Invalid type!");
        }
    }

    private void removeAnimal() throws CustomException{
        if(this.controller.getSizeController() != 0){
            System.out.println("Enter index: ");
            Scanner readIndex = new Scanner(System.in);
            int index = readIndex.nextInt();
            if (index - 1 >= 0 && index - 1 < this.controller.getSizeController()) {
                this.controller.remove(index - 1);
            } else {
                throw new CustomException("Invalid index!");
            }
        } else {
            throw new CustomException("There is nothing left to remove!");
        }
    }

    private void displayFiltered() throws CustomException{
        System.out.println("Enter weight");
        Scanner readWeight = new Scanner(System.in);
        float weight = readWeight.nextFloat();
        if(weight <= 0){
            throw new CustomException("Invalid weight!");
        } else {
            if(this.controller.getSizeController() != 0){
                Animal[] filteredAnimals = this.controller.getFiltered(weight);
                if(filteredAnimals.length == 0){
                    System.out.println("There are no animals that have the weight greater than " + weight + " kg.");
                } else {
                    int index;
                    for(index = 0; index < filteredAnimals.length; index++){
                        System.out.println((index + 1) + ". " + filteredAnimals[index].toText());
                    }
                }
            } else {
                throw new CustomException("The list is empty!");
            }
        }
    }

    public void start(){
        boolean done = false;
        while(!done){
            try {
                printMenu();
                Scanner readOption = new Scanner(System.in);
                int option = readOption.nextInt();
                if(option == 1){
                    this.printAll();
                }
                else if(option == 2){
                    this.addAnimal();
                }
                else if(option == 3){
                    this.removeAnimal();
                }
                else if(option == 4){
                    this.displayFiltered();
                }
                else if(option == 5){
                    done = true;
                }
                else{
                    System.out.println("Invalid input");
                }
            }
            catch (CustomException customException){
                System.out.println(customException.getMessage());
            }
        }
    }
}
