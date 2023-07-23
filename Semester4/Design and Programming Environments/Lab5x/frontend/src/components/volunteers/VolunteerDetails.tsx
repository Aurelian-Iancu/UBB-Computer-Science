import {Box, Button, Card, CardActions, CardContent, Container, IconButton, Tooltip, Typography} from "@mui/material";
import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { Volunteer } from "../../models/Volunteer";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import {BACKEND_API_URL} from "../../constants";
import DeleteIcon from "@mui/icons-material/Delete";
import UpgradeIcon from "@mui/icons-material/Upgrade";


export const VolunteerDetails = () => {

    const { volunteerId } = useParams();
    const [volunteer, setVolunteer] = useState<Volunteer>();

    useEffect(() => {
        const fetchVolunteer = async () => {
            const response = await fetch(`${BACKEND_API_URL}/volunteer/${volunteerId}`);
            const volunteer = await response.json();
            setVolunteer(volunteer);
            console.log(volunteer);
        };
        fetchVolunteer();
    }, [volunteerId]);

    return (
        <Container>
            <Card style={{backgroundColor:"whitesmoke"}}>
                <CardContent>
                    <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', paddingRight:3}}>
                        <IconButton component={Link} sx={{ mr: 3 }} to={`/volunteer`}>
                            <ArrowBackIcon />
                        </IconButton>{" "}
                        <h2 style={{textAlign:"left", fontWeight:'bold'}}>{volunteer?.firstName} {volunteer?.lastName}</h2>
                    </Box>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Email: {volunteer?.email}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Telephone: {volunteer?.phone}</p>
                    <p  style={{textAlign:"left", fontWeight:'bold'}}>Country: {volunteer?.country}</p>
                </CardContent>

                <CardActions>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/volunteer/update/${volunteerId}`}>
                        <EditIcon sx={{ color: "navy" }}/>
                    </IconButton>

                    <IconButton component={Link} sx={{ mr: 3 }} to={`/volunteer/delete/${volunteerId}`}>
                        <DeleteIcon sx={{ color: "darkred" }} />
                    </IconButton>
                </CardActions>

            </Card>
        </Container>
    );
};