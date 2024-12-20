import React, { useState } from "react";
import Image from "next/image";
import Switch from "@/app/components/Switch";

interface CardProps {
  title: string;
  description: string;
  imageSrc: string;
  alt: string;
  onToggle: (value: string) => void;
}

const Card: React.FC<CardProps> = ({
  title,
  description,
  imageSrc,
  alt,
  onToggle,
}) => {
  const [detail, setDetail] = useState<boolean>(false);
  const [isOn, setIsOn] = useState<boolean>(false);

  const onSubmit = () => setDetail(!detail);
  const handleToggle = () => {
    setIsOn(!isOn);
    onToggle(title);
  };

  return (
    <>
      {detail ? (
        <div className="flex flex-col items-start p-4 bg-white rounded-lg shadow-md text-black h-full">
          <Image
            src={imageSrc}
            onError={(e) => {
              (e.currentTarget as HTMLImageElement).src = "/placeholder.jpg"; // Set placeholder on error
            }}
            alt={alt}
            width={600}
            height={350}
            className="rounded-lg object-cover w-full h-auto max-h-[300px] sm:max-h-[400px]"
          />
          <h2 className="text-lg font-bold mt-2 ml-2">{title}</h2>
          <p className="ml-2 mt-1">{description}</p>
          <form onSubmit={onSubmit}>
            <button
              type="submit"
              className="text-lg mt-2 font-semibold  hover:text-blue-500"
            >
              Go Back
            </button>
          </form>
        </div>
      ) : (
        <div className="flex flex-col items-center p-4 bg-white rounded-lg shadow-md text-black h-full w-full">
          <h2 className="text-lg font-bold mt-2 ml-2 content-center">
            {title}
          </h2>
          <div className="flex flex-col sm:flex-row items-center sm:space-x-4 mt-4 space-y-2 sm:space-y-0">
            <Switch
              isOn={isOn}
              handleToggle={handleToggle}
              id={`switch-${title}`}
            />
            <form onSubmit={onSubmit}>
              <button
                type="submit"
                className="font-semibold  hover:text-blue-500"
              >
                Learn more...
              </button>
            </form>
          </div>
        </div>
      )}
    </>
  );
};

export default Card;
