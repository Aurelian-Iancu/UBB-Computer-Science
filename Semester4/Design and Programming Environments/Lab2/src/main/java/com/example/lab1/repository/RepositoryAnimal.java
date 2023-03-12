package com.example.lab1.repository;

import com.example.lab1.model.Animal;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.stream.Stream;

@Repository
public interface RepositoryAnimal extends JpaRepository<Animal, Long> {
    List<Animal> findByWeightGreaterThan(double weight);
}
