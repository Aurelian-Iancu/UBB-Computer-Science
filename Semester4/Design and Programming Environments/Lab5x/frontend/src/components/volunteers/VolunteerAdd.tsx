import {
    Box,
    Button,
    Card,
    CardActions,
    CardContent,
    Container,
    IconButton,
    Snackbar,
    TextField, Tooltip,
    Typography
} from "@mui/material";
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Volunteer } from "../../models/Volunteer";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { BACKEND_API_URL } from "../../constants";
import MuiAlert, {AlertProps} from "@mui/material/Alert";
import UpgradeIcon from "@mui/icons-material/Upgrade";
import AddIcon from "@mui/icons-material/Add";

const Alert = React.forwardRef<HTMLDivElement, AlertProps>(function Alert(
    props,
    ref,
) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

export const VolunteerAdd = () => {

    const navigate = useNavigate();

    const [errorMessage, setErrorMessage] = useState("");
    const [showNotification, setShowNotification] = useState(false);


    const [volunteer, setVolunteer] = useState({
        firstName:"",
        lastName:"",
        email:"",
        phone:0,
        country:""
    });

    const addVolunteer = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.post(`${BACKEND_API_URL}/volunteer/save`, volunteer);
            navigate("/volunteer");
        } catch (error) {
            console.log(error);
            setErrorMessage("Volunteer could not be added. Make sure the information is correct. ");
            setShowNotification(true);
        }
    };

    return (
        <Container>

            {showNotification && (
                <Snackbar open={!!errorMessage} autoHideDuration={6000} onClose={() => setShowNotification(false)}>
                    <Alert severity="error" sx={{ width: '100%' }}>
                        {errorMessage}
                    </Alert>
                </Snackbar>

            )}

            <Card>
                <CardContent>

                    <form onSubmit={addVolunteer}>
                        <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', paddingBlockEnd:3}}>
                            <IconButton component={Link} sx={{ mr: 3 }} to={`/volunteer`}>
                                <ArrowBackIcon />
                            </IconButton>{" "}
                            <Typography variant="h6" sx={{flexGrow: 1, textAlign: 'center'}}>
                                <b>Add New Volunteer</b>
                            </Typography>

                            <Button type="submit" color="inherit" sx={{ color: 'black'}}>
                                <Tooltip title="Add" arrow>
                                    <AddIcon/>
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
                                   label="Phone"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setVolunteer({ ...volunteer, phone: Number(event.target.value) })}
                        />

                        <TextField style={{color:"#2471A3", fontWeight:'bold'}}
                                   id="country"
                                   label="Country"
                                   variant="outlined"
                                   fullWidth
                                   sx={{ mb: 2 }}
                                   onChange={(event) => setVolunteer({ ...volunteer, country: event.target.value })}
                        />
                    </form>
                </CardContent>
                <CardActions></CardActions>
            </Card>
        </Container>
    );
};