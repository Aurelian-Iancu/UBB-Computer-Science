package com.example.lab1.repository.ShelterRepository;

import com.example.lab1.model.Shelter;
import com.example.lab1.service.mappers.shelterMappers.ShelterDTOCount;
import jakarta.annotation.Nonnull;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
@Repository
public interface ShelterRepository extends JpaRepository<Shelter, Long>{
    @Nonnull
    Page<Shelter> findAll(@Nonnull Pageable pageable);
}
