import data from "@/data/sitesData.json";
import { parseAppSegmentConfig } from "next/dist/build/segment-config/app/app-segment-config";
import Image from "next/image";

interface SiteProps {
  address: string;
  types: string[];
  rating: number | null;
  time_spent: number[];
  metadata: { type: string };
  name: string;
  content: string;
  opening_hours: string[];
}

const siteDataMap = data as Record<string, SiteProps>;

interface SiteParams {
  params: { name: string };
}

const Site = ({ params }: SiteParams) => {
  const { name } = params;
  console.log(name);

  const siteData = Object.values(siteDataMap).find(
    (data) => encodeURIComponent(data.name) === name
  );

  if (!siteData) {
    return (
      <div className="max-w-4xl mx-auto p-6 bg-gray-50 rounded-lg shadow-md">
        <h1 className="text-3xl font-bold mb-4 text-gray-800">
          Site Not Found
        </h1>
        <p className="text-gray-700">
          The site you are looking for does not exist.
        </p>
      </div>
    );
  }

  const averageStayTime =
    Math.ceil((siteData.time_spent[0] + siteData.time_spent[1]) / 2 / 5) * 5;

  return (
    <div className="max-w-4xl mx-auto p-6 bg-gray-50 rounded-lg shadow-md">
      <h1 className="text-3xl font-bold mb-4 text-gray-800">{siteData.name}</h1>
      <Image
        src={`/images/${siteData.name.replace(/\s/g, "_")}.jpg`}
        alt={siteData.name}
        width={600}
        height={450}
        className="rounded-lg object-cover w-full h-auto mb-6"
      />
      <p className="text-gray-700 mb-4">{siteData.content}</p>
      <div className="mb-4">
        <p className="text-sm font-semibold text-gray-600">地址: </p>
        <p className="text-gray-800">{siteData.address}</p>
      </div>
      {siteData.rating && (
        <div className="mb-4">
          <p className="text-sm font-semibold text-gray-600">評價: </p>
          <p className="text-gray-800">{siteData.rating.toFixed(1)}</p>
        </div>
      )}
      <div className="mb-4">
        <p className="text-sm font-semibold text-gray-600">預計停留時間:</p>
        <p className="text-gray-800">{averageStayTime} 分鐘</p>
      </div>
      <div className="mb-4">
        <p className="text-sm font-semibold text-gray-600">開放時間:</p>
        <ul className="text-gray-800">
          {siteData.opening_hours.map((hour, index) => (
            <li key={index} className="list-disc ml-6">
              {hour}
            </li>
          ))}
        </ul>
      </div>
      <div className="mb-4">
        <p className="text-sm font-semibold text-gray-600">景點標籤: </p>
        <ul className="flex flex-wrap gap-2">
          {siteData.types.map((type, index) => (
            <li
              key={index}
              className="bg-gray-200 text-gray-800 px-3 py-1 rounded-full text-sm"
            >
              {type}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Site;
