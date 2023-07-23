import {Box, Button, Card, CardActions, CardContent, Container, IconButton, Tooltip, Typography} from "@mui/material";
import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { AnimalWShelter } from "../../models/AnimalWShelter";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import {BACKEND_API_URL} from "../../constants";
import DeleteIcon from "@mui/icons-material/Delete";
import UpgradeIcon from "@mui/icons-material/Upgrade";


export const AnimalDetails = () => {

    const { animalId } = useParams();
    const [animal, setAnimal] = useState<AnimalWShelter>();

    useEffect(() => {
        const fetchShelter = async () => {
            const response = await fetch(`${BACKEND_API_URL}/animal/${animalId}`);
            const animal = await response.json();
            setAnimal(animal);
            console.log(animal);
        };
        fetchShelter();
    }, [animalId]);

    return (
        <Container>
            <Card style={{backgroundColor:"whitesmoke"}}>
                <CardContent>
                    <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', paddingRight:3}}>
                        <IconButton component={Link} sx={{ mr: 3 }} to={`/animal`}>
                            <ArrowBackIcon />
                        </IconButton>{" "}
                        <h2 style={{textAlign:"left", fontWeight:'bold'}}>{animal?.name}</h2>
                    </Box>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Type: {animal?.type}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Weight: {animal?.weight}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Date of birth: {animal?.dateOfBirth}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Breed: {animal?.breed}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Shelter: {animal?.shelter.name}</p>
                </CardContent>

                <CardActions>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/animal/update/${animalId}`}>
                        <EditIcon sx={{ color: "navy" }}/>
                    </IconButton>

                    <IconButton component={Link} sx={{ mr: 3 }} to={`/animal/delete/${animalId}`}>
                        <DeleteIcon sx={{ color: "darkred" }} />
                    </IconButton>
                </CardActions>

            </Card>
        </Container>
    );
};