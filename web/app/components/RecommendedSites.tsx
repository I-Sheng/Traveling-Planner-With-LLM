"use client";

import React, { useState, useEffect } from "react";
import Card from "@/app/components/Cards";
import data from "@/data/sitesData.json";
import ScheduleSitesComponent from "./ScheduleSites";

interface RecommendedSitesProps {
  day: number;
  preference: string;
  onSubmit: () => void;
}

const RecommendedSitesComponent: React.FC<RecommendedSitesProps> = ({
  day,
  preference,
  onSubmit,
}) => {
  const [recommendedSites, setRecommendedSites] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [selectedOptions, setSelectedOptions] = useState<string[]>([]);
  const [submitted, setSubmitted] = useState<boolean>(false);

  const toggleOption = (option: string) => {
    setSelectedOptions((prevSelectedOptions) => {
      const newSelectedOptions = prevSelectedOptions.includes(option)
        ? prevSelectedOptions.filter((opt) => opt !== option)
        : [...prevSelectedOptions, option];

      return newSelectedOptions;
    });
  };

  const handleSubmit = () => {
    setSubmitted(!submitted); // Set submitted to true to show confirmation
  };

  const returnSubmit = () => {
    handleSubmit();
    setSelectedOptions([]);
  };

  useEffect(() => {
    async function fetchRecommendedSites() {
      try {
        const response = await fetch("/api/recommend", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ day, preference }),
        });

        if (!response.ok) {
          throw new Error("Failed to fetch recommended sites");
        }

        const data = await response.json();

        if (data.result && Array.isArray(data.result)) {
          setRecommendedSites(data.result);
        } else {
          throw new Error("Unexpected data structure");
        }
      } catch (error: any) {
        setError(error.message);
      }
    }

    fetchRecommendedSites();
    setSelectedOptions([]);
  }, [day, preference]); // Dependencies to re-fetch when day or preference changes

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <>
      {submitted ? (
        <ScheduleSitesComponent
          day={day}
          sites={selectedOptions.join(", ")}
          start_time={480}
          end_time={1200}
          start_point="嘉義火車站"
          onSubmit={returnSubmit}
        />
      ) : (
        <div>
          <ul className="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 gap-8 mt-20 mb-20 mx-28">
            {recommendedSites.map((site: string, index) => (
              <li key={index} className="flex py-1">
                <Card
                  title={site}
                  description={data[site as keyof typeof data]["content"]}
                  imageSrc={`images/${site}.jpg`}
                  alt={site}
                  onToggle={toggleOption}
                />
              </li>
            ))}
          </ul>
          <div className="flex items-center justify-center gap-36 mt-5 mb-20">
            <form onSubmit={onSubmit}>
              <button
                type="submit"
                className="bg-blue-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
              >
                上一頁
              </button>
            </form>

            <form onSubmit={handleSubmit}>
              <button
                type="submit"
                className="bg-green-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
              >
                旅程規劃
              </button>
            </form>
          </div>
        </div>
      )}
    </>
  );
};

export default RecommendedSitesComponent;
