import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const AddPrivate = () => {
  const location = useLocation();
  const { destination } = location.state || {};

  const [geolocation, setGeolocation] = useState('');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

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
      const response = await fetch('http://localhost:5145/api/PrivateDestinations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          geolocation,
          title,
          description,
          image,
          startDate,
          endDate,
        }),
      });

      if (response.ok) {
        console.log('Private destination added successfully');
        navigate('/alldestinations'); // Redirect to the desired page

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
    <div>
      <h1>Add Private Destination</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="geolocation">Geolocation:</label>
          <input type="text" id="geolocation" value={geolocation} onChange={handleGeolocationChange} required />
        </div>
        <div>
          <label htmlFor="title">Title:</label>
          <input type="text" id="title" value={title} onChange={handleTitleChange} required />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <input type="text" id="description" value={description} onChange={handleDescriptionChange} required />
        </div>
        <div>
          <label htmlFor="image">Image:</label>
          <input type="text" id="image" value={image} onChange={handleImageChange} required />
        </div>
        <div>
          <label htmlFor="startDate">Start Date:</label>
          <input type="date" id="startDate" value={startDate} onChange={handleStartDateChange} required />
        </div>
        <div>
          <label htmlFor="endDate">End Date:</label>
          <input type="date" id="endDate" value={endDate} onChange={handleEndDateChange} required />
        </div>
        <button type="submit">Add Private Destination</button>
      </form>
      <button onClick={handlePickFromPublic}>Pick from Public</button>
    </div>
  );
};

export default AddPrivate;
