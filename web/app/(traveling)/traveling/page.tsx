// pages/index.tsx
"use client";

import React, { useState } from "react";
import Preference from "@/app/components/Preference";
import RecommendedSitesComponent from "@/app/components/RecommendedSites";

const HomePage: React.FC = () => {
  const [selectedOptions, setSelectedOptions] = useState<string[]>([]);
  const [submitted, setSubmitted] = useState<boolean>(false);

  const handlePreferenceChange = (value: string[]) => {
    setSelectedOptions(value);
  };

  const day = 1;

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
          onSubmit={handleSubmit}
        />
      ) : (
        <div className="min-h-screen flex flex-col">
          <main className="flex-grow bg-gradient-to-b from-blue-50 to-blue-100">
            <div className="w-3/5 mx-auto flex flex-col justify-center items-center mt-20">
              <p className="content-center font-bold text-2xl mb-3">
                嘉義一日遊
              </p>
              <p className="content-center font-regular text-xl">
                起點: 嘉義火車站
              </p>
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
        </div>
      )}
    </>
  );
};

export default HomePage;
