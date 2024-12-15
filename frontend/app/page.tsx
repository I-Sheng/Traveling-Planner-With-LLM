// pages/index.tsx
import React from "react";
import Link from "next/link";

const HomePage: React.FC = () => {
  return (
    <Link
      href="/traveling"
      className="flex items-center justify-center h-screen bg-gray-100"
    >
      <button
        type="submit"
        className="bg-blue-600 text-white py-2 px-5 font-semibold rounded-lg shadow-md transition-transform transform hover:scale-105 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
        開始旅遊規劃
      </button>
    </Link>
  );
};

export default HomePage;