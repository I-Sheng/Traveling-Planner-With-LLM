"use client";
import { useState, ChangeEvent } from "react";

interface SliderProps {
  onValueChange: (value: number) => void;
}

const Slider: React.FC<SliderProps> = ({ onValueChange }) => {
  const [value, setValue] = useState<number>(2);

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const newValue = Number(event.target.value);
    setValue(newValue);
    onValueChange(newValue); // Send the value to the parent
  };

  return (
    <div className="w-full px-4 py-6 bg-white shadow rounded-lg">
      <label
        htmlFor="customRange"
        className="block mb-2 text-sm font-medium text-gray-900"
      >
        Days for the trip
      </label>
      <div className="relative pt-1">
        <input
          type="range"
          id="customRange"
          className="w-full h-2 rounded-lg appearance-none cursor-pointer"
          min="1"
          max="5"
          value={value}
          onChange={handleChange}
          style={{
            background: `linear-gradient(to right, #10B981 0%, #10B981 ${
              ((value - 1) / 4) * 100
            }%, #cbd5e1 ${((value - 1) / 4) * 100}%, #cbd5e1 100%)`,
          }}
        />
      </div>
      <div className="flex justify-between text-xs px-2">
        <span>1</span>
        <span>5</span>
      </div>
      <div className="mt-4 text-center">
        <span className="text-lg font-semibold text-gray-900">{value} day</span>
      </div>
    </div>
  );
};

export default Slider;
