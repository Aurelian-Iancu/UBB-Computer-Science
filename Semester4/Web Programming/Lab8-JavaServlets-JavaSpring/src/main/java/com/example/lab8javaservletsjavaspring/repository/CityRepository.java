package com.example.lab8javaservletsjavaspring.repository;

import com.example.lab8javaservletsjavaspring.model.City;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CityRepository extends JpaRepository<City, Long> {
}
