'use client';

import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';
import { useForm } from 'react-hook-form';

const containerStyle = { width: '100%', height: '400px' };
const center = { lat: 30.1766, lng: -85.8055 }; // Panama City Beach

export default function Home() {
  const { register, handleSubmit } = useForm();

  const onSubmit = (data) => console.log(data); // Stub for event submission

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4">
        <h1 className="text-3xl font-bold">8:05 LIVE - Discover Live Music</h1>
      </header>
      <main className="flex flex-col md:flex-row p-4">
        <div className="md:w-1/2">
          <LoadScript googleMapsApiKey="YOUR_GOOGLE_MAPS_API_KEY">
            <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={12}>
              <Marker position={center} />
            </GoogleMap>
          </LoadScript>
        </div>
        <div className="md:w-1/2 p-4">
          <h2 className="text-2xl">Submit an Event</h2>
          <form onSubmit={handleSubmit(onSubmit)}>
            <input {...register('eventName')} placeholder="Event Name" className="border p-2 mb-2 w-full" />
            <input {...register('location')} placeholder="Location" className="border p-2 mb-2 w-full" />
            <button type="submit" className="bg-blue-600 text-white p-2">Submit</button>
          </form>
          <h2 className="text-2xl mt-4">Tonight's Shows</h2>
          <ul>{/* Event list stub */}</ul>
        </div>
      </main>
    </div>
  );
}
