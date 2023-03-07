package com.example.lab1.repository;

import com.example.lab1.model.EntityAnimal;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RepositoryAnimal extends JpaRepository<EntityAnimal, Long> {
}
