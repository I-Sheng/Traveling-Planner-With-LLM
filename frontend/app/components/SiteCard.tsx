import React from "react";
import Image from "next/image";
import Link from "next/link";

interface CardProps {
  title: string;
  imageSrc: string;
  alt: string;
}

const SiteCard: React.FC<CardProps> = ({ title, imageSrc, alt }) => {
  return (
    <>
      <div className="flex flex-col items-center p-4 bg-white rounded-lg shadow-md text-black h-full w-full">
        <h2 className="text-lg font-bold mt-2 ml-2 content-center">{title}</h2>
        <Image
          src={imageSrc}
          alt={alt}
          width={500}
          height={400}
          loading="lazy"
          className="rounded-lg object-cover w-full h-auto max-h-[300px] sm:max-h-[400px]"
        />
        <div className="flex flex-col sm:flex-row items-center sm:space-x-4 mt-4 space-y-2 sm:space-y-0">
          <button type="submit" className="font-semibold  hover:text-blue-500">
            Learn more...
          </button>
        </div>
      </div>
    </>
  );
};

export default SiteCard;
