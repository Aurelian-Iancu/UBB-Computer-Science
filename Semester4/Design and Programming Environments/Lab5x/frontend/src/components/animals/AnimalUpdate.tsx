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


export const AnimalUpdate = () => {
    const [errorMessage, setErrorMessage] = useState("");
    const [showNotification, setShowNotification] = useState(false);

    const navigate = useNavigate();
    const {animalId} = useParams();

    const [loading, setLoading] = useState(true)
    const [animal, setAnimal] = useState({
        id: animalId,
        name:"",
        type:"",
        weight:1,
        dateOfBirth:"",
        breed:""
    });

    useEffect(() => {
        const fetchAnimal = async () => {
            const response = await fetch(`${BACKEND_API_URL}/animal/${animalId}`);
            const animal = await response.json();
            setAnimal({
                id: animalId,
                name: animal.name,
                type: animal.type,
                weight: animal.weight,
                breed: animal.breed,
                dateOfBirth: animal.dateOfBirth
            })
            setLoading(false);
            console.log(animal);
        };
        fetchAnimal();
    }, [animalId]);

    const updateAnimal = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.put(`${BACKEND_API_URL}/animal/update/${animalId}`, animal);
            navigate(`/animal/${animalId}`);
        } catch (error) {
            console.log(error);
            setErrorMessage("Animal could not be updated.  Make sure the information is correct. ");
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

            {!loading && !animal && <div>Animal not found</div>}

            {!loading && (
                <Card>
                    <CardContent>
                        <form onSubmit={updateAnimal}>
                        <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', paddingBlockEnd:3}}>
                            <IconButton component={Link} to={`/animal`} sx={{mr: 2}}>
                                <ArrowBackIcon/>
                            </IconButton>
                            <Typography variant="h6" sx={{flexGrow: 1, textAlign: 'center', color:'black'}}>
                                <b>Update {animal.name} Animal</b>
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
                                   onChange={(event) => setAnimal({ ...animal, name: event.target.value })}
                        />
                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="type"
                                   label="Type"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setAnimal({ ...animal, type: event.target.value })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="weight"
                                   label="Weight"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setAnimal({ ...animal, weight: Number(event.target.value) })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="dateOfBirth"
                                   label="Date Of Birth"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setAnimal({ ...animal, dateOfBirth: event.target.value })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="breed"
                                   label="Breed"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setAnimal({ ...animal, breed: event.target.value })}
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