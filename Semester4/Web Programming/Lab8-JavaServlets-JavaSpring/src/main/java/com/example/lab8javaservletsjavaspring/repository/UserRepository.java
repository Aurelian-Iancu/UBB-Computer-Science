package com.example.lab8javaservletsjavaspring.repository;

import com.example.lab8javaservletsjavaspring.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
