import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './AddPrivate.css';

const AddPrivate = () => {
  const location = useLocation();
  const { destination } = location.state || {};

  const [geolocation, setGeolocation] = useState('');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const user = localStorage.getItem('item');
  const item = JSON.parse(user);
  const userid = item ? item.userid : null;
  const token = item ? item.token : null;

  useEffect(() => {
    if (destination) {
      setGeolocation(destination.geolocation);
      setTitle(destination.title);
      setDescription(destination.description);
      setImage(destination.image);
    }
  }, [destination]);

  const navigate = useNavigate();

  const handleGeolocationChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setGeolocation(event.target.value);
  };

  const handleTitleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setTitle(event.target.value);
  };

  const handleDescriptionChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setDescription(event.target.value);
  };

  const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setImage(event.target.value);
  };

  const handleStartDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setStartDate(event.target.value);
  };

  const handleEndDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEndDate(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await fetch('https://localhost:7203/api/PrivateDestinations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          geolocation,
          title,
          description,
          image,
          startDate,
          endDate,
          userid
        }),
      });

      if (response.ok) {
        console.log('Private destination added successfully');
        navigate('/pickpublic'); // Redirect to the desired page

        // Perform any necessary actions after successfully adding the private destination
      } else {
        console.error('Error adding private destination');
      }
    } catch (error) {
      console.error('Error adding private destination:', error);
    }
  };

  const handlePickFromPublic = () => {
    navigate('/pickpublic');
  };

  return (
      <div className="add-private-container">
        <h1>Add Private Destination</h1>
        <form onSubmit={handleSubmit} className="add-private-form">
          <label htmlFor="geolocation" className="form-field">Geolocation:</label>
          <input type="text" id="geolocation" value={geolocation} onChange={handleGeolocationChange} required />

          <label htmlFor="title" className="form-field">Title:</label>
          <input type="text" id="title" value={title} onChange={handleTitleChange} required />

          <label htmlFor="description" className="form-field">Description:</label>
          <input type="text" id="description" value={description} onChange={handleDescriptionChange} required />

          <label htmlFor="image" className="form-field">Image:</label>
          <input type="text" id="image" value={image} onChange={handleImageChange} required />

          <label htmlFor="startDate" className="form-field">Start Date:</label>
          <input type="date" id="startDate" value={startDate} onChange={handleStartDateChange} required />

          <label htmlFor="endDate" className="form-field">End Date:</label>
          <input type="date" id="endDate" value={endDate} onChange={handleEndDateChange} required />

          <div className="form-actions">
            <button type="submit">Add Private Destination</button>
            <button onClick={handlePickFromPublic}>Pick from Public</button>
          </div>
        </form>
      </div>
  );
}

export default AddPrivate;
