// pages/index.tsx
"use client";

import React, { useState, useEffect } from "react";
import Itravel from "@/app/components/Itravel";
import Footer from "@/app/components/Footer";
import NumberSlider from "@/app/components/Slider";
import Preference from "@/app/components/Preference";
import Card from "@/app/components/Cards";
import data from "@/data/sitesData.json";

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

  const toggleOption = (option: string) => {
    setSelectedOptions((prevSelectedOptions) => {
      const newSelectedOptions = prevSelectedOptions.includes(option)
        ? prevSelectedOptions.filter((opt) => opt !== option)
        : [...prevSelectedOptions, option];

      return newSelectedOptions;
    });
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
  }, [day, preference]); // Dependencies to re-fetch when day or preference changes

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <ul className="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 gap-8 mt-20 mb-20 mx-28">
        {recommendedSites.map((site: string, index) => (
          <li key={index} className="flex py-1">
            <Card
              title={site}
              description={data[site as keyof typeof data]["content"]}
              imageSrc={data[site as keyof typeof data]["images"][0]}
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

        <form onSubmit={onSubmit}>
          <button
            type="submit"
            className="bg-green-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
          >
            旅程規劃
          </button>
        </form>
      </div>
      <h1>{selectedOptions.join(", ")}</h1>
    </div>
  );
};

const HomePage: React.FC = () => {
  const [day, setDay] = useState<number>(2);
  const [selectedOptions, setSelectedOptions] = useState<string[]>([]);
  const [submitted, setSubmitted] = useState<boolean>(false);

  const handlePreferenceChange = (value: string[]) => {
    setSelectedOptions(value);
  };

  const handleSliderChange = (value: number) => {
    setDay(value);
  };

  const handleSubmit = () => {
    setSubmitted(!submitted); // Set submitted to true to show confirmation
  };

  const options: Array<string> = [
    "親子旅遊",
    "文化古蹟",
    "美食之旅",
    "自然風光",
    "冒險體驗",
    "購物旅遊",
    "療癒放鬆",
    "生態旅遊",
    "藝術之旅",
  ];

  return (
    <>
      {submitted ? (
        <RecommendedSitesComponent
          day={day}
          preference={selectedOptions.join("、")}
          onChange={handleSubmit}
        />
      ) : (
        <div className="min-h-screen flex flex-col">
          <Itravel />
          <main className="flex-grow bg-gradient-to-b from-blue-50 to-blue-100">
            <div className="w-3/5 mx-auto content-center mt-20">
              <NumberSlider onValueChange={handleSliderChange} />
            </div>
            <div className="w-full mx-auto mt-20 content-center flex flex-col items-center">
              <Preference
                options={options}
                onPreferenceChange={handlePreferenceChange}
              />
              <button
                onClick={handleSubmit}
                className="bg-blue-700 text-white mb-10 py-2 px-5 font-bold rounded-lg hover:shadow-xl hover:bg-blue-800"
              >
                開始推薦
              </button>
            </div>
          </main>
          <Footer />
        </div>
      )}
    </>
  );
};

export default HomePage;
