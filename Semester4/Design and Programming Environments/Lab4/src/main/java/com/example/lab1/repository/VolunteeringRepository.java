package com.example.lab1.repository;

import com.example.lab1.model.KeyVolunteering;
import com.example.lab1.model.Volunteering;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface VolunteeringRepository extends JpaRepository<Volunteering, KeyVolunteering> {
}
