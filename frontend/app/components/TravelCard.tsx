import React from "react";
import Image from "next/image";

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
      return `${minutes} 分鐘`;
    }
    if (minutes === 0) {
      return `${hours} 小時`;
    }
    return `${hours} 小時  ${minutes} 分鐘`;
  }
  const timeParts = arrive_time.split(":");
  const hour = timeParts.length > 1 ? parseInt(timeParts[0], 10) : 0;
  const isAfternoon = hour > 12;

  return (
    <div
      className={`flex flex-col items-start p-4 rounded-lg shadow-md text-black h-full ${
        isAfternoon ? "bg-yellow-200" : "bg-orange-100"
      }`}
    >
      <h2 className="text-xl font-bold mt-2 ml-2 mb-1">{title}</h2>
      <Image
        src={imageSrc}
        alt={alt}
        onError={(e) => {
          (e.currentTarget as HTMLImageElement).src = "/placeholder.jpeg"; // Set placeholder on error
        }}
        width={300}
        height={175}
        className="rounded-lg object-cover"
      />
      <p className="font-medium text-lg mb-[1.5px] mt-0.5">
        預計到達時間: {arrive_time}
      </p>
      {stay_time !== null && (
        <p className="font-medium text-lg ">
          預估停留時間: {transferTime(stay_time)}
        </p>
      )}
    </div>
  );
};

export default TravelCard;

export type { TravelCardProps };
