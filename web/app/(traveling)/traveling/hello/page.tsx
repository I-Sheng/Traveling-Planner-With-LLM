"use client";
import { useState } from "react";

export default function HelloWorldComponent() {
  const [message, setMessage] = useState("");

  async function fetchMessage() {
    try {
      const response = await fetch("/api/hello", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        const data = await response.json();
        setMessage(data.message); // Display the message from the API
      } else {
        setMessage("Failed to fetch the message");
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("An error occurred");
    }
  }

  return (
    <div>
      <button onClick={fetchMessage}>Fetch Message</button>
      <h1>{message}</h1>
    </div>
  );
}
