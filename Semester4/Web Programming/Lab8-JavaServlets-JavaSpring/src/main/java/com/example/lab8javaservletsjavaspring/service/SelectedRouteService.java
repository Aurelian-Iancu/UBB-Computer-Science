package com.example.lab8javaservletsjavaspring.service;

import com.example.lab8javaservletsjavaspring.model.SelectedRoute;
import com.example.lab8javaservletsjavaspring.repository.SelectedRouteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class SelectedRouteService {
    private final SelectedRouteRepository selectedRouteRepository;

    @Autowired
    public SelectedRouteService(SelectedRouteRepository selectedRouteRepository) {
        this.selectedRouteRepository = selectedRouteRepository;
    }

    public List<SelectedRoute> getAllSelectedRoutes() {
        return selectedRouteRepository.findAll();
    }

    public Optional<SelectedRoute> getSelectedRouteById(Long id) {
        return selectedRouteRepository.findById(id);
    }

    public SelectedRoute saveSelectedRoute(SelectedRoute selectedRoute) {
        return selectedRouteRepository.save(selectedRoute);
    }

    public void deleteSelectedRoute(Long id) {
        selectedRouteRepository.deleteById(id);
    }
}
