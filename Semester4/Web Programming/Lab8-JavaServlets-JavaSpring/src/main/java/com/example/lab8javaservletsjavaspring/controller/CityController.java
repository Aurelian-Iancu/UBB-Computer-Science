package com.example.lab8javaservletsjavaspring.controller;

import com.example.lab8javaservletsjavaspring.model.City;
import com.example.lab8javaservletsjavaspring.service.CityService;
import javassist.NotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/cities")
public class CityController {
    private final CityService cityService;

    @Autowired
    public CityController(CityService cityService) {
        this.cityService = cityService;
    }

    @GetMapping
    public List<City> getAllCities() {
        return cityService.getAllCities();
    }

    @GetMapping("/{id}")
    public City getCityById(@PathVariable Long id) throws NotFoundException {
        return cityService.getCityById(id)
                .orElseThrow(() -> new NotFoundException("City not found with id: " + id));
    }

    @PostMapping
    public City createCity(@RequestBody City city) {
        return cityService.saveCity(city);
    }

    @PutMapping("/{id}")
    public City updateCity(@PathVariable Long id, @RequestBody City city) throws NotFoundException {
        City existingCity = cityService.getCityById(id)
                .orElseThrow(() -> new NotFoundException("City not found with id: " + id));

        // Update the existing city with new values
        existingCity.setName(city.getName());
        // Update other properties as needed

        return cityService.saveCity(existingCity);
    }

    @DeleteMapping("/{id}")
    public void deleteCity(@PathVariable Long id) {
        cityService.deleteCity(id);
    }
}
