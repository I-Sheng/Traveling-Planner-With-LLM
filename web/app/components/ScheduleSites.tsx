"use client";

import React, { useState, useEffect } from "react";
import TravelCard from "./TravelCard";
import data from "@/data/sitesData.json";
import TravelTimeArrow from "./TravelTimeArrow";

interface ScheduleSitesProps {
  day: number;
  sites: string;
  start_time: number;
  end_time: number;
  start_point: string;
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
}) => {
  const [scheduleSites, setScheduleSites] = useState<NodeProps[]>([]);
  const [error, setError] = useState<string | null>(null);

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

        if (data.result && Array.isArray(data.result)) {
          setScheduleSites(data.result);
        } else {
          throw new Error("Unexpected data structure");
        }
      } catch (error: any) {
        setError(error.message);
      }
    }

    fetchScheduleSites();
  }, [sites]); // Dependencies to re-fetch when day or preference changes

  if (error) {
    return <p>Error: {error}</p>;
  }

  const transferArrivalTime = (time: number) => {
    time = time + start_time;
    let hours: number = (time / 60) | 0;
    let minutes: number = time % 60;
    return `${hours}時 ${minutes}分`;
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
      <ul className="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 gap-8 mt-20 mb-20 mx-28">
        {Object.entries(groupByDay(scheduleSites)).map(([vehicle, items]) => (
          <div key={vehicle} className="flex flex-col p-4 border rounded-md">
            {items.map((node: NodeProps, index) => (
              <li key={index} className="flex py-1">
                <TravelCard
                  title={node.name}
                  imageSrc={data[node.name as keyof typeof data]["images"][0]}
                  alt={node.name}
                  arrive_time={transferArrivalTime(node.arrival)}
                  stay_time={
                    node.end_node
                      ? null
                      : scheduleSites[index + 1].arrival -
                        node.travel -
                        node.arrival
                  }
                />
                {node.end_node === false && index !== 0 && (
                  <TravelTimeArrow travelTime={node.travel} />
                )}
              </li>
            ))}
          </div>
        ))}
      </ul>
    </div>
  );
};

export default ScheduleSitesComponent;
