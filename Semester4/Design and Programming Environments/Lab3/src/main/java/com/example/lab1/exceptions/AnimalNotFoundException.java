package com.example.lab1.exceptions;

public class AnimalNotFoundException extends RuntimeException{
    public AnimalNotFoundException(Long id){super("The animal with the id: " + id + " was not found!");}
}
