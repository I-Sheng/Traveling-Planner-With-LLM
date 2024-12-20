// pages/index.tsx
import React from "react";
import Link from "next/link";

const HomePage: React.FC = () => {
  return (
    <div className="flex items-center justify-center h-screen gap-16">
      <Link href="/traveling" passHref>
        <button
          type="submit"
          className="bg-blue-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        >
          開始旅遊規劃
        </button>
      </Link>
      <Link href="/sites" passHref>
        <button
          type="submit"
          className="bg-green-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
        >
          景點美食總覽
        </button>
      </Link>
    </div>
  );
};

export default HomePage;
