import {Box, Button, Card, CardActions, CardContent, Container, IconButton, Tooltip, Typography} from "@mui/material";
import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Shelter } from "../../models/Shelter";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import {BACKEND_API_URL} from "../../constants";
import DeleteIcon from "@mui/icons-material/Delete";
import UpgradeIcon from "@mui/icons-material/Upgrade";


export const ShelterDetails = () => {

    const { shelterId } = useParams();
    const [shelter, setShelter] = useState<Shelter>();

    useEffect(() => {
        const fetchShelter = async () => {
            const response = await fetch(`${BACKEND_API_URL}/shelter/${shelterId}`);
            const shelter = await response.json();
            setShelter(shelter);
            console.log(shelter);
        };
        fetchShelter();
    }, [shelterId]);

    return (
        <Container>
            <Card style={{backgroundColor:"whitesmoke"}}>
                <CardContent>
                    <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', paddingRight:3}}>
                        <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter`}>
                            <ArrowBackIcon />
                        </IconButton>{" "}
                        <h2 style={{textAlign:"left", fontWeight:'bold'}}>{shelter?.name}</h2>
                    </Box>

                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Description: {shelter?.description}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Address: {shelter?.address}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Number of volunteers: {shelter?.numberOfVolunteers}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Capacity: {shelter?.capacity}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>City: {shelter?.city}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Animals</p>
                    {shelter?.animals?.length == 0 && <p>This shelter doesn't have any animals.</p>}
                    <ul style={{textAlign:"left", fontWeight:'bold'}}>
                        {shelter?.animals?.map((animal) => (
                            <li key={animal.animalId}>{animal.name}</li>
                        ))}
                    </ul>
                </CardContent>

                <CardActions>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter/update/${shelterId}`}>
                        <EditIcon sx={{ color: "navy" }}/>
                    </IconButton>

                    <IconButton component={Link} sx={{ mr: 3 }} to={`/shelter/delete/${shelterId}`}>
                        <DeleteIcon sx={{ color: "darkred" }} />
                    </IconButton>
                </CardActions>

            </Card>
        </Container>
    );
};