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


export const VolunteerUpdate = () => {
    const [errorMessage, setErrorMessage] = useState("");
    const [showNotification, setShowNotification] = useState(false);

    const navigate = useNavigate();
    const {volunteerId} = useParams();

    const [loading, setLoading] = useState(true)
    const [volunteer, setVolunteer] = useState({
        id: volunteerId,
        firstName:"",
        lastName:"",
        email:"",
        phone:1,
        country:""
    });

    useEffect(() => {
        const fetchVolunteer = async () => {
            const response = await fetch(`${BACKEND_API_URL}/volunteer/${volunteerId}`);
            const volunteer = await response.json();
            setVolunteer({
                id: volunteerId,
                firstName: volunteer.firstName,
                lastName: volunteer.lastName,
                email: volunteer.email,
                phone: volunteer.phone,
                country: volunteer.country
            })
            setLoading(false);
            console.log(volunteer);
        };
        fetchVolunteer();
    }, [volunteerId]);

    const updateVolunteer = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.put(`${BACKEND_API_URL}/volunteer/update/${volunteerId}`, volunteer);
            navigate(`/volunteer/${volunteerId}`);
        } catch (error) {
            console.log(error);
            setErrorMessage("Volunteer could not be updated.  Make sure the information is correct. ");
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

            {!loading && !volunteer && <div>Volunteer not found</div>}

            {!loading && (
                <Card>
                    <CardContent>
                        <form onSubmit={updateVolunteer}>
                        <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', paddingBlockEnd:3}}>
                            <IconButton component={Link} to={`/volunteer`} sx={{mr: 2}}>
                                <ArrowBackIcon/>
                            </IconButton>
                            <Typography variant="h6" sx={{flexGrow: 1, textAlign: 'center', color:'black'}}>
                                <b>Update {volunteer.firstName} {volunteer.lastName} Volunteer</b>
                            </Typography>

                            <Button type="submit" color="inherit" sx={{ color: 'black'}}>
                                <Tooltip title="Update" arrow>
                                    <UpgradeIcon/>
                                </Tooltip>
                            </Button>
                        </Box>
                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="firstName"
                                   label="First Name"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setVolunteer({ ...volunteer, firstName: event.target.value })}
                        />
                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="lastName"
                                   label="Last Name"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setVolunteer({ ...volunteer, lastName: event.target.value })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="email"
                                   label="Email"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setVolunteer({ ...volunteer, email: event.target.value })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="phone"
                                   label="Telephone"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setVolunteer({ ...volunteer, phone: Number(event.target.value) })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="nationality"
                                   label="Nationality"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setVolunteer({ ...volunteer, country: event.target.value })}
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