import React, { useState, useEffect } from "react";

interface TravelCardProps {
  title: string;
  imageSrc: string;
  alt: string;
  arrive_time: string;
  stay_time: number | null;
}

const TravelCard: React.FC<TravelCardProps> = ({
  title,
  imageSrc,
  alt,
  arrive_time,
  stay_time,
}) => {
  function transferTime(time: number) {
    const hours = Math.floor(time / 60);
    const minutes = time % 60;
    if (hours === 0) {
      return `${minutes}分鐘`;
    }
    return `${hours}小時 ${minutes}分鐘`;
  }
  const timeParts = arrive_time.split("點");
  const hour = timeParts.length > 1 ? parseInt(timeParts[0], 10) : 0;
  const isAfternoon = hour > 12;

  return (
    <div
      className={`flex flex-col items-start p-4 rounded-lg shadow-md text-black h-full ${
        isAfternoon ? "bg-yellow-200" : "bg-orange-100"
      }`}
    >
      <h2 className="text-lg font-bold mt-2 ml-2">{title}</h2>
      <img
        src={imageSrc}
        alt={alt}
        className="rounded-lg w-[600px] h-[350px] object-cover"
      />
      <p>到達時間: {arrive_time}</p>
      {stay_time !== null && <p>停留時間: {transferTime(stay_time)}</p>}
    </div>
  );
};

export default TravelCard;

export type { TravelCardProps };
