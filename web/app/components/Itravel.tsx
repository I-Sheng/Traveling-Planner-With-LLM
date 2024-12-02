// components/Header.tsx
import Link from "next/link";
import React from "react";

const Header: React.FC = () => {
  return (
    <header className="p-4 bg-blue-500 text-white flex justify-between items-center">
      <h1 className="text-2xl font-bold mx-auto">Itravel</h1>
    </header>
  );
};

export default Header;
