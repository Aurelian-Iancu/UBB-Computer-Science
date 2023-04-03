package com.example.lab1.advices;

import com.example.lab1.exceptions.AnimalNotFoundException;
import com.example.lab1.exceptions.ShelterNotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
public class ShelterNotFoundAdvice {
    @ResponseBody
    @ExceptionHandler(ShelterNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public String shelterNotFoundHandler(ShelterNotFoundException bx) {
        return bx.getMessage();
    }
}
