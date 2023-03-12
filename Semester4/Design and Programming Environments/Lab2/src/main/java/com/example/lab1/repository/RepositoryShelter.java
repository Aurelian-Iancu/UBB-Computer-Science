package com.example.lab1.repository;

import com.example.lab1.model.Shelter;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RepositoryShelter extends JpaRepository<Shelter, Long> {
}
