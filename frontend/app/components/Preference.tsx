"use client";
import { useState } from "react";

const Home: React.FC<{
  options?: string[];
  onPreferenceChange: (value: string[]) => void;
}> = ({ options = [], onPreferenceChange }) => {
  const [selectedOptions, setSelectedOptions] = useState<string[]>([]);

  const toggleOption = (option: string) => {
    setSelectedOptions((prevSelectedOptions) => {
      const newSelectedOptions = prevSelectedOptions.includes(option)
        ? prevSelectedOptions.filter((opt) => opt !== option)
        : [...prevSelectedOptions, option];

      return newSelectedOptions;
    });
    onPreferenceChange(selectedOptions);
  };

  const combinedText = selectedOptions.join("、");

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="text-xl font-bold mb-4">偏好選擇</h1>
      <div className="flex flex-wrap gap-4 justify-center">
        {options.map((option, index) => (
          <div
            key={index}
            onClick={() => toggleOption(option)}
            className={`cursor-pointer p-4 border rounded-md transition ${
              selectedOptions.includes(option)
                ? "bg-blue-500 text-white"
                : "bg-gray-200 text-gray-800"
            } hover:shadow-lg`}
          >
            {option}
          </div>
        ))}
      </div>

      {combinedText && (
        <div className="mt-4 p-4 bg-gray-100 rounded-md text-gray-800">
          <strong>偏好: </strong> {combinedText}
        </div>
      )}
    </div>
  );
};

export default Home;
