import React, { useState, useRef } from "react";
import GoogleMapReact from "google-map-react";
import Marker from "./marker";

import "./App.css";

export default function App() {
  const mapRef = useRef();
  let markerList = [];
  var color,
    letters = "0123456789ABCDEF".split("");
  function AddDigitToColor(limit) {
    color += letters[Math.round(Math.random() * limit)];
  }
  function GetRandomColor() {
    color = "#";
    AddDigitToColor(5);
    for (var i = 0; i < 5; i++) {
      AddDigitToColor(15);
    }
    return color;
  }
  //generating markerlist
  fetch("http://127.0.0.1:5000/")
    .then((data) => data.json())
    .then((data) => {
      Object.keys(data).forEach((item, index) => {
        let randomColor = GetRandomColor();

        data[item].forEach((points, index) => {
          markerList.push(
            <Marker color={randomColor} lat={points[0]} lng={points[1]} />
          );
        });
      });
    });

  return (
    <div style={{ height: "100vh", width: "100%" }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: "AIzaSyC_doFYE64lqv3BDELsfLIUCWZ63Tn3Y6c" }}
        defaultCenter={{ lat: 43.6196334, lng: -79.4842971 }}
        defaultZoom={9}
        yesIWantToUseGoogleMapApiInternals
        onGoogleApiLoaded={({ map }) => {
          mapRef.current = map;
        }}
      >
        {/* Loading Markers */}
        {markerList}
      </GoogleMapReact>
    </div>
  );
}
