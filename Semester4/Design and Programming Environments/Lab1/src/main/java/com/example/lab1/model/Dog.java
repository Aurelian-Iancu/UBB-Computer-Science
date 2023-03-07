package com.example.lab1.model;

public class Dog {

    private int dogId;
    private String name;
    private int age;
    private int weight;
    private String breed;
    private String foodType;

    public int getDogId() {
        return dogId;
    }

    public void setDogId(int dogId) {
        this.dogId = dogId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public String getFoodType() {
        return foodType;
    }

    public void setFoodType(String foodType) {
        this.foodType = foodType;
    }

    public Dog() {
    }

    public Dog(int dogId, String name, int age, int weight, String breed, String foodType) {
        this.dogId = dogId;
        this.name = name;
        this.age = age;
        this.weight = weight;
        this.breed = breed;
        this.foodType = foodType;
    }
}
