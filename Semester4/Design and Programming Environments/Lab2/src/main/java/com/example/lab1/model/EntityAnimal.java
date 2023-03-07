package com.example.lab1.model;

import jakarta.persistence.*;

@Entity
@Table
public class EntityAnimal {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private int animalId;
    @Column
    private String name;
    @Column
    private String type;
    @Column
    private double weight;
    @Column
    private String dateOfBirth;

    public int getAnimalId() {
        return animalId;
    }

    public void setAnimalId(int animalId) {
        this.animalId = animalId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public String getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(String dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public EntityAnimal() {
    }

    public EntityAnimal(int animalId, String name, String type, double weight, String dateOfBirth) {
        this.animalId = animalId;
        this.name = name;
        this.type = type;
        this.weight = weight;
        this.dateOfBirth = dateOfBirth;
    }
}
