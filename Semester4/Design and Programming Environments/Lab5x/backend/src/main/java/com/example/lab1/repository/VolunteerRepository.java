package com.example.lab1.repository;

import com.example.lab1.model.Volunteer;
import jakarta.annotation.Nonnull;
import org.springframework.data.domain.Page;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import org.springframework.data.domain.Pageable;


@Repository
public interface VolunteerRepository extends JpaRepository<Volunteer, Long> {
    @Nonnull
    Page<Volunteer> findAll(@Nonnull Pageable pageable);
}
