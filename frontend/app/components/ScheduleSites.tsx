"use client";

import React, { useState, useEffect } from "react";
import TravelCard from "./TravelCard";
import TravelTimeArrow from "./TravelTimeArrow";
import Link from "next/link";

interface ScheduleSitesProps {
  day: number;
  sites: string;
  start_time: number;
  end_time: number;
  start_point: string;
  onSubmit: () => void;
}

interface NodeProps {
  arrival: number;
  end_node: boolean;
  name: string;
  service: number;
  travel: number;
  vehicle: number;
}
const ScheduleSitesComponent: React.FC<ScheduleSitesProps> = ({
  day,
  sites,
  start_time,
  end_time,
  start_point,
  onSubmit,
}) => {
  const [scheduleSites, setScheduleSites] = useState<NodeProps[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setLoading] = useState<boolean>(true);

  const handleSubmit = () => {
    onSubmit();
    setError(null);
    setScheduleSites([]);
  };
  useEffect(() => {
    async function fetchScheduleSites() {
      try {
        const response = await fetch("/api/routing", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            day,
            sites,
            start_time,
            end_time,
            start_point,
          }),
        });

        if (!response.ok) {
          throw new Error("Failed to fetch scheduled route");
        }

        const data = await response.json();

        setLoading(false);
        if (data.result && Array.isArray(data.result)) {
          setScheduleSites(data.result);
        } else {
          throw new Error("Unexpected data structure");
        }
      } catch (error: unknown) {
        if (error instanceof Error) {
          setError(error.message);
        } else {
          setError("An unknown error occurred");
        }
      }
    }

    fetchScheduleSites();
  }, [day, sites, start_time, end_time, start_point]); // Dependencies to re-fetch when day or preference changes

  if (error) {
    return <p>Error: {error}</p>;
  }

  const transferArrivalTime = (time: number) => {
    time = time + start_time;
    const hours: number = (time / 60) | 0;
    const minutes: number = time % 60;
    if (minutes < 10) {
      return `${hours}:0${minutes}`;
    }
    return `${hours}:${minutes}`;
  };

  const groupByDay = (data: NodeProps[]): Record<number, NodeProps[]> => {
    return data.reduce((acc: Record<number, NodeProps[]>, item) => {
      if (!acc[item.vehicle]) {
        acc[item.vehicle] = [];
      }
      acc[item.vehicle].push(item);
      return acc;
    }, {});
  };
  return (
    <div>
      <div className="mt-10">
        <h2 className="text-2xl font-bold text-center mb-6">行程安排</h2>
        <div className="bg-blue-100 p-6 rounded-lg shadow-lg">
          <ul className="space-y-4">
            {scheduleSites.map((node, index) => (
              <li
                key={index}
                className="flex flex-col items-start bg-white p-4 border rounded-lg shadow-md hover:shadow-lg transition-shadow"
              >
                <span className="text-lg font-semibold text-gray-700">
                  {node.name}
                </span>
                <span className="text-sm text-gray-500 mt-2">
                  {index === 0
                    ? `出發時間: ${transferArrivalTime(node.arrival)}`
                    : index === scheduleSites.length - 1
                    ? `結束時間: ${transferArrivalTime(node.arrival)}`
                    : `到達時間: ${transferArrivalTime(node.arrival)}`}
                </span>
              </li>
            ))}
          </ul>
        </div>
      </div>
      <h2 className="text-2xl font-bold text-center mt-16">行程詳情</h2>

      <ul className="flex flex-wrap gap-8 justify-center items-center mt-5 mb-20">
        {Object.entries(groupByDay(scheduleSites)).map(([vehicle, items]) => (
          <div
            key={vehicle}
            className="flex flex-col items-center justify-center p-4 border rounded-md"
          >
            {items.map((node: NodeProps, index) => (
              <React.Fragment key={index}>
                {/* TravelCard */}
                <li className="flex py-1">
                  <TravelCard
                    title={node.name}
                    index={index}
                    imageSrc={`/images/${node.name.replace(/\s/g, "_")}.jpg`}
                    alt={node.name}
                    arrive_time={transferArrivalTime(node.arrival)}
                    stay_time={
                      node.end_node || index == 0
                        ? null
                        : items[index + 1]?.arrival - node.travel - node.arrival
                      //node.service
                    }
                  />
                </li>

                {/* TravelTimeArrow */}
                {index !== items.length - 1 && (
                  <div className="flex justify-center my-2">
                    <TravelTimeArrow travelTime={node.travel} />
                  </div>
                )}
              </React.Fragment>
            ))}
          </div>
        ))}
      </ul>
      {!isLoading && (
        <div className="flex items-center justify-center gap-36 mt-5 mb-20">
          <form onSubmit={handleSubmit}>
            <button
              type="submit"
              className="bg-blue-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              上一頁
            </button>
          </form>
          <Link href="/">
            <button
              type="submit"
              className="bg-green-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
            >
              完成規劃
            </button>
          </Link>
        </div>
      )}
    </div>
  );
};

export default ScheduleSitesComponent;
