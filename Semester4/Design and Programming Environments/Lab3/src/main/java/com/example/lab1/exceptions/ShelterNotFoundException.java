package com.example.lab1.exceptions;

public class ShelterNotFoundException extends RuntimeException{
    public ShelterNotFoundException(Long id){super("The shelter with the id: " + id + " was not found!");}
}
