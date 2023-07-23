package com.example.lab1.repository;

import com.example.lab1.model.Animal;
import com.example.lab1.model.Shelter;
import jakarta.annotation.Nonnull;
import jakarta.persistence.Entity;
import jakarta.validation.constraints.NotNull;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;


public interface AnimalRepository extends JpaRepository<Animal, Long> {
    //List<Animal> findByWeightGreaterThan(double weight);

    @Nonnull
    Page<Animal> findAll(@Nonnull Pageable pageable);

    Page<Animal> findByWeightGreaterThan(Double weight, Pageable pageable);

    @Nonnull
    @EntityGraph(attributePaths = "shelter")
    Optional<Animal> findByAnimalId(@Nonnull Long id);

    Long countByWeightGreaterThanEqual(Double weight);
}
