import React from "react";

interface SwitchProps {
  isOn: boolean;
  handleToggle: () => void;
  id: string;
}

const Switch: React.FC<SwitchProps> = ({ isOn, handleToggle, id }) => {
  return (
    <div className="relative w-12 h-6">
      <input
        checked={isOn}
        onChange={handleToggle}
        className="absolute w-0 h-0 opacity-0"
        id={id}
        type="checkbox"
      />
      <label
        htmlFor={id}
        className={`flex items-center justify-between w-full h-full rounded-full transition-colors duration-200 cursor-pointer ${
          isOn ? "bg-green-500" : "bg-gray-400"
        }`}
      >
        <span
          className={`absolute top-1 left-1 w-4 h-4 rounded-full bg-white shadow-md transform transition-transform duration-200 ${
            isOn ? "translate-x-6" : ""
          }`}
        />
      </label>
    </div>
  );
};

export default Switch;
