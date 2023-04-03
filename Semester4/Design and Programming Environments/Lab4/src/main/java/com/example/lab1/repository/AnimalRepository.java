package com.example.lab1.repository;

import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;


public interface AnimalRepository extends JpaRepository<Animal, Long> {
    List<Animal> findByWeightGreaterThan(double weight);
}
