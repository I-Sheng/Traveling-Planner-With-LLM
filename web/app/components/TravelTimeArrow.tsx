import React from "react";

interface TravelTimeArrowProps {
  travelTime: number;
}

const TravelTimeArrow: React.FC<TravelTimeArrowProps> = ({ travelTime }) => {
  const transferArrivalTime = (time: number) => {
    let hours: number = (time / 60) | 0;
    let minutes: number = time % 60;
    if (hours === 0) {
      return `${minutes}分`;
    }
    return `${hours}時 ${minutes}分`;
  };

  return (
    <div className="flex items-center">
      {/* Arrow */}
      <div className="flex flex-col items-center">
        {/* Arrow Line */}
        <div className="w-2 h-20 bg-blue-500"></div>
        {/* Arrow Head */}
        <div className="w-0 h-0 border-l-[12px] border-l-transparent border-r-[12px] border-r-transparent border-t-[12px] border-t-blue-500"></div>
      </div>

      {/* Travel Time Label */}
      <div className="text-2xl text-gray-800 font-semibold ml-2 mr-auto">
        {transferArrivalTime(travelTime)}
      </div>
    </div>
  );
};

export default TravelTimeArrow;
