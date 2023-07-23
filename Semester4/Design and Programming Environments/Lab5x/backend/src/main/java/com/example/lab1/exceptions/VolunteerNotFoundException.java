package com.example.lab1.exceptions;

public class VolunteerNotFoundException extends RuntimeException{
    public VolunteerNotFoundException(Long id){super("The volunteer with the id: " + id + " was not found!");}
}
