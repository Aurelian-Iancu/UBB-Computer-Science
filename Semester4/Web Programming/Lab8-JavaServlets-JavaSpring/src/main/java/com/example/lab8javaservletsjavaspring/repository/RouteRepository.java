package com.example.lab8javaservletsjavaspring.repository;

import com.example.lab8javaservletsjavaspring.model.Route;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RouteRepository extends JpaRepository<Route, Long> {

}
