package com.example.lab1.service;
import com.example.lab1.model.Animal;
import com.example.lab1.model.Employee;
import com.example.lab1.model.Shelter;
import com.example.lab1.repository.RepositoryAnimal;
import com.example.lab1.repository.RepositoryEmployee;
import com.example.lab1.repository.RepositoryShelter;

import java.util.List;
import java.util.Optional;

@org.springframework.stereotype.Service
public class Service {
    private final RepositoryAnimal repositoryAnimal;

    private final RepositoryShelter repositoryShelter;

    private final RepositoryEmployee repositoryEmployee;

    public Service(RepositoryAnimal repositoryAnimal, RepositoryShelter repositoryShelter, RepositoryEmployee repositoryEmployee) {
        this.repositoryAnimal = repositoryAnimal;
        this.repositoryShelter = repositoryShelter;
        this.repositoryEmployee = repositoryEmployee;
    }

    // Animal --------------------------------------------

    public List<Animal> findAllAnimals(){
        return repositoryAnimal.findAll();
    }

    public Optional<Animal> findAnimalById(Long id){
        return repositoryAnimal.findById(id);
    }

    public Animal saveAnimal(Animal animal, Long id) {
        return this.repositoryShelter.findById(id)
                .map(shelter -> {
                    animal.setShelter(shelter);
                    return this.repositoryAnimal.save(animal);
                }).orElse(null);
    }

    public Animal updateAnimal(Animal animal, Long id){
        Animal oldAnimal = repositoryAnimal.findById(id).orElse(null);
        if(oldAnimal != null) {
            oldAnimal.setName(animal.getName());
            oldAnimal.setType(animal.getType());
            oldAnimal.setWeight(animal.getWeight());
            oldAnimal.setDateOfBirth(animal.getDateOfBirth());
            repositoryAnimal.save(oldAnimal);
            return oldAnimal;

        }

        return repositoryAnimal.save(animal);
    }

    public void deleteAnimal(Long id){
        repositoryAnimal.deleteById(id);
    }

    public List<Animal> findByWeightGreaterThan(Double weight){
        return this.repositoryAnimal.findByWeightGreaterThan(weight);
    }

    //Employee ------------------------------------------

    public List<Employee> findAllEmployees(){
        return this.repositoryEmployee.findAll();
    }

    public Optional<Employee> findEmployeeById(Long id){
        return this.repositoryEmployee.findById(id);
    }

    public Employee saveEmployee(Employee employee){
        return this.repositoryEmployee.save(employee);
    }

    public Employee updateEmployee(Employee employee, Long id){
        Employee oldEmployee = repositoryEmployee.findById(id).orElse(null);
        if(oldEmployee != null){
            oldEmployee.setName(employee.getName());
            oldEmployee.setRole(employee.getRole());
            oldEmployee.setSalary(employee.getSalary());
            oldEmployee.setAge(employee.getAge());
            repositoryEmployee.save(oldEmployee);
            return oldEmployee;
        }
        return repositoryEmployee.save(employee);
    }

    public void deleteEmployee(Long id){
        repositoryEmployee.deleteById(id);
    }

    //Shelter -----------------------------------------------

    public List<Shelter> findAllShelters(){
        return repositoryShelter.findAll();
    }
    public Optional<Shelter> findShelterById(Long id){
        return repositoryShelter.findById(id);
    }

    public Shelter saveShelter(Shelter shelter){
        return this.repositoryShelter.save(shelter);
    }

    public Shelter updateShelter(Shelter shelter, Long id){
        Shelter oldShelter = repositoryShelter.findById(id).orElse(null);
        if(oldShelter != null){
            oldShelter.setName(shelter.getName());
            oldShelter.setAddress(shelter.getAddress());
            oldShelter.setNumberOfEmployees(shelter.getNumberOfEmployees());
            oldShelter.setCapacity(shelter.getCapacity());
            repositoryShelter.save(oldShelter);
            return oldShelter;
        }

        return repositoryShelter.save(shelter);

    }

    public void deleteShelter(Long id){
        repositoryShelter.deleteById(id);
    }
}
