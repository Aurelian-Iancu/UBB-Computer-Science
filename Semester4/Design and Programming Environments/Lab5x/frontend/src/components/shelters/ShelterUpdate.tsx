import {
    Box,
    Button,
    Card,
    CardActions,
    CardContent,
    CircularProgress,
    Container,
    IconButton,
    Snackbar,
    TextField, Tooltip, Typography
} from "@mui/material";
import React, {useEffect, useState} from "react";
import {Link, useNavigate, useParams} from "react-router-dom";
import {Shelter} from "../../models/Shelter";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import {BACKEND_API_URL} from "../../constants";
import MuiAlert, {AlertProps} from "@mui/material/Alert";
import UpgradeIcon from '@mui/icons-material/Upgrade';


const Alert = React.forwardRef<HTMLDivElement, AlertProps>(function Alert(
    props,
    ref,
) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});


export const ShelterUpdate = () => {
    const [errorMessage, setErrorMessage] = useState("");
    const [showNotification, setShowNotification] = useState(false);

    const navigate = useNavigate();
    const {shelterId} = useParams();

    const [loading, setLoading] = useState(true)
    const [shelter, setShelter] = useState({
        id: shelterId,
        name:"",
        address:"",
        numberOfVolunteers:1,
        capacity:1,
        city:""
    });

    useEffect(() => {
        const fetchShelter = async () => {
            const response = await fetch(`${BACKEND_API_URL}/shelter/${shelterId}`);
            const shelter = await response.json();
            setShelter({
                id: shelterId,
                name: shelter.name,
                address: shelter.address,
                numberOfVolunteers: shelter.numberOfVolunteers,
                capacity: shelter.capacity,
                city: shelter.city
            })
            setLoading(false);
            console.log(shelter);
        };
        fetchShelter();
    }, [shelterId]);

    const updateShelter = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.put(`${BACKEND_API_URL}/shelter/update/${shelterId}`, shelter);
            navigate(`/shelter/${shelterId}`);
        } catch (error) {
            console.log(error);
            setErrorMessage("Shelter could not be updated.  Make sure the information is correct. ");
            setShowNotification(true);
        }
    };


    return (
        <Container>

            {showNotification && (
                <Snackbar open={!!errorMessage} autoHideDuration={6000} onClose={() => setShowNotification(false)}>
                    <Alert severity="error" sx={{width: '100%'}}>
                        {errorMessage}
                    </Alert>
                </Snackbar>

            )}

            {loading && <CircularProgress/>}

            {!loading && !shelter && <div>Shelter not found</div>}

            {!loading && (
                <Card>
                    <CardContent>
                        <form onSubmit={updateShelter}>
                        <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', paddingBlockEnd:3}}>
                            <IconButton component={Link} to={`/shelter`} sx={{mr: 2}}>
                                <ArrowBackIcon/>
                            </IconButton>
                            <Typography variant="h6" sx={{flexGrow: 1, textAlign: 'center', color:'black'}}>
                                <b>Update {shelter.name} Shelter</b>
                            </Typography>

                            <Button type="submit" color="inherit" sx={{ color: 'black'}}>
                                <Tooltip title="Update" arrow>
                                    <UpgradeIcon/>
                                </Tooltip>
                            </Button>
                        </Box>
                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="name"
                                   label="Name"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setShelter({ ...shelter, name: event.target.value })}
                        />
                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="address"
                                   label="Address"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setShelter({ ...shelter, address: event.target.value })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="numberOfVolunteers"
                                   label="Number of volunteers"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setShelter({ ...shelter, numberOfVolunteers: Number(event.target.value) })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="capacity"
                                   label="Capacity"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setShelter({ ...shelter, capacity: Number(event.target.value) })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="city"
                                   label="City"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setShelter({ ...shelter, city: event.target.value })}
                        />

                        </form>
                    </CardContent>
                    <CardActions></CardActions>
                </Card>
            )
            }
        </Container>
    );
};