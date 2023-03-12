package com.example.lab1.controller;

import com.example.lab1.model.Animal;
import com.example.lab1.model.Employee;
import com.example.lab1.model.Shelter;
import com.example.lab1.service.Service;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api")
public class Controller {
    private final Service service;

    public Controller(Service service) {
        this.service = service;
    }

    // Animal ---------------------------------

    @PostMapping("/animal/save/shelter{id}")
    public Animal saveAnimal(@RequestBody Animal animal, @PathVariable("id") Long id){
        return service.saveAnimal(animal, id);
    }

    @GetMapping("/animal/getAll")
    public List<Animal> findAllAnimals(){
        return service.findAllAnimals();
    }

    @GetMapping("/animal/getById/{id}")
    public Optional<Animal> findAnimalById(@PathVariable("id") Long id){
        return service.findAnimalById(id);
    }

    @PutMapping("/animal/update/{id}")
    public Animal updateAnimal(@RequestBody Animal animal, @PathVariable("id") Long id){
        return service.updateAnimal(animal, id);
    }

    @DeleteMapping("/animal/delete/{id}")
    public void deleteAnimal(@PathVariable("id") Long id){
        service.deleteAnimal(id);
    }

    @GetMapping("/animal/filter/{weight}")
    public Object filterAnimals(@PathVariable("weight") Double weight){
        if(weight == null){
            return this.service.findAllAnimals();
        }
        return service.findByWeightGreaterThan(weight);
    }

    // Employee ------------------------------------

    @PostMapping("/employee/save")
    public Employee saveEmployee(@RequestBody Employee employee){
        return service.saveEmployee(employee);
    }

    @GetMapping("/employee/getAll")
    public List<Employee> findAllEmployees(){
        return this.service.findAllEmployees();
    }

    @GetMapping("/employee/getById/{id}")
    public Optional<Employee> findEmployeeById(@PathVariable("id") Long id){
        return this.service.findEmployeeById(id);
    }

    @PutMapping("/employee/update/{id}")
    public Employee updateEmployee(@RequestBody Employee employee, @PathVariable("id") Long id){
        return this.service.updateEmployee(employee, id);
    }

    @DeleteMapping("/employee/delete/{id}")
    public void deleteEmployee(@PathVariable("id") Long id){
        this.service.deleteEmployee(id);
    }

    // Shelter ---------------------------------------------

    @PostMapping("/shelter/save")
    public Shelter saveShelter(@RequestBody Shelter shelter){
        return service.saveShelter(shelter);
    }

    @GetMapping("/shelter/getAll")
    public List<Shelter> findAllShelters(){
        return service.findAllShelters();
    }

    @GetMapping("/shelter/getById/{id}")
    public Optional<Shelter> findShelterById(@PathVariable("id") Long id){
        return service.findShelterById(id);
    }

    @PutMapping("/shelter/update/{id}")
    public Shelter updateShelter(@RequestBody Shelter shelter, @PathVariable("id") Long id){
        return service.updateShelter(shelter, id);
    }

    @DeleteMapping("/shelter/delete/{id}")
    public void deleteShelter(@PathVariable("id") Long id){
        service.deleteShelter(id);
    }
}
