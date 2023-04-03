package com.example.lab1.repository;

import com.example.lab1.model.Shelter;
import com.example.lab1.service.mappers.shelterMappers.ShelterDTOCount;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
@Repository
public interface ShelterRepository extends JpaRepository<Shelter, Long>{
}
