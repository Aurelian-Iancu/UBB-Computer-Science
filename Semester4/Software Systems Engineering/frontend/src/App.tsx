import React from 'react';
import "./App.css";
import {BrowserRouter as Router, Routes, Route, Navigate} from "react-router-dom";
import { AppMenu } from "./components/AppMenu";
import { AppHome } from "./components/AppHome";
import { LoginForm } from "./components/Login/login";
import { AllDestinations } from "./components/PublicDestinations/AllDestinations";
import { PrivateDestinations } from "./components/PrivateDestination/PrivateDestinations";
import AddDestination from "./components/PublicDestinations/AddDestination";
import UpdateDestination from "./components/PublicDestinations/UpdateDestination";
import AllUserDestinations from "./components/PrivateDestination/AllUserDestinations";
import AddPrivate from "./components/PrivateDestination/AddPrivate";

function App() {

    const user = localStorage.getItem('item');
    const item = JSON.parse(user);
    const userRole = item ? item.roles : null;

    const checkAccess = (allowedRoles, route) => {
        if (!allowedRoles.includes(userRole)) {
            return <Navigate to="/" />;
        }
        return route.element;
    };

    return (
        <React.Fragment>
            <Router>
                <AppMenu />
                <Routes>
                    {userRole === null && (
                        <React.Fragment>
                            <Route path="/login" element={<LoginForm />} />
                            <Route path="/" element={<AppHome />} />
                        </React.Fragment>
                    )}

                    {userRole === "Admin" && (
                        <React.Fragment>
                            <Route path="/alldestinations" element={<AllDestinations />} />
                            <Route path="/adddestination" element={<AddDestination />} />
                            <Route path="/updatedestination" element={<UpdateDestination />} />
                        </React.Fragment>
                    )}

                    {userRole === "Normal" && (
                        <React.Fragment>
                            <Route path="/pickpublic" element={<AllUserDestinations />}/>
                            <Route path="/addprivatedestination" element={<AddPrivate />}/>
                            <Route path="/privatedestinations" element={<PrivateDestinations />}/>
                        </React.Fragment>
                    )}
                </Routes>
            </Router>
        </React.Fragment>
    );
}
export default App;
