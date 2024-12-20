import data from "@/data/sitesData.json";
import SiteCard from "../components/SiteCard";
interface SiteNameProps {
  name: string;
}

const Site: React.FC = () => {
  return (
    <>
      <ul className="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 gap-8 mt-20 mb-20 mx-28">
        {Object.entries(data).map(([key, values]) => (
          <li key={key} className="flex py-1">
            <SiteCard
              title={key}
              imageSrc={`/images/${encodeURIComponent(key)}.jpg`}
              alt={key}
            />
          </li>
        ))}
      </ul>
    </>
  );
};

export default Site;
